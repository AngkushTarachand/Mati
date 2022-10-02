import flask
from app import flask_app, db
from app.forms import RegisterForm, NewCrop
from app.models import Users


@flask_app.route("/")
def homepage():
    return flask.render_template("homepage.html")


@flask_app.route("/register")
def register_page_2():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        f_name = register_form.first_name.data
        l_name = register_form.last_name.data
        email_address = register_form.email_address.data
        pwd = register_form.password.data
        c_pwd = register_form.password.data

        list_form = [f_name, l_name, email_address, pwd, c_pwd]

    return flask.render_template("signin.html", register_form=register_form)


@flask_app.route("/register", methods=["GET", "POST"])
def register_page():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        f_name = register_form.first_name.data
        l_name = register_form.last_name.data
        email_address = register_form.email_address.data
        pwd = register_form.password.data
        c_pwd = register_form.password.data
        # print(c_pwd)
        # if c_pwd == c_pwd:
        #     print("Under progress for confirm password")
        users = Users(
            first_name=f_name,
            last_name=l_name,
            email_address=email_address,
            password=pwd
        )

        db.session.add(users)
        db.session.commit()

        print("ADDING TO DATABASE")

        return flask.redirect("/")

    return flask.render_template("register.html", register_form=register_form)


@flask_app.route("/dashboard",  methods=["GET", "POST"])
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
