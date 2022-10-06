import flask
from app import flask_app, db
from app.forms import RegisterForm, NewCrop, SignInForm
from app.models import Users
from app import login_manager, models
import flask_login


@flask_app.route("/")
def homepage():
    return flask.render_template("homepage.html")


# @flask_app.route("/register", methods=["GET", "POST"])
# def register_page():
#     register_form = RegisterForm()
#     if register_form.validate_on_submit():
#         f_name = register_form.first_name.data
#         l_name = register_form.last_name.data
#         email_address = register_form.email_address.data
#         pwd = register_form.password.data
#         c_pwd = register_form.password.data
#         print(c_pwd)
#         # if c_pwd == c_pwd:
#         #     print("Under progress for confirm password")
#
#         # users = Users(
#         #     first_name=f_name,
#         #     last_name=l_name,
#         #     email_address=email_address,
#         #     password=pwd
#         # )
#         #
#         # db.session.add(users)
#         # db.session.commit()
#
#         print("ADDING TO DATABASE")
#
#         return flask.redirect("/")
#
#     login_form = SignInForm()
#     if login_form.validate_on_submit():
#         print("Hoorays")
#         return flask.redirect("/")
#     return flask.render_template("signin.html", register_form=register_form, login_form=login_form)


@flask_app.route("/dashboard", methods=["GET", "POST"])
def dashboard_page():
    new_crop = NewCrop()
    print("Form")
    if new_crop.validate_on_submit():
        crop_name = new_crop.crop_name.data
        sow_date = new_crop.sow_date.data
        # harvest_date = new_crop.harvest.data
        quantity = new_crop.quantity.data
        units = new_crop.units.data

        da_list = [crop_name,
                   sow_date,
                   harvest_date,
                   quantity,
                   units]
        print(da_list)
    else:
        print("Wrong outcome")

    return flask.render_template("dashboard-content.html", new_crop=new_crop)


@login_manager.user_loader
def load_user(Id):
    Id = int(Id)
    return models.Users.get(Id)


@flask_app.route("/login", methods=["GET", "POST"])
def login():

    if flask_login.current_user.is_authenticated:
        return flask.redirect("/")

    login_form = SignInForm()
    register_form = RegisterForm()

    if login_form.validate_on_submit():

        user = models.Users.query.filter_by(email_address=login_form.email.data)
        print(user)

        if user is None or not user.email == login_form.email.data:
            flask.flash('Invalid username or password')
            return flask.redirect("/")
        # print("text_3")
        flask_login.login_user(user, remember=True)
        return flask.redirect("/")
    return flask.render_template('signin.html', login_form=login_form, register_form=register_form)


@flask_app.route('/logout')
def logout():
    flask_login.logout_user()
    return flask.redirect("/")
