from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from application.config import DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    """
    blueprint
    """
    from application.api.views.main import api_bp
    from application.webapp.views.main import main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    return app
