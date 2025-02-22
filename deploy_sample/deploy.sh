#!/bin/bash

# Get the current user's home directory
USER_HOME=$(eval echo ~$(whoami))
PROJECT_DIR="$USER_HOME/Devops_CICD"
REPO_DIR="$PROJECT_DIR/Devops_pipeline"
SUDOERS_FILE="/etc/sudoers.d/nginx_restart"
LOG_FILE="$PROJECT_DIR/log/deploy.log"

# Ensure the log directory exists
mkdir -p $PROJECT_DIR/log

# Log start
echo "Starting deployment at $(date)" >> $LOG_FILE

# Add sudoers rule if not exists
USERNAME=$(whoami)
RULE="$USERNAME ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx"

# Check if rule is already present
if ! sudo grep -Fxq "$RULE" $SUDOERS_FILE 2>/dev/null; then
    echo "$RULE" | sudo tee $SUDOERS_FILE > /dev/null
    echo "Added sudoers rule for Nginx restart" >> $LOG_FILE
else
    echo "Sudoers rule already exists" >> $LOG_FILE
fi

# Pull latest changes or clone if missing
if [ -d "$REPO_DIR/.git" ]; then
    cd $REPO_DIR
        if ! git pull origin main; then
        log_message "Git pull failed!"
        exit 1
else
    if ! git clone https://github.com/minnathdhani/Devops_pipeline.git "$REPO_DIR"; then
        log_message "Git clone failed!"
        exit 1
    fi
fi

# Restart Nginx
export SUDO_ASKPASS=~/askpass.sh
sudo -A systemctl restart nginx

# Log completion
echo "Deployment completed at $(date)" >> $LOG_FILE
