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
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember")
        print(email, password,)
        # database.login(email, password)
    form = LoginForm()
    return render_template('login.html', title="Login", forms=form)

@root.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        remember = request.form.get("remember")
    
        database.signup(username, email, password)
    
    form = RegistrationForm()
    return render_template('signup.html', title="Signup", forms=form)

if __name__ == "__main__":
    root.run(host='0.0.0.0', port=80, debug=True)