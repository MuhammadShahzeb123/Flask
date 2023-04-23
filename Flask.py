from flask import Flask, render_template, url_for
from Functions import LoginForm, RegistrationForm
import Data

root = Flask(__name__)

root.config['SECRET_KEY'] = '0b582cabd95b82f5ec0f4061826b4c36'

@root.route("/Home")
def Home():
    return render_template('home.html', title="HOME", items=Data.dummy, content="Hello World")


@root.route("/About")
def about():
    return render_template('about.html', title="About")

@root.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", forms=form)

@root.route("/signup")
def signup():
    form = RegistrationForm()
    return render_template('signup.html', title="Signup", forms=form)

root.run(host='0.0.0.0', port=80, debug=True)