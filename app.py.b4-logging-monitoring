from flask_migrate import Migrate
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Set up SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'incidents.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Incident model with created_at and updated_at timestamps
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), nullable=True)
    systems_affected = db.Column(db.String(200), nullable=True)
    resolution = db.Column(db.Text, nullable=True)
    remarks = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = None
    sort_order = request.args.get('sort_order', 'desc')  # Default to descending
    search_query = request.args.get('search', '')  # Get search term
    view = request.args.get('view', 'table')  # Default to table view

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority')
        systems_affected = request.form.get('systems_affected')
        resolution = request.form.get('resolution')
        remarks = request.form.get('remarks')

        if not title or not description:
            error_message = 'Title and Description are required.'
        else:
            incident = Incident(
                title=title,
                description=description,
                priority=priority,
                systems_affected=systems_affected,
                resolution=resolution,
                remarks=remarks
            )
            db.session.add(incident)
            db.session.commit()
            return redirect(url_for('index'))

    # Build query with search
    query = Incident.query
    if search_query:
        query = query.filter(
            db.or_(
                Incident.title.ilike(f'%{search_query}%'),
                Incident.description.ilike(f'%{search_query}%')
            )
        )

    # Apply sorting
    if sort_order == 'asc':
        incidents = query.order_by(Incident.created_at.asc()).all()
    else:
        incidents = query.order_by(Incident.created_at.desc()).all()

    return render_template(
        'index.html',
        incidents=incidents,
        error_message=error_message,
        sort_order=sort_order,
        search_query=search_query,
        view=view  # Pass view type (table or card)
    )


    # Display the form and the incident history
# duplicat from the above #    return render_template('index.html', incidents=incidents, error_message=error_message, sort_order=sort_order)


@app.route('/edit/<int:incident_id>', methods=['GET', 'POST'])
def edit_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    if request.method == 'POST':
        incident.title = request.form['title']
        incident.description = request.form['description']
        incident.priority = request.form['priority']
        incident.systems_affected = request.form['systems_affected']
        incident.resolution = request.form['resolution']
        incident.remarks = request.form['remarks']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', incident=incident)

@app.route('/delete/<int:incident_id>', methods=['GET'])
def delete_incident(incident_id):
    incident = Incident.query.get_or_404(incident_id)
    db.session.delete(incident)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)

