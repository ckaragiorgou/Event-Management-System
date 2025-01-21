from flask import Blueprint, render_template
from flask_login import login_required
from app.routes.models import Client, Project, Task

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/')
@login_required
def view_analytics():
    total_clients = Client.query.count()
    total_projects = Project.query.count()
    completed_projects = Project.query.filter_by(status='Completed').count()
    return render_template('analytics/view.html', total_clients=total_clients, total_projects=total_projects, completed_projects=completed_projects)