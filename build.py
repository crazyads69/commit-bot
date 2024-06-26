# Use pyinstaller to create an executable file from commit-bot.py. Run the executable file to generate a commit message and commit the changes to the repository.

import subprocess

print("Building commit-bot executable...")
subprocess.run(
    ["pyinstaller", "commit-bot.py", "--onefile", "--runtime-hook", "./env.py"],
    check=True,
)
print("Commit-bot executable built successfully.")
