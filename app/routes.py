import flask
from app import flask_app
from app.forms import RegisterForm
from app.models import User


@flask_app.route("/")
def homepage():
    return flask.render_template("homepage.html")


@flask_app.route("/register", methods=["GET", "POST"])
def register_page():
    register_form = RegisterForm()
    if register_form.validate_on_submit():

        f_name = register_form.first_name.data
        l_name = register_form.last_name.data
        email_address = register_form.email_address.data
        pwd = register_form.password.data
        c_pwd = register_form.password.data

        user = User(
            f_name=f_name,
            l_name=l_name,
            email_address=email_address,
            password=pwd
        )

        db.session.add(user)
        db.session.commit()

        print ("ADDING TO DATABASE")

        return flask.redirect("/")

    return flask.render_template("register.html", register_form=register_form)

