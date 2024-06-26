# Use pyinstaller to create an executable file from commit-bot.py. Run the executable file to generate a commit message and commit the changes to the repository.

from re import sub
import subprocess

print("Building commit-bot executable...")
subprocess.run(
    ["pyinstaller", "commit-bot.py", "--onefile", "--runtime-hook", "./env.py"],
    check=True,
)
print("Commit-bot executable built successfully.")

# Copy the excutable to the current directory
print("Copying commit-bot executable...")
subprocess.run(
    ["cp", "-r", "dist/commit-bot", "."],
    check=True,
)

# Change the permissions of the executable
print("Changing permissions of commit-bot executable...")
subprocess.run(
    ["chmod", "+x", "commit-bot"],
    check=True,
)

# Copy the commit-bot executable to the /usr/local/bin directory
print("Copying commit-bot executable to /usr/local/bin...")
print("You may be prompted for your password.")
subprocess.run(
    ["sudo", "cp", "-r", "commit-bot", "/usr/local/bin/"],
    check=True,
)
subprocess.run(
    ["sudo", "chmod", "755", "/usr/local/bin/commit-bot"],
    check=True,
)
print("Commit-bot executable has been successfully installed.")
