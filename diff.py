import subprocess


def git_diff():
    """
    Captures the output of `git diff` and returns it as a string.

    Returns:
        str: The unified diff of the changes in the working directory.
    """
    try:
        # Run the git diff command and capture the output
        diff = subprocess.check_output(["git", "diff"], text=True)
        # get the git committer ident
        committer = subprocess.check_output(
            ["git", "var", "GIT_COMMITTER_IDENT"], text=True
        )
        print(f"Committer: {committer}")
        # Remove the time and timezone information from the committer after the ">"
        committer = committer.split(">")[0] + ">"
        # Add the committer information to the diff
        diff = f"Committer: {committer}\n{diff}"
    except subprocess.CalledProcessError as e:
        # Handle errors if the git command fails
        print(f"Error running git diff: {e}")
        diff = ""
    return diff
