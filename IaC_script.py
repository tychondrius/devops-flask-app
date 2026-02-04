#!/usr/bin/env bash

# ==========================================================

# DevOps Principles and Practice – Assessment Task 2 (IaC)

# Student Number: 30174846

#

# Automates:

# - Update Ubuntu to latest version

# - Install Python + Flask (via pipx – Ubuntu 24.04 safe)

# - Install Git

# - Install Docker and Docker Compose

# ==========================================================

set -e

echo "=== Task 2 IaC script started: $(date) ==="

# 1. Update Ubuntu

sudo apt update -y

sudo apt upgrade -y

# 2. Install Python tooling

sudo apt install -y python3 python3-pip python3-venv

# 3. Install pipx and Flask

sudo apt install -y pipx

sudo apt install -y python3-flask

pipx ensurepath || true

export PATH="$PATH:$HOME/.local/bin"

if ! command -v flask >/dev/null 2>&1; then

  pipx install flask

fi

# 4. Install Git

sudo apt install -y git

# 5. Install Docker + Docker Compose

sudo apt install -y ca-certificates curl gnupg lsb-release

sudo install -m 0755 -d /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \

sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \

"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu \

$(. /etc/os-release && echo ${UBUNTU_CODENAME}) stable" | \

sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update -y

sudo apt install -y docker.io

sudo apt install -y docker-compose

sudo systemctl enable docker

sudo systemctl start docker

sudo usermod -aG docker ubuntu

# 6. Verification

echo "=== Verification ==="

python3 --version

git --version

docker --version

docker-compose --version

flask --version

echo "=== Task 2 IaC script completed successfully ==="

echo "Please log out and back in (or reboot) to apply Docker permissions."