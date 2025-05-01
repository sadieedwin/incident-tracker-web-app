# These are the issues I encountered while messing with the App lol

## 📌 [May 1, 2025] - Fixed Python Not Found and 502 Bad Gateway Error

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


