from app import db
import flask_login


# , flask_login.UserMixin
class Users(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String,
                           nullable=False
                           )
    last_name = db.Column(db.String,
                          nullable=False)
    email_address = db.Column(db.String,
                              unique=True,
                              nullable=False)
    password = db.Column(db.String,
                         nullable=False)
    # crops = db.relationship('Crop', secondary=user_crop_table, back_populates='crops_users_table')

    # def get_id(self):
    #     return self.id


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sow_date = db.Column(db.Date)
    # harvest = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    units = db.Column(db.String)
    # users = db.relationship('User', secondary=user_crop_table, back_populates='crops_users_table')

# crops_users_table = db.Table(
#     'crops', id,
#     db.Column('user_id', db.Integer, db.ForeignKey('Users.id')),
#     db.Column('crop-id', db.Integer, db.ForeignKey('Crop.id'))
# )
