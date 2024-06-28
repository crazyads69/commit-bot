import os
import subprocess
import platform


# Define the build_executable function that builds the commit-bot executable
def build_executable():
    print("Building commit-bot executable...")
    # Check platform if Windows and Linux then use the UPX compression to optimize the executable size
    if platform.system() != "Darwin":
        subprocess.run(
            [
                "pyinstaller",
                "commit-bot.py",
                "--onefile",
                "--runtime-hook",
                "./env.py",
                "--clean",
                "--strip",
                "--log-level=WARN",
                "--upx-dir",
                "./upx",  # Specify the path to UPX if needed
            ],
            check=True,
        )
    else:
        subprocess.run(
            [
                "pyinstaller",
                "commit-bot.py",
                "--onefile",
                "--runtime-hook",
                "./env.py",
                "--clean",  # Clean PyInstaller cache and remove temporary files before building
                "--strip",  # Strip the executable to reduce its size
                "--log-level=WARN",  # Reduce the verbosity of logs
            ],
            check=True,
        )
    print("Commit-bot executable built successfully.")


# Define the copy_executable function that copies the commit-bot executable to the current source directory
def copy_executable():
    print("Copying commit-bot executable...")
    if platform.system() == "Windows":
        subprocess.run(
            ["copy", "dist\\commit-bot.exe", "."],
            shell=True,
            check=True,
        )
    else:
        subprocess.run(
            ["cp", "-r", "dist/commit-bot", "."],
            check=True,
        )


# Define the change_permissions function that changes the permissions of the commit-bot executable
def change_permissions():
    if platform.system() != "Windows":
        print("Changing permissions of commit-bot executable...")
        subprocess.run(
            ["chmod", "+x", "commit-bot"],
            check=True,
        )


# Define the install_executable function that installs the commit-bot executable
def install_executable():
    if platform.system() == "Windows":
        install_on_windows()
    else:
        install_on_unix()


# Define the install_on_windows function that installs the commit-bot executable on Windows
def install_on_windows():
    print("Copying commit-bot executable to C:\\Program Files\\commit-bot...")
    install_path = "C:\\Program Files\\commit-bot"
    os.makedirs(install_path, exist_ok=True)
    subprocess.run(
        ["copy", "commit-bot.exe", install_path],
        shell=True,
        check=True,
    )
    add_to_path_windows(install_path)


# Define the add_to_path_windows function that adds the commit-bot executable to the PATH environment variable on Windows
def add_to_path_windows(install_path):
    print("Adding commit-bot to the PATH environment variable...")
    print("Make sure you have the necessary permissions to modify the PATH.")
    current_path = os.environ["PATH"]
    if install_path not in current_path:
        subprocess.run(
            f'setx PATH "{current_path};{install_path}"',
            shell=True,
            check=True,
        )
    print(
        "Commit-bot has been added to the PATH. You may need to restart your terminal or log out and log back in for the changes to take effect."
    )


# Define the install_on_unix function that installs the commit-bot executable on Unix-based systems
def install_on_unix():
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


def remove_excutable():
    print("Removing commit-bot executable...")
    if platform.system() == "Windows":
        subprocess.run(
            ["del", "commit-bot.exe"],
            shell=True,
            check=True,
        )
    else:
        subprocess.run(
            ["rm", "commit-bot"],
            check=True,
        )


if __name__ == "__main__":
    build_executable()
    copy_executable()
    change_permissions()
    install_executable()
    remove_excutable()
    print("Commit-bot executable has been successfully installed.")
