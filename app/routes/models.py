from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default='consultant')
    def __repr__(self):
        return f'<User {self.username}>'

    def check_password(self, password):
        return self.password == password

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    contact_details = db.Column(db.String(128), nullable=False)
    company_size = db.Column(db.String(64))
    industry = db.Column(db.String(64))

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='Pending')
    deadline = db.Column(db.Date)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    title = db.Column(db.String(64), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    priority = db.Column(db.String(20), default='Medium')
    deadline = db.Column(db.Date)
