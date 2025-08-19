# What is it?
Python wrapper for the Instagram API and the Instagram Graph API v23.

# Benefits of using this library
- Publish posts, reels and stories on Instagram.
- You will be able to use it in your app if it requires some form of Instagram integration.
- You won't need to write raw http queries to interact with the Instagram API and the Instagram Graph API.
- Plug and play parts from this library without wasting time in the Instagram API documentation.

# Why I am making this?
- Because the current Python wrappers are either outdated. I tried using a famous Instagram API wrapper which had some 300 stars but turns out it hasn't been updated since 9 months at the time of writing this sentence.
- So that I don't need to write raw http queries in my python code as I think it makes the code unnecessarily hard to read, especially for people new in coding.
- If I have this problem, then I think other people might have it as well. So, a part of the inspiration is altruism also.
- I have never made a Python library before so it will be a good learning experience as well.

# Basics about the directory structure
- `tests/`: contains unit tests.
- `.gitignore`: contains a list of files to be ignored for committing.
- `requirements.txt`: contains the packages required by this project.
- `Notes.md`: contains raw ideas and braindump about the project.
- `README.md`: contains information about the project.
- `LICENSE`: contains the license of the project.
- If a directory contains `Notes.md` or `README.md`, it means that those files are applicable for that specific directory only. For example, `Notes.md` inside the `tests/` directory contains the braindump and raw ideas related to testing only.
- `venv`: contains the virtual environment.
- `dev-venv`: contains the virtual environment for testing.