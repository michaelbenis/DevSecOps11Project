# "import os" is importing the Python's built-in library for interacting with the operating system.
# This library provides a way to access environment variables and other system information.
# In this script, we use os.environ.get() method to access the REPO_TO_CLONE and BRANCH_TO_MERGE environment variables passed to the container.
import os

# "import git" is importing the GitPython library,
# which allows us to interact with git repositories using Python.
# This library provides an easy-to-use interface to the git command line,
# allowing us to perform various git operations such as cloning, checking out branches,
# and merging within our Python script.
import git

# "import re" is importing the Python's built-in library for regular expressions.
# This library provides a set of functions to work with regular expressions,
# which are a way of searching and manipulating strings based on patterns.
# In this script, the regular expression library is used to check if the git URL passed as an environment variable is from GitHub.
# The reason why we need it in this script is to ensure that the script only works with GitHub repositories,
# and to prevent the script from trying to clone or merge from an invalid URL.
import re

# Get git URL from environment variable
url = os.environ.get('REPO_TO_CLONE')

# Check if the URL is from GitHub
if re.match(r"https://github.com/.*", url):
    # Check if the repository exists locally
    try:
        repo = git.Repo("./NewRepo")
    except git.exc.InvalidGitRepositoryError:
        # Clone the repository
        repo = git.Repo.clone_from(url, "./NewRepo")
    except Exception as e:
        print(e)
        raise SystemExit
    # Check if the branch exists, if not create it
    try:
        branch_name = os.environ.get('BRANCH_TO_MERGE')
        branch = repo.create_head(branch_name)
    except git.exc.GitCommandError:
        branch = repo.heads[branch_name]
    # Checkout the branch
    branch.checkout()
    # Attempt to merge the branch
    try:
        repo.git.merge("main")
    except git.exc.GitCommandError as e:
        if "CONFLICT" in e.stderr:
            # Handle merge conflicts
            print("Conflicts: ")
            print(e.stderr)
            resolve = input("Resolve conflicts and enter 'y' to continue: ")
            if resolve == "y":
                repo.git.add(A=True)
                repo.index.commit("Resolved conflicts")
    except Exception as e:
        print(e)
        raise SystemExit
else:
    print("you should use Github link only")