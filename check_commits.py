from github import Github
from dotenv import load_dotenv
import os, requests

load_dotenv()

# GitHub repository details
GITHUB_REPO = "minnathdhani/Devops_pipeline"  # Change this
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Use a GitHub token with repo read access

# Get the current user's home directory dynamically
HOME_DIR = os.path.expanduser("~")
LOCAL_COMMIT_FILE = f"{HOME_DIR}/Devops_CICD/log/latest_commit.txt"
DEPLOY_SCRIPT = f"{HOME_DIR}/Devops_CICD/deploy.sh"

def get_latest_commit():
    url = f"https://api.github.com/repos/{GITHUB_REPO}/commits/main"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()["sha"]
    else:
        print("Error fetching latest commit.")
        return None

def load_saved_commit():
    if os.path.exists(LOCAL_COMMIT_FILE):
        with open(LOCAL_COMMIT_FILE, "r") as file:
            return file.read().strip()
    return None

def save_commit(commit_sha):
    with open(LOCAL_COMMIT_FILE, "w") as file:
        file.write(commit_sha)

def main():
    latest_commit = get_latest_commit()
    saved_commit = load_saved_commit()

    if latest_commit and latest_commit != saved_commit:
        print("New commit found! Deploying...")
        os.system(f"bash {DEPLOY_SCRIPT}")
        save_commit(latest_commit)
        print("Deployment Completed Successfully.")
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()