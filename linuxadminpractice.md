## 🐧 Linux System Administration Practice Tasks

For the Incident Tracker Project
This section outlines practical Linux administration tasks that can be incorporated into the Incident Tracker project to simulate real-world ops scenarios.


**✅ 1. Systemd Service Management**

Manage the Flask app using a custom systemd service.

- Create and manage a service unit:
/etc/systemd/system/incident-tracker.service

- Useful commands:

sudo systemctl start incident-tracker

sudo systemctl enable incident-tracker

sudo systemctl status incident-tracker

sudo journalctl -u incident-tracker

**✅ 2. Logging & Log Rotation**

App logs are written to /var/log/incident-tracker/incident_tracker.log.

- Set up log rotation with logrotate:

sudo nano /etc/logrotate.d/incident-tracker

Example config:


    /var/log/incident-tracker/incident_tracker.log {

    weekly
    
    rotate 4
    
    compress
    
    delaycompress
    
    missingok
    
    notifempty
    
    create 0640 ubuntu adm 
    
    }

**✅ 3. File & Directory Permissions**

- Use a dedicated Linux user to run the app.

- Restrict access to logs and app files:

sudo chown -R ubuntu:www-data /home/ubuntu/incident-tracker-web-app

sudo chmod 750 /var/log/incident-tracker

**✅ 4. Firewall & Security**

- Allow only necessary traffic:

sudo ufw allow 80/tcp

sudo ufw allow 443/tcp

sudo ufw enable

- Disable unused ports and services.

**✅ 5. Scheduled Backups with Cron**

Create automated database backups using cron.

- Example cron job:

0 2 * * * /usr/bin/sqlite3 /path/to/incidents.db .dump > /home/ubuntu/backups/db-$(date +\%F).sql

- Use cron.daily or cron.weekly as well.

**✅ 6. Monitoring & Alerts**

- Use tools like htop, top, free, df, and vmstat to monitor:

- CPU

- Memory

- Disk usage

- Optional: simulate real monitoring with Icinga, Nagios, or Prometheus.

  - Example: alert if memory usage > 80%

  - HTTP health checks for uptime monitoring

**✅ 7. NGINX Reverse Proxy + SSL**

Serve the Flask app behind NGINX.

- Basic reverse proxy:

    location / {

    proxy_pass http://127.0.0.1:8000;
    
    proxy_set_header Host $host;
    
    proxy_set_header X-Real-IP $remote_addr;
    
    }
    
- Add free HTTPS with Certbot:

sudo apt install certbot python3-certbot-nginx

sudo certbot --nginx

**✅ 8. Backup and Restore Simulation**

- Simulate disaster recovery:
  - Break the DB
  - Restore from .sql dump

- Use sqlite3 to reload:
- 
sqlite3 incidents.db < backup.sql

**✅ 9. Disk Space Monitoring**

- Create a script to monitor disk usage:

    #!/bin/bash

    usage=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

    if [ "$usage" -gt 80 ]; then

    echo "Disk usage is critically high: $usage%" | mail -s "Disk Alert" your@email.com
    
    fi
    
- Add to crontab to run every hour.

**✅ 10. System Hardening & Updates**

- Regular system updates:

sudo apt update && sudo apt upgrade

- Hardening steps:
  - Disable unused services
  - Use SSH keys instead of passwords
  - Change default SSH port
  - Use fail2ban for brute-force protection
  
  ---
## 🔧 Ops Project Progress – Log Rotation, Backups, and Session Management

### 📁 Log Rotation Configuration

I configured **log rotation** for the incident tracker application logs located at `/var/log/incident-tracker/incident_tracker.log`. This helps manage log file size and keeps logs organized.

**Logrotate Config:**

    /var/log/incident-tracker/incident_tracker.log { 

    weekly # Rotate logs weekly 
    
    rotate 4 # Keep 4 archived logs 
    
    compress # Compress old logs to save space 
    
    delaycompress # Delay compression until next rotation 
    
    missingok # Ignore if log file is missing 
    
    notifempty # Don’t rotate empty logs 
    
    create 0640 ubuntu adm # Create new logs with this permission and ownership
    
    }


✅ Added inline comments for clarity and maintainability.  
✅ Validated that log rotation will keep the logs under control automatically.

---

### 🗃️ SQLite Database Backup via Cron

To automate **daily backups** of the SQLite database (`incidents.db`), I created a cron job:

0 2 * * * /usr/bin/sqlite3 /home/ubuntu/incident-tracker-web-app/incidents.db .dump > /home/ubuntu/incident-tracker-backups/db-$(date +\%F).sql && find /home/ubuntu/incident-tracker-backups -name "db-*.sql" -type f -mtime +7 -delete


- **Runs daily at 2:00 AM**
- **Backs up the entire DB** into a timestamped SQL dump
- **Destination:** `/home/ubuntu/backups/`
- **Note:** Created the directory manually to avoid `No such file or directory` error.

---

### 🔄 Installed `tmux` for Persistent SSH Sessions

To avoid session loss due to SSH disconnects or idle timeouts:
sudo apt install tmux

Now using `tmux` for safe, resumable work sessions:
tmux # Start a new session tmux attach # Reconnect to an existing session


🔒 Protects long-running tasks and CLI work even if SSH drops.

---

### ✅ Summary of Ops Improvements

- [x] Log rotation implemented and documented  
- [x] Cron job for SQLite backups in place  
- [x] `tmux` installed for persistent terminal sessions  






