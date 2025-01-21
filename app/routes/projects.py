from flask import Blueprint, render_template
from flask_login import login_required
from app.routes.models import Project
from app import db

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/')
@login_required
def view_projects():
    projects = Project.query.all()
    return render_template('projects/view.html', projects=projects)