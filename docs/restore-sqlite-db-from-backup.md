# 🔁 Restoring the SQLite Database from Backup

If the `incidents.db` file is accidentally deleted or corrupted, you can restore it from a backup `.sql` file.

## 🧰 Prerequisites

- Ensure the backup file exists in the `incident-tracker-backups` directory.
- Example backup file name: `db-2025-05-01.sql`.

---

## ✅ Steps to Restore

### 1. Stop the Flask Application
It's a good idea to stop the app before restoring the database to avoid any conflicts:
```bash
sudo systemctl stop incident-tracker.service
```
### 2. Navigate to the Project Directory
```bash
cd /home/ubuntu/incident-tracker-web-app
```

### 3. Restore the Database
Use the SQLite .sql dump file to recreate the database:
```bash
sqlite3 incidents.db < /home/ubuntu/incident-tracker-backups/db-2025-05-01.sql
```
### 4. Restart the Application
```bash
sudo systemctl start incident-tracker.service
```
### 5. Check the Status
```
sudo systemctl status incident-tracker.service
```

### 📁 List Available Backups
You can list all available backup files using:
```
ls /home/ubuntu/incident-tracker-backups/db-*.sql
```
**✅ Done!**
Your database should now be restored and your app back online.
