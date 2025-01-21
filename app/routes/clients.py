from flask import Blueprint, render_template
from flask_login import login_required
from app.routes.models import Client
from app import db

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/')
@login_required
def view_clients():
    clients = Client.query.all()
    return render_template('clients/view.html', clients=clients)