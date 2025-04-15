# Progress Journal - Incident Tracker Web App

## ✅ Features

- [x] Report new incident
- [x] View incidents in table view
- [x] Card view toggle
- [x] Search incidents
- [x] Edit/Delete incidents
- [ ] User authentication
- [ ] Email notifications

---

## 🛠️ DevOps / Ops Task List – Incident Tracker Project
🔍 Monitoring & Alerts

Set up Icinga 2 to monitor:
- [x] Flask app uptime (via HTTP check)
- [x] Disk space on the VM
- [ ] System load or memory usage
- [ ] SQLite file existence or size

- [ ]Send alerts via email or Slack on critical issues

🔒 Security Hardening

- [ ] Create a dedicated Linux user for running the app
- [ ] Set up firewall rules (e.g., UFW or iptables)
- [ ] Enable automatic security updates
- [ ] Install and configure fail2ban for SSH protection

💾 Backups

- [x] Create a cron job to back up the SQLite database daily
- [ ] Store backups in a secure directory with proper permissions
- [ ]     Optionally, upload backups to Amazon S3

🐳 Containerization (Optional but valuable)

- [ ] Create a Dockerfile for the Flask app
- [ ] Use Docker Compose to manage the app and monitoring tools together

⚙️ Automation & CI/CD

- [ ] Set up a GitHub Actions workflow for automated testing/deployment
- [ ] Write a simple shell script for deploying updates to the server

📈 Logging & Rotation

- [x] Configure logrotate for application logs
- [x] Implement basic log monitoring - created a basic script (log_watcher.sh)
- [ ] Optional: Centralize logs to another server or cloud service

☁️ Cloud Infrastructure Simulation

- [ ] Launch an EC2 instance to host the project in AWS
- [ ] Use CloudWatch for metrics and alarms
- [ ] Create and attach an IAM role (for S3, CloudWatch, etc.)





## **Progress Journal - LOG**

**April 09, 2025 - Initial Setup and Basic Structure**
Goal: Start a new Flask web application for tracking incidents.

Actions:

Set up the project directory and initialized a Flask app.

Created a basic structure with app.py and templates/ for HTML files.

Implemented the main route to render a simple homepage.

Set up the SQLite database with a table for incidents (fields like title, description, priority, etc.).

**April 10, 2025 - Adding Incident Reporting Functionality**
Goal: Enable users to report incidents.

Actions:

Created a form for users to report incidents with fields: title, description, priority, systems affected, resolution, and remarks.

Implemented POST request handling for form submissions.

Displayed success/error messages based on form validation.

**April 10, 2025 - Adding Search Functionality**
Goal: Implement search feature to search incidents by title or description.

Actions:

Added a search input field in the UI for filtering incidents.

Implemented GET request handling to search the incidents by title and description.

April 11, 2025 - Improving UI and Styling
Goal: Enhance the visual presentation of the app.

Actions:

Styled the app with custom CSS for a more user-friendly experience.

Designed two views for incidents: Table view and Card view.

Allowed toggling between Table and Card views via buttons.

Ensured both views displayed relevant incident details like title, priority, systems affected, and timestamps.

**April 11, 2025 - Date Formatting and Handling Null Values**
Goal: Improve incident date display and handle null values gracefully.

Actions:

Used Jinja2 templating to format created_at and updated_at date fields.

Added checks to display "N/A" for incidents with missing date values to prevent errors in the UI.

**April 12, 2025 - Incident Management (Edit/Delete)**
Goal: Enable incident management actions like editing and deleting incidents.

Actions:

Created Edit and Delete links for each incident in both Table and Card views.

Implemented routes to handle editing and deleting incidents.

**April 12, 2025 - GitHub Repository Setup and Initial Commit**
Goal: Track project progress and share it on GitHub.

Actions:
Committed the initial project files (including app.py, templates/, and static/ directories).
Pushed the initial code to GitHub.

**April 12, 2025 - Final Testing**
Goal: Test the full functionality of the web app.

Actions:
Tested adding, editing, deleting, and searching incidents.

Verified the toggling between Table and Card views.

Confirmed that all buttons and links worked as expected.

Next Steps
Add more incidents for testing.

Enhance features: Add more fields and improve sorting functionality.

Consider adding authentication for better security and user management.


**April 12, 2025 - Log File Integration for Basic Monitoring**
- enable logging in the Flask App; updated app.py (/var/log/incident-tracker/incident-tracker.log) - new, updated, and deleted incidents will be logged.
- enabled logrotate and created a simple log-watcher script.

**Icinga setup**
- Separate VM for the icinga server(satellite)

  Log Rotation: Created /etc/logrotate.d/incident_tracker to handle log rotation for your incident tracker project.

Log Monitoring: Developed a log-watcher.sh script to monitor log files, specifically tracking events related to create, update, and delete actions.

Icinga Setup: Launched an existing Icinga server for monitoring the incident tracker infrastructure.

Monitoring Configuration: Configured Icinga to monitor system resources such as CPU, memory, and disk space

**April 14, 2025**
- Encountered a problem with delete function, after some time the incidents were being deleted.
- Fixed by modifying the del route changing from GET to POST method. Fixed the index and styling as well.
- 
