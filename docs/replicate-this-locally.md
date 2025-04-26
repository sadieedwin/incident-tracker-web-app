## How to Run Incident Tracker Locally
1. **Install Python** (if not yet installed)
```text
Download from python.org and install it.
Make sure python and pip commands work in your terminal/cmd.
```

2. **Create a project folder**
```
mkdir incident-tracker-local
cd incident-tracker-local
```
3. **Set up a virtual environment** (good practice!)
```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
4. **Install Flask and SQLAlchemy, migrate**
```
pip install flask flask_sqlalchemy flask_migrate
```

5. **Add your project files**
Copy your app.py, templates/(index/edit/create), and static/style.css folder/files into the main folder.

6. **Run the Flask app**
```
flask run
```
7. **Access your app**
Open your browser and visit:
**http://127.0.0.1:5000**

✅ No EC2 needed.

✅ No complicated setup.

✅ Everything runs on your own laptop.

---
### Run the app in the background (Different app, but same concept)

**Sample flask_run.bat** (to run this in the background terminal)
```bat
@echo off
REM Activate virtual environment
call venv\Scripts\activate

REM Run Flask app in a new command window
start cmd /k "flask run --host=0.0.0.0 --port=5000"
```
**How to use:**
- Save that as flask_run.bat in the root of your project folder (same level as your venv folder).
- Double-click the file to run your app in a new terminal window.
- Done!

_If you'd prefer to run it silently in the background, you can use Windows Task Scheduler or a PowerShell script with Start-Process. Here's a cleaner way using PowerShell:_
**flask_background.ps1**
```powershell
# Navigate to project directory
cd "C:\Users\User.Name\Desktop\URL Repo"

# Activate virtual environment
& "venv\Scripts\Activate.ps1"

# Run Flask app in background (hidden window)
Start-Process -WindowStyle Hidden powershell -ArgumentList "flask run --host=0.0.0.0 --port=5000"
```

**How to use:**
- Save it as flask_background.ps1.
- Right-click > "Run with PowerShell" (or run from PowerShell manually).

If you see execution policy errors, run:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Shortcut:**
- Create a shortcut, in the location box, paste this: (change the user.name)
```
powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File "C:\Users\User.Name\Desktop\URL Repo\flask_background.ps1"
