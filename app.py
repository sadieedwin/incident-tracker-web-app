from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import or_
from datetime import datetime
import os
import logging

app = Flask(__name__)

# Logging
logging.basicConfig(
    filename='/var/log/incident-tracker/incident_tracker.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)

# SQLite configuration
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'incidents.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Incident model
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), nullable=True)
    systems_affected = db.Column(db.String(200), nullable=True)
    resolution = db.Column(db.Text, nullable=True)
    root_cause = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    sort_order = request.args.get('sort_order', 'desc')
    search_query = request.args.get('search', '')
    per_page = request.args.get('per_page', 5, type=int)
    page = request.args.get('page', 1, type=int)

    if request.method == 'POST':
        # You can handle new incident form here if needed
        return redirect(url_for('index'))

    # Query building
    query = Incident.query
    if search_query:
        query = query.filter(
            or_(
                Incident.title.ilike(f'%{search_query}%'),
                Incident.description.ilike(f'%{search_query}%')
            )
        )

    if sort_order == 'asc':
        query = query.order_by(Incident.created_at.asc())
    else:
        query = query.order_by(Incident.created_at.desc())

    incidents = query.paginate(page=page, per_page=per_page, error_out=False)

    # Total number of incidents
    total_incidents = Incident.query.count()

    return render_template(
        'index.html',
        incidents=incidents.items,
        pagination=incidents,
        error_message=error_message,
        sort_order=sort_order,
        search_query=search_query,
        per_page=per_page,
        total_incidents=total_incidents
    )


@app.route('/create', methods=['GET', 'POST'])
def create_incident():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        systems_affected = request.form['systems_affected']
        resolution = request.form['resolution']
        root_cause = request.form['root_cause']

        new_incident = Incident(
            title=title,
            description=description,
            priority=priority,
            systems_affected=systems_affected,
            resolution=resolution,
            root_cause=root_cause
        )

        db.session.add(new_incident)
        db.session.commit()
        app.logger.info(f"Incident created: Title='{title}', Priority={priority}")

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/edit/<int:incident_id>', methods=['GET', 'POST'])
def edit_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    if request.method == 'POST':
        incident.title = request.form['title']
        incident.description = request.form['description']
        incident.priority = request.form['priority']
        incident.systems_affected = request.form['systems_affected']
        incident.resolution = request.form['resolution']
        incident.root_cause = request.form['root_cause']
        db.session.commit()
        app.logger.info(f"Incident updated: ID={incident.id}, Title='{incident.title}', Priority={incident.priority}")
        return redirect(url_for('index'))

    return render_template('edit.html', incident=incident)

@app.route('/delete/<int:incident_id>', methods=['POST'])
def delete_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    app.logger.info(f"Incident deleted: ID={incident.id}, Title='{incident.title}'")
    db.session.delete(incident)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

