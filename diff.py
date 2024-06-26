# This file grab the ouput of git diff and store it in a file called diff.txt
# The file diff.txt is then read and the lines are stored in a string called diff

import os
import subprocess


# Create a function that will grab the output of git diff and store it in a file called diff.txt
# Then read the file diff.txt and store the lines in a string called diff and remove the file diff.txt
# This function will be called in the main file and return the string diff


def git_diff():
    try:
        diff = ""
        # Create unified diff of the changes in the working directory
        subprocess.run(["git", "diff", "HEAD", "--cached", ">", "diff.txt"], shell=True)
        with open("diff.txt", "r") as file:
            diff = file.read()
        os.remove("diff.txt")
    except FileNotFoundError:
        diff = ""
    return diff
