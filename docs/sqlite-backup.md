### 🗃️ SQLite Database Backup via Cron

To automate **daily backups** of the SQLite database (`incidents.db`), I created a cron job:

0 2 * * * /usr/bin/sqlite3 /home/ubuntu/incident-tracker-web-app/incidents.db .dump > /home/ubuntu/incident-tracker-backups/db-$(date +\%F).sql && find /home/ubuntu/incident-tracker-backups -name "db-*.sql" -type f -mtime +7 -delete


- **Runs daily at 2:00 AM**
- **Backs up the entire DB** into a timestamped SQL dump
- **Destination:** `/home/ubuntu/backups/`
- **Note:** Created the directory manually to avoid `No such file or directory` error.
