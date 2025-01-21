from flask import Blueprint, render_template
from flask_login import login_required
from app.routes.models import Task
from app import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
@login_required
def view_tasks():
    tasks = Task.query.all()
    return render_template('tasks/view.html', tasks=tasks)
