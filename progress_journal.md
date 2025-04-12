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

## 🚧 In Progress
- Adding realistic incident data
- Testing full feature flow

---

## 📈 Next Steps
- Enhance sorting functionality
- Add user authentication
- Implement email notifications for updates

**Progress Journal - Incident Tracker Web App**

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

Created a GitHub repository for the project.

Added an initial README.md file to the repository.

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
