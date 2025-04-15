# Progress Journal - Incident Tracker Web App

## ✅ Features

- [x] Report new incident
- [x] View incidents in table view
- [x] Card view toggle
- [x] Search incidents
- [x] Edit/Delete incidents
- [ ] User authentication
- [ ] Email notifications
- [x] Pagination

---

## 🛠️ DevOps / Ops Task List – Incident Tracker Project
🔍 Monitoring & Alerts

Set up Icinga 2 to monitor:
- [x] Flask app uptime (via HTTP check)
- [x] Disk space on the VM
- [ ] System load or memory usage
- [ ] SQLite file existence or size

- [ ] Send alerts via email or Slack on critical issues

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

---

## **Progress Journal - LOG**

## 🗓️ April 09, 2025 - Initial Setup and Basic Structure

**🎯 Goal:** Start a new Flask web application for tracking incidents.

**✅ Actions:**
- Set up the project directory and initialized a Flask app.
- Created a basic structure with `app.py` and `templates/` for HTML files.
- Implemented the main route to render a simple homepage.
- Set up the SQLite database with a table for incidents (fields like title, description, priority, etc.).

---

## 🗓️ April 10, 2025 - Adding Incident Reporting Functionality

**🎯 Goal:** Enable users to report incidents.

**✅ Actions:**
- Created a form for users to report incidents with fields: title, description, priority, systems affected, resolution, and remarks.
- Implemented POST request handling for form submissions.
- Displayed success/error messages based on form validation.

---

### Adding Search Functionality

**🎯 Goal:** Implement search feature to search incidents by title or description.

**✅ Actions:**
- Added a search input field in the UI for filtering incidents.
- Implemented GET request handling to search the incidents by title and description.

---

## 🗓️ April 11, 2025 - Improving UI and Styling

**🎯 Goal:** Enhance the visual presentation of the app.

**✅ Actions:**
- Styled the app with custom CSS for a more user-friendly experience.
- Designed two views for incidents: Table view and Card view.
- Allowed toggling between Table and Card views via buttons.
- Ensured both views displayed relevant incident details like title, priority, systems affected, and timestamps.

---

### Date Formatting and Handling Null Values

**🎯 Goal:** Improve incident date display and handle null values gracefully.

**✅ Actions:**
- Used Jinja2 templating to format `created_at` and `updated_at` date fields.
- Added checks to display "N/A" for incidents with missing date values to prevent errors in the UI.

---

## 🗓️ April 12, 2025 - Incident Management (Edit/Delete)

**🎯 Goal:** Enable incident management actions like editing and deleting incidents.

**✅ Actions:**
- Created Edit and Delete links for each incident in both Table and Card views.
- Implemented routes to handle editing and deleting incidents.

---

###  GitHub Repository Setup and Initial Commit

**🎯 Goal:** Track project progress and share it on GitHub.

**✅ Actions:**
- Committed the initial project files (`app.py`, `templates/`, and `static/` directories).
- Pushed the initial code to GitHub.

---

###  Testing

**🎯 Goal:** Test the full functionality of the web app.

**✅ Actions:**
- Tested adding, editing, deleting, and searching incidents.
- Verified the toggling between Table and Card views.
- Confirmed that all buttons and links worked as expected.

**📝 Next Steps:**
- Add more incidents for testing.
- Enhance features: Add more fields and improve sorting functionality.
- Consider adding authentication for better security and user management.

---

### Log File Integration for Basic Monitoring

**🎯 Goal:** Enable basic logging and monitoring for the incident tracker app.

**✅ Actions:**
- Enabled logging in the Flask App; updated `app.py` to log create, update, and delete events to `/var/log/incident-tracker/incident-tracker.log`.
- Set up log rotation: Created `/etc/logrotate.d/incident_tracker` to handle log rotation.
- Developed a `log-watcher.sh` script to monitor log files for important events.

---

### 🧪 Icinga Monitoring Setup

**🎯 Goal:** Monitor the infrastructure using Icinga.

**✅ Actions:**
- Used an existing VM as the Icinga monitoring server.
- Configured log monitoring and system resource checks (CPU, memory, disk space).
- Connected the Icinga server to monitor the incident tracker project’s EC2 instance.

---

## 🗓️ April 14, 2025 - Bug Fixes and Improvements

**🎯 Goal:** Fix issues and refine behavior of the delete functionality.

**✅ Actions:**
- Encountered an issue where incidents weren’t deleting properly.
- Fixed by changing the Delete route to use `POST` method instead of `GET`.
- Made adjustments to index handling and improved styling.


## ✅ April 15 Progress Update

### 🔧 Changes Made
- **Renamed `remarks` column to `root_cause`** in the database model to better reflect the field's purpose.
- **Updated all related templates and forms** to use `root_cause` instead of `remarks`.
- **Modified the edit incident route** in `app.py` to handle the new `root_cause` field.

### 🐛 Issue Encountered
- Got a `BadRequestKeyError: 'root_cause'` during incident editing.
  - Cause: The form was missing the `name="root_cause"` input field, leading to a KeyError when trying to access it via `request.form`.

### ✅ Resolution
- Added the missing form field in the incident edit template.
- Retested: edit functionality now works correctly with the new `root_cause` field.

### 🧠 Lessons Learned
- Always double-check that your form inputs match the field names you're accessing in `request.form`.
- When renaming a column in your model, make sure to update:
  - Database schema
  - HTML templates
  - Flask routes and logic

 ## 📅 April 15, 2025 - Modification
  - Reorganized and simplified the app to focus on a single table view for clarity and ease of use.
  - Added pagination

