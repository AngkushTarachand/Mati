import flask_wtf
import wtforms

# Sign up for the first time ~ Register


class RegisterForm(flask_wtf.FlaskForm):

    first_name = wtforms.StringField("First Name")
    last_name = wtforms.StringField("Last Name")
    email_address = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    confirm_password = wtforms.PasswordField("Confirm Password")

    submit = wtforms.SubmitField("Submit")

# Sign in ~ User


class SignUpForm(flask_wtf.FlaskForm):

    email = wtforms.StringField("email")
    password = wtforms.StringField("Password")
    submit = wtforms.SubmitField("Sign in")


