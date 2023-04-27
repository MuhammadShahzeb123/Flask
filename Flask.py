from flask import Flask, render_template, url_for, request
from Functions import LoginForm, RegistrationForm, DataBase
import Data

database = DataBase()
root = Flask(__name__)

root.config['SECRET_KEY'] = '0b582cabd95b82f5ec0f4061826b4c36'

@root.route("/home")
def home():
    return render_template('home.html', title="HOME", items=Data.dummy, content="Hello World")


@root.route("/about")
def about():
    return render_template('about.html', title="About")

@root.route("/login", methods=["GET", "POST"])
def login():
    Returning_Value = None
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        Returning_Value = database.login(email, password)
        print(Returning_Value)

    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

@root.route("/signup", methods=["GET", "POST"])
def signup():
    Returning_Value = None
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if password == confirm_password:
            Returning_Value = database.signup(username, email, password)
        else:
            Returning_Value = False
    form = RegistrationForm()
    if request.method == "POST":
        print(Returning_Value)
        print(form.username.errors)
        print(form.email.errors)
        print(form.password.errors)
        print(form.confirm_password.errors)
    return render_template('signup.html', title="Signup", form=form)

if __name__ == "__main__":
    root.run(host='0.0.0.0', port=80, debug=True)