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

🚀 Getting Started
🖥️ Local Setup
1. Clone the repo

2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
- Python 3.8+
- pip
- SQLite
- Flask
- Gunicorn (for deployment)
- Linux (Ubuntu tested)

4. Run the app
python app.py

☁️ EC2 Deployment (Basic Steps)
- Launch Ubuntu EC2 on AWS
- SSH into your instance
- Install Python, pip, Git, Flask
- Clone repo
- Configure NGINX as reverse proxy
- Use systemd to run Flask as a service

Detailed instructions coming soon...

🗃️ Database Schema

Table: incidents
- id (Primary Key)
- title
- description
- priority
- resolutionn
- root_cause
- created_at
- updated_at

🔁 CI/CD with GitHub Actions (Plan)

📈 Monitoring (Plan/InProgress)
- App logs are stored in /var/log/incident-tracker/
- Custom script or Icinga checks availability
- Systemd restart policy ensures uptime

📸 Screenshots
Updating soon...
![Incident Tracker](https://github.com/user-attachments/assets/397ee894-9dd6-45a1-9604-6bbcf9cf4831)

📚 What I Learned
- Deploying Flask on a real Linux server
- Using NGINX as a reverse proxy
- Setting up CI/CD pipelines with GitHub Actions (plan)
- Managing a web app with systemd
- Connecting Python backend to SQL databases

🧭 Future Improvements
- Dockerize the app
- Add user authentication
- Migrate from SQLite to MySQL and maybe go to AWS RDS
- Add alerting/notifications

👨‍💻 Author
Edwin Sadie
Operations Engineer | Fool Stuck Engineer
[www.linkedin.com/in/sadieedwin] | [https://github.com/sadieedwin]
