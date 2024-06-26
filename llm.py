from google.generativeai import GenerativeModel


def generate_commit_message(diff_input: str, model: GenerativeModel) -> str:
    SYSTEM_PROMPT = f"""
## Generate a High-Quality Git Commit Message

Please create a concise and informative commit message following best practices for Git commit messages.

**Context:**

The following is a diff of the changes made in this commit:
{diff_input}

**Commit Message Structure:**

<type>[optional scope]: <short summary>
[optional body]
[optional footer(s)]

**Commit Types:**

* **feat:** A new feature is introduced.
* **fix:** A bug fix is implemented.
* **chore:** Non-functional changes (e.g., updating dependencies).
* **refactor:** Code refactoring without fixing bugs or adding features.
* **docs:** Documentation updates.
* **style:** Code style changes (e.g., formatting).
* **test:** Adding or updating tests.
* **perf:** Performance improvements.
* **ci:** Continuous integration changes.
* **build:** Build system or external dependencies changes.
* **revert:** Reverting a previous commit.

**Guidelines:**

1. **Subject Line:**
   - Use imperative mood (e.g., "Add", "Fix", "Update").
   - Keep it concise (50 characters or less).
   - Capitalize the first letter.
   - Do not end with a period.

2. **Body:**
   - Use if more explanation is needed.
   - Wrap text at 72 characters.
   - Explain the "what" and "why" of the changes.

3. **Footer:**
    - Use for issue references (e.g., "Closes #123" or "Closes JIRA-123").
    - Include co-author information if necessary.

**Example:**

fix(auth): resolve login failure issue
This commit fixes the login failure issue that was occurring due to incorrect password hashing. The hashing algorithm has been updated to bcrypt.
Closes #456
Co-authored-by: Jiwon Choi <devjiwonchoi@gmail.com>

**Generate a commit message following these guidelines.**
"""
    try:
        response = model.generate_content(SYSTEM_PROMPT)
        return response.text
    except Exception as e:
        print(f"Error generating commit message: {e}")
        return ""
