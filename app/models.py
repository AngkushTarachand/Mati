from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email_address = db.Column(db.String)
    password = db.Column(db.String)
    # crops = db.relationship('Crop', secondary=user_crop_table, back_populates='crops_users_table')


class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sow_date = db.Column(db.Date)
    harvest = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    units = db.Column(db.String)
    # users = db.relationship('User', secondary=user_crop_table, back_populates='crops_users_table')


# crops_users_table = db.Table(
#     'crops',id
#     db.Column('user_id', db.Integer, db.ForeignKey('user_id')),
#     db.Column('crop-id', db.Integer, db.ForeignKey('dog.id'))
# )
