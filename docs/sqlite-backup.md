## 🗃️ SQLite Database Backup via Cron

To automate **daily backups** of the SQLite database (`incidents.db`), I created a cron job:
```bash
0 2 * * * /usr/bin/sqlite3 /home/ubuntu/incident-tracker-web-app/incidents.db .dump > /home/ubuntu/incident-tracker-backups/db-$(date +\%F).sql && find /home/ubuntu/incident-tracker-backups -name "db-*.sql" -type f -mtime +7 -delete
```

- **Runs daily at 2:00 AM**
- **Backs up the entire DB** into a timestamped SQL dump
- **Destination:** `/home/ubuntu/backups/`
- **Deletes backups** older than 7 days to save space
- **Note:** Created the directory manually to avoid `No such file or directory` error.


### Example:
```bash
ubuntu@inci-track:~/incident-tracker-backups$ pwd
/home/ubuntu/incident-tracker-backups
ubuntu@inci-track:~/incident-tracker-backups$ ls -l
total 20
-rw-rw-r-- 1 ubuntu ubuntu 18427 May  1 13:10 db-2025-05-01.sql
```

### 📖 Explanation:
| Part | Description |
|------|-------------|
| `0 2 * * *` | Run the command **every day at 2:00 AM** |
| `/usr/bin/sqlite3` | The SQLite command-line tool |
| `/home/ubuntu/incident-tracker-web-app/incidents.db` | Path to database file |
| `.dump` | Exports the entire database in SQL format |
| `> /home/ubuntu/incident-tracker-backups/db-$(date +%F).sql` | Saves the output to a file named with the current date (e.g. `db-2025-05-01.sql`) |
| `&&` | Run the next command **only if the backup was successful** |
| `find /home/ubuntu/incident-tracker-backups` | Search in the backup directory |
| `-name "db-*.sql"` | Look for files matching the backup filename pattern |
| `-type f` | Only match files (not directories) |
| `-mtime +7` | Only match files **older than 7 days** |
| `-delete` | Permanently delete those matched files |

---

### Checked backup and it is running:
```
ubuntu@inci-track:~$ date
Mon May 26 17:35:44 UTC 2025
ubuntu@inci-track:~$
ubuntu@inci-track:~$ ls -ltr incident-tracker-backups/
total 180
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 18 02:00 db-2025-05-18.sql                                                                                             -rw-rw-r-- 1 ubuntu ubuntu 18752 May 19 02:00 db-2025-05-19.sql
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 20 02:00 db-2025-05-20.sql
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 21 02:00 db-2025-05-21.sql
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 22 02:00 db-2025-05-22.sql                                                                                             -rw-rw-r-- 1 ubuntu ubuntu 18752 May 23 02:00 db-2025-05-23.sql
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 24 02:00 db-2025-05-24.sql
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 25 02:00 db-2025-05-25.sql
-rw-rw-r-- 1 ubuntu ubuntu 18752 May 26 02:00 db-2025-05-26.sql
```
