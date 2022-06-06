

from application.config import DevelopmentConfig
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


db = SQLAlchemy()
migrate=Migrate()
# restserver = Api()

def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    # restserver.init_app(app)

    """
    Main view blueprint
    """
    from application.localapp.views.main import main_bp
    from application.api.views.main import api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    return app
