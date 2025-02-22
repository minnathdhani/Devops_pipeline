# 🔥 DevOps Pipeline

Welcome to our **CI/CD Project** repository! This project demonstrates a continuous integration and continuous deployment (CI/CD) pipeline using GitHub, Python, Bash, and Nginx.

## 📌 Key Contributors
- Tanuj
- Minnath
- Shraddha
- Harjeet
- Jasmine
- Aniruddha
- Ankit

## 📂 Project Structure  
- **index.html** - Landing page of the site.
- **requirements.txt** - Dependencies required for running the scripts.

## Overview of the Setup
1. **Push Code from Windows to GitHub**: Developers push their code changes to the GitHub repository.
2. **Set Up the Ubuntu Server for Deployment**: An Ubuntu server is configured to host the application.
3. **Create a Python Script to Check for New Commits**: A Python script checks for new commits in the GitHub repository.
4. **Create a Bash Script for Deployment**: A Bash script pulls the latest code and restarts the Nginx server.
5. **Set Up a Cron Job to Run the Python Script**: A cron job automates the execution of the Python script at regular intervals.
6. **Test the Setup**: Verify that the deployment process works as expected.

## Installation Instructions

### Need to Install the Following on Your Ubuntu/Linux
```bash
sudo apt install -y nginx 
sudo apt install -y git
sudo apt install -y python3
sudo apt install pipx -y
pipx ensurepath
pipx install PyGithub
```

### Clone the Repository in Ubuntu
1. **Set Up Your SSH**: Ensure your SSH keys are configured for GitHub.
2. **Clone the Repository**:
   ```bash
   git clone <your-repo-name>
   ```

### Token Setup Instructions

#### For Windows
1. Install `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```
2. Create a `.env` file in the root directory.
3. Add the required variables (e.g., `GITHUB_TOKEN="your_key"`).
4. Ensure to put `.env` under `.gitignore` to keep it safe from commits.

#### For Ubuntu
1. Install `python-dotenv` using pipx:
   ```bash
   pipx install python-dotenv
   ```
2. Create a `.env` and `.gitignore` file in the "Devops_pipeline" directory.
3. Add the required variables (e.g., `GITHUB_TOKEN="your_key"`).
4. Ensure to put `.env` under `.gitignore` to keep it safe from commits.

## Validation Steps

### Python & Git Version Validation
```bash
python3 --version
git --version
```

### Nginx Validation Status
```bash
sudo systemctl status nginx
```
- If not running, start it using:
```bash
sudo systemctl start nginx
```

### Set Up a Cron Job to Run the Python Script
1. Edit the crontab:
   ```bash
   crontab -e
   ```
2. Add the following line to run the Python script every minute:
   ```bash
   * * * * * /usr/bin/python3 $HOME/Devops_CICD/check_commits.py >> $HOME/Devops_pipeline/log/check_commits.log 2>&1
   ```

### Validation Steps for Cron
1. List current cron jobs:
   ```bash
   crontab -l
   ```
2. Check the status of the cron service:
   ```bash
   systemctl status cron
   ```
   - If it's not running, start it:
   ```bash
   sudo systemctl start cron
   ```
3. Restart the cron service if needed:
   ```bash
   sudo systemctl restart cron
   ```

### Check Cron Logs for Errors
```bash
sudo journalctl -u cron --since "1 hour ago"
```

## Conclusion
- ✅ **Windows system** → Pushes code to GitHub
- ✅ **Ubuntu server** → Pulls the latest code using Python & Bash
- ✅ **Cron job** → Automates deployment every minute 🚀
