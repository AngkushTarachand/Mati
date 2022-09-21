import flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLALchemy
from app.config import Config

flask_app = flask.Flask(__name__)
# secret key for form
flask_app.config['SECRET_KEY'] = "final"

# configuration of database
flask_app.config.from_object(Config)

db = SQLALchemy(flask_app)
migrate = Migrate(flask_app, db)

from app import routes
