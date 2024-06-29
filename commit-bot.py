from calendar import c
from diff import git_diff
import click
from llm import generate_commit_message
import os
import dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import subprocess
import time


def generate_and_commit(model):
    # Get the diff of the current changes
    diff = git_diff()
    if not diff:
        click.echo("No changes are found.")
        return

    while True:
        commit_message = generate_commit_message(diff, model)
        if commit_message:
            # Remove unwanted characters from the commit message
            commit_message = (
                commit_message.replace("```", "")
                .replace("**", "")
                .replace("`", "")
                .replace("#", "")
                .replace("*", "")
                .strip()
            )
            # Check if the first line of the commit message is in the required format
            if not commit_message.startswith(
                (
                    "feat:",
                    "fix:",
                    "chore:",
                    "refactor:",
                    "docs:",
                    "style:",
                    "test:",
                    "perf:",
                    "ci:",
                    "build:",
                    "revert:",
                    "feat(",
                    "fix(",
                    "chore(",
                    "refactor(",
                    "docs(",
                    "style(",
                    "test(",
                    "perf(",
                    "ci(",
                    "build(",
                    "revert(",
                )
            ):
                click.echo("The commit message does not follow the required format.")
                click.echo(commit_message)
                click.echo("Retrying in 1 minute...")
                for remaining in range(60, 0, -1):
                    print(f"Retrying in {remaining} seconds...", end="\r")
                    time.sleep(1)
                continue

            # Grab the first line of the commit message to use as the commit title
            commit_title = commit_message.split("\n")[0]
            # Use the leftover commit message as the commit body
            commit_body = "\n".join(commit_message.split("\n")[1:])
            # Run the git commit command with the commit title and body
            subprocess.run(
                ["git", "commit", "-m", commit_title, "-m", commit_body], check=True
            )
            # Check the current branch
            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"], text=True
            ).strip()

            # Push the commit to the remote repository
            subprocess.run(["git", "push", "-u", "origin", branch], check=True)

            # Grab the commit hash of the last commit
            commit_hash = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], text=True
            ).strip()
            click.echo(
                f"Commit message generated and committed with hash: {commit_hash}"
            )
            break
        else:
            click.echo("Failed to generate a commit message.")
            click.echo("Retrying in 1 minute...")
            for remaining in range(60, 0, -1):
                print(f"Retrying in {remaining} seconds...", end="\r")
                time.sleep(1)


@click.command()
def main():
    # Progress bar
    click.echo("Generating commit message...")
    # Load env
    dotenv.load_dotenv()

    # Set the API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        "gemini-1.5-pro-latest",
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
        generation_config=genai.types.GenerationConfig(
            # Only one candidate for now.
            max_output_tokens=8192,
            temperature=0.6,
            top_p=1.0,
        ),
    )

    generate_and_commit(model)


if __name__ == "__main__":
    main()
