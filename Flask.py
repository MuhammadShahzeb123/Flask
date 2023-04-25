from flask import Flask, render_template, url_for
import Functions


root = Flask(__name__)

@root.route("/Home")
def Home():
    return render_template('home.html', title="HOME", items=Functions.dummy, content="Hello World")


@root.route("/Layout")
def Layout():
    return render_template('layout.html', title="Layout", items=Functions.dummy)

@root.route("/About")
def about():
    return render_template('about.html', title="About")

@root.route("/login")
def login():
    form = Functions.RegistrationAndLogin()

@root.route("/signup")
def signup():
    return "<h1>Under Progress</h1><div style='font-weight: bold; font-size: 20px; color: red'><a href='/Home'>Go Home</a></div>"


root.run(host='0.0.0.0', port=80, debug=True)