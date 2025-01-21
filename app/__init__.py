from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from .routes.auth import auth_bp as auth_blueprint
    from .routes.clients import clients_bp as clients_blueprint
    from .routes.projects import projects_bp as projects_blueprint
    from .routes.tasks import tasks_bp as tasks_blueprint
    from .routes.analytics import analytics_bp as analytics_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(clients_blueprint)
    app.register_blueprint(projects_blueprint)
    app.register_blueprint(tasks_blueprint)
    app.register_blueprint(analytics_blueprint)

    return app


