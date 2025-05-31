# ✅ Incident Tracker - Ops Progress Checklist
## 🛠️ Core Functionalities
- [x] Flask app with SQLite backend
- [x] Pagination, search, and sorting
- [x] Create, edit, delete incidents
- [x] Log file setup with rotation
- [x] Home and create incident buttons in UI

## 🔧 Linux Admin Practice
### 🗂️ Log Management
- [x] Configure logging ; Custom log file: /var/log/incident-tracker/incident_tracker.log
- [x] Logrotate configuration (/etc/logrotate.d/incident_tracker)
- [ ] Optional: Centralize logs to another server or cloud service

### 🛡️ Backup & Recovery
- [x] Daily cron job to dump DB into /home/ubuntu/incident-tracker-backups
- [x] Verified dump file with timestamp format
- [ ] Store backups in a secure directory with proper permissions
- [ ] Optionally, upload backups to Amazon S3

### Others
- [x] Installed `tmux` for persistent sessions
- [ ] Re-installed `python3`

## 🔍 Monitoring (Planned / In Progress)
- [x] Use Icinga or Nagios to monitor Flask service uptime
- [ ] Set up alerts for high disk usage or error logs
- [ ] Monitor system resource metrics (CPU, memory)
- [ ] SQLite file existence or size
- [ ] Send alerts via email or Slack on critical issues
- [ ] TO DO: refine monitors

## Metrics
- [x] Added the incident-tracker host to the Grafana server

## 🔐 Security Hardening (Planned)
- [ ] Create a dedicated Linux user for running the app
- [ ] Configure UFW firewall (allow only SSH + web)
- [ ] Harden SSH access (disable password login)
- [ ] Set file/folder permissions for logs and backups
- [ ] Set up HTTPS with Let's Encrypt (via NGINX)
- [ ] Enable automatic security updates
- [ ] Install and configure fail2ban for SSH protection

## ☁️ AWS / Cloud Ops (Planned)
- [ ] Mount EBS volume for /var/log or /home/ubuntu/backups
- [ ] Sync backups to S3 using awscli
- [ ] Set up CloudWatch logs or custom metrics
- [ ] Create and attach an IAM role (for S3, CloudWatch, etc.)

## 🚀 CI/CD Automation (Planned)
- [ ] GitHub Actions to deploy on main push
- [ ] Auto restart systemd service after deployment
- [ ] Rollback plan or backup on deployment


## 🧪 Fault Testing & Resilience (Planned)
- [ ] Simulate app or DB crash
- [ ] Observe and log error behavior
- [x] [Restore sqlite db from backup and verify recovery ](https://github.com/sadieedwin/incident-tracker-web-app/blob/main/docs/sqlite-db-restore-simulation.md)
