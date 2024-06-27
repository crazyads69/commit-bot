# commit-bot

## Overview

`commit-bot` is a tool designed to automate the process of generating commit messages, adding new changes to your project, and pushing them to the current HEAD branch. This tool leverages the Gemini AI to create high-quality commit messages based on the diff of the changes made in your project.

## Installation

### Step 1: Install Dependencies

Ensure you have all the necessary dependencies by installing them from `requirements.txt`:

```sh
    pip install -r requirements.txt
```

### Step 2: Obtain Gemini API Key

You will need an API key from Gemini Studio. Follow the steps below to set up your API key:

1. Obtain your Gemini API Key from Gemini Studio.
2. Rename `env_example.py` to `env.py`
3. Update the API Key in `env.py`:

```python
    os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"
```

### Step 3: Build the Project

Run the build.py script and wait for a success message indicating the installation is complete. **On Windows, make sure you run the build script with administrator permissions.**

```sh
    python build.py
```

## Usage

To use the commit-bot, navigate to the project directory where you want to commit changes and run the following command:

```sh
    commit-bot
```

The commit-bot will:

- Generate a commit message based on the diff of the changes.
- Add the new changes to the staging area.
- Commit the changes with the generated commit message.
- Push the changes to the current HEAD branch.

## Example

Navigate to your project directory:

```sh
    cd /path/to/your/project
```

Run the commit-bot command:

```sh
    commit-bot
```

The bot will handle the rest, ensuring your changes are committed and pushed efficiently.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.
Happy coding!

Feel free to modify or extend this `README.md` to better fit any additional specifics or requirements of your project.
