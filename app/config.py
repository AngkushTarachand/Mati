import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///" + os.path.join(basedir, 'app.db')
