# 🚨 Incident Tracker Web App

A lightweight web-based application to log, track, and manage operational incidents. Built with Python (Flask), deployed on a Linux server, and structured with real-world Ops practices in mind.

---

## 🔍 Project Overview

This project is designed to simulate a real enterprise environment for learning and portfolio purposes. It integrates web development with DevOps tools and workflows including Linux server setup, CI/CD, cloud deployment, and system monitoring.

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python (Flask)
- **Database**: MySQL (SQLite for local dev)
- **Web Server**: NGINX
- **OS**: Ubuntu (Linux)
- **CI/CD**: GitHub Actions
- **Cloud Hosting**: AWS EC2
- **Monitoring**: Icinga, custom scripts

---

## 🧱 System Architecture

```text
User --> NGINX --> Flask App --> MySQL Database
                       ↑
       Deployed from GitHub Actions --> AWS EC2
🚀 Getting Started
🖥️ Local Setup
1. Clone the repo
git clone https://github.com/your-username/incident-tracker.git
cd incident-tracker

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app
python app.py

☁️ EC2 Deployment (Basic Steps)
- Launch Ubuntu EC2 on AWS
- SSH into your instance
- Install Python, pip, Git, Flask
- Clone your repo
- Configure NGINX as reverse proxy
- Use systemd to run Flask as a service
- Secure with Let’s Encrypt SSL

Detailed instructions coming soon in /docs/server-setup.md

🗃️ Database Schema

Table: incidents
- id (Primary Key)
- title
- description
- severity (Low, Medium, High)
- status (Open, Closed)
- created_at
- updated_at

🔁 CI/CD with GitHub Actions
Every push to main triggers:
Linting / basic test
Deployment script (using SSH)

Example workflow file: .github/workflows/deploy.yml

📈 Monitoring
- App logs are stored in /var/log/incident-tracker/
- Custom script or Icinga checks availability
- Systemd restart policy ensures uptime

📸 Screenshots
Coming soon...
![Incident Tracker](https://github.com/user-attachments/assets/397ee894-9dd6-45a1-9604-6bbcf9cf4831)



📚 What I Learned
- Deploying Flask on a real Linux server
- Using NGINX as a reverse proxy
- Setting up CI/CD pipelines with GitHub Actions
- Managing a web app with systemd
- Connecting Python backend to SQL databases

🧭 Future Improvements
- Dockerize the app
- Add user authentication
- REST API endpoints
- Move DB to AWS RDS
- Add alerting/notifications
- Build dashboard with incident analytics

👨‍💻 Author
Edwin Sadie
Operations Engineer | Linux Enthusiast | DevOps Explorer
[www.linkedin.com/in/sadieedwin] | [https://github.com/sadieedwin]
