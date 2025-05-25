# These are the issues I encountered while messing with the App lol

## 1. 📌 [May 1, 2025] - Fixed Python Not Found and 502 Bad Gateway Error

### 🛠️ Issue Summary:
- The issue happened after I messed up with the files with git merge conflicts haha
- Encountered a `502 Bad Gateway` error when trying to access the Incident Tracker web app.
- The systemd service `incident-tracker.service` failed with status `203/EXEC`.
- Also noticed that running the `python` command returned:  
  `Command 'python' not found, did you mean: ...`

### 🔍 Root Cause:
- The `python` command was missing from the system. On Ubuntu systems, `python` often points to `python3`, but in this case, the symbolic link was not present or had been removed.
- This caused the service to fail since the service file was referencing `/usr/bin/python` or another invalid path.

### ✅ Resolution Steps:
1. Installed python3 `sudo apt install python-is-python3`
2. Recreated the virtual environment `python -m venv venv`
3. Re-installed flask flask_sqlalchemy `pip install flask flask_sqlalchemy`
4. Restarted incident-tracker and verified the app is running again. :D

---

## 2. Logrotate config issue:
**Error** when running a test run of logrotate: `sudo logrotate /etc/logrotate.conf --debug`
```
error: incident_tracker:1 unexpected } (missing previous '{')
removing last 1 log configs
error: found error in file incident_tracker, skipping
```
**Before**:
```
ubuntu@inci-track:/etc/logrotate.d$ ll /var/log/incident-tracker/
total 4352
drwxr-xr-x  2 ubuntu ubuntu    4096 Apr 13 06:22 ./
drwxrwxr-x 15 root   syslog    4096 May 25 00:00 ../
-rw-r--r--  1 ubuntu ubuntu 4441630 May 25 18:39 incident_tracker.log
```

**Fix**: Added the missing '{'

Force run using: `sudo logrotate -f /etc/logrotate.d/incident_tracker`

**After**:
```
ubuntu@inci-track:/etc/logrotate.d$ sudo logrotate -f /etc/logrotate.d/incident_tracker 

ubuntu@inci-track:/etc/logrotate.d$ sudo !!
sudo grep -i incident /var/lib/logrotate/status
"/var/log/incident-tracker/incident_tracker.log" 2025-5-25-18:41:47
"/var/log/incident_tracker.log" 2025-4-14-3:0:0
 
ubuntu@inci-track:/etc/logrotate.d$ ll /var/log/incident-tracker/
total 4352
drwxr-xr-x  2 ubuntu ubuntu    4096 May 25 18:41 ./
drwxrwxr-x 15 root   syslog    4096 May 25 00:00 ../
-rw----r--  1 ubuntu ubuntu       0 May 25 18:41 incident_tracker.log
-rw-r--r--  1 ubuntu ubuntu 4442014 May 25 18:41 incident_tracker.log.1
```
