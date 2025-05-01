## 🚀 Deploy Flask App with Gunicorn, Nginx, and systemd

This guide walks through deploying the **Incident Tracker** Flask app in a production-grade setup using **Gunicorn** (WSGI server), **Nginx** (reverse proxy), and **systemd** (service manager).

---

### 🧰 1. Prerequisites

- Your Flask app is in: `/home/ubuntu/incident-tracker-web-app`
- You have a virtual environment with dependencies installed
- You’re on an Ubuntu server (adjust paths accordingly if not)

---

### 📦 2. Install Gunicorn and Nginx

```bash
sudo apt update
sudo apt install gunicorn nginx -y
```
Inside your virtual environment:
```bash
cd ~/incident-tracker-web-app
source venv/bin/activate
pip install gunicorn
```

### 🧪 3. Test Gunicorn (optional)
Run your app using Gunicorn:
```bash
cd ~/incident-tracker-web-app
gunicorn --bind 127.0.0.1:8000 app:app
```
If this works (check in the browser at `http://<your-server-ip>:8000`), proceed to the next step.

### ⚙️ 4. Create systemd service
```bash
sudo nano /etc/systemd/system/incident-tracker.service
```
Paste this configuration:
```ini
[Unit]
Description=Gunicorn instance to serve Incident Tracker Flask App
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/incident-tracker-web-app
Environment="PATH=/home/ubuntu/incident-tracker-web-app/venv/bin"
ExecStart=/home/ubuntu/incident-tracker-web-app/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```
Save and exit.

Then enable and start the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable incident-tracker
sudo systemctl start incident-tracker
```
Check status:

```bash
sudo systemctl status incident-tracker
```

### 🌐 5. Configure Nginx as reverse proxy
```bash
sudo nano /etc/nginx/sites-available/incident-tracker
```
Paste this:
```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Enable the config:
```bash
sudo ln -s /etc/nginx/sites-available/incident-tracker /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### ✅ 6. Access the App
Now visit:
`http://<your-server-ip>`

### 🧼 7. (Optional) Remove default site
```bash
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl reload nginx
```
### 🧠 Notes
- For HTTPS, use Let's Encrypt with certbot.
- Make sure your Flask app.py exposes app (not using if __name__ == "__main__" to run).

