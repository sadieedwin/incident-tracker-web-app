## 🛠️ Systemd Service setup for the App

### Running the Flask app directly with Python
```bash
ubuntu@inci-track:~$ vi /etc/systemd/system/incident-tracker.service

[Unit]
Description=Running Flask App with systemd (Python Script Execution)
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/incident-tracker-web-app
Environment="PATH=/home/ubuntu/incident-tracker/venv/bin"
ExecStart=/home/ubuntu/incident-tracker-web-app/venv/bin/python /home/ubuntu/incident-tracker-web-app/app.py

[Install]
WantedBy=multi-user.target
```

### Enable / Start the service
```
sudo systemctl daemon-reload
sudo systemctl enable incident-tracker
sudo systemctl start incident-tracker
```

