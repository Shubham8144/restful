from os import environ


class DevelopmentConfig:
    TESTING = True
    DEBUG = True
    FLASK_ENV = "development"
    SECRET_KEY = environ.get("SECRET_KEY")

    # database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")


class ProductionConfig:
    TESTING = False
    DEBUG = False
    FLASK_ENV = "production"
    SECRET_KEY = environ.get("SECRET_KEY")

    # database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
