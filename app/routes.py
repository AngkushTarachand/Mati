import flask
from app import flask_app


@flask_app.route("/")
def homepage():
    return "Hackathon 2"
