import flask
from app import flask_app


@flask_app.route("/")
def homepage():
    return flask.render_template("homepage.html")
