# ✅ Incident Tracker - Ops Progress Checklist
## 🛠️ Core Functionalities
- [x] Flask app with SQLite backend
- [x] Pagination, search, and sorting
- [x] Create, edit, delete incidents
- [x] Log file setup with rotation
- [x] Home and create incident buttons in UI

## 🔧 Linux Admin Practice
### 🗂️ Log Management
- [x] Custom log file: /var/log/incident-tracker/incident_tracker.log
- [x] Logrotate configuration (/etc/logrotate.d/incident_tracker)
- [ ] Weekly rotation, compression, and retention

### 🛡️ Backup & Recovery
- [x] Daily cron job to dump DB into /home/ubuntu/incident-tracker-backups
- [x] Verified dump file with timestamp format
- [ ] Log and backup directories created with proper permissions

### Others
- [x] Installed `tmux` for persistent sessions
- [ ] Re-installed `python3`

## 🔍 Monitoring (Planned / In Progress)
- [x] Use Icinga or Nagios to monitor Flask service uptime
- [ ] Set up alerts for high disk usage or error logs
- [ ] Monitor system resource metrics (CPU, memory)
- [ ] TO DO: refine monitors

## 🔐 Security Hardening (Planned)
- [ ] Configure UFW firewall (allow only SSH + web)
- [ ] Harden SSH access (disable password login)
- [ ] Set file/folder permissions for logs and backups
- [ ] Set up HTTPS with Let's Encrypt (via NGINX)

## ☁️ AWS / Cloud Ops (Planned)
- [ ] Mount EBS volume for /var/log or /home/ubuntu/backups
- [ ] Sync backups to S3 using awscli
- [ ] Set up CloudWatch logs or custom metrics

## 🚀 CI/CD Automation (Planned)
- [ ] GitHub Actions to deploy on main push
- [ ] Auto restart systemd service after deployment
- [ ] Rollback plan or backup on deployment


## 🧪 Fault Testing & Resilience (Planned)
- [ ] Simulate app or DB crash
- [ ] Observe and log error behavior
- [ ] Restore from backup and verify recovery
