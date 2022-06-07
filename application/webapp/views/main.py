from flask import blueprints

main_bp = blueprints.Blueprint("main_bp", __name__)


@main_bp.route("/")
def home_view():
    return "<h1>Welcome to Geeks for Geeks</h1>"
