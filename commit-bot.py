from diff import git_diff
import click
from llm import generate_commit_message
import os
import dotenv
import google.generativeai as genai
import subprocess


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
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Get the diff of the current changes
    diff = git_diff()
    if diff:
        commit_message = generate_commit_message(diff, model)

        if commit_message:
            # Grab the first line of the commit message to use as the commit title
            commit_title = commit_message.split("\n")[0]
            # Use the leftover commit message as the commit body
            commit_body = "\n".join(commit_message.split("\n")[1:])

            # Stage all changes
            subprocess.run(["git", "add", "."], check=True)

            # Run the git commit command with the commit title and body
            subprocess.run(
                ["git", "commit", "-m", commit_title, "-m", commit_body], check=True
            )

            # Grab the commit hash of the last commit
            commit_hash = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], text=True
            ).strip()
            click.echo(
                f"Commit message generated and committed with hash: {commit_hash}"
            )
        else:
            click.echo("Failed to generate a commit message.")
    else:
        click.echo("No changes found.")


if __name__ == "__main__":
    main()
