from flask import Flask, render_template, url_for, request, flash, redirect
from Functions import LoginForm, RegistrationForm, DataBase
import Data

database = DataBase()
root = Flask(__name__)
user = "Shahzeb"
root.config['SECRET_KEY'] = '0b582cabd95b82f5ec0f4061826b4c36'

@root.route("/home")
def home():
    return render_template('home.html', title="HOME", items=Data.dummy, content="Hello World", user=user)


@root.route("/about")
def about():
    return render_template('about.html', title="About", user=user)

@root.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    Returning_Value = None
    if request.method == "POST":
        if form.validate_on_submit():
            email = request.form.get("email")
            password = request.form.get("password")
            Returning_Value = database.login(email, password)
            print(Returning_Value)
            if Returning_Value == True:
                flash('Logged in Successfully', 'success')
                return redirect(url_for('home'))  
            else:
                flash('Login Failed', 'danger')
    return render_template('login.html', title="Login", form=form, user=user)

@root.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    Returning_Value = None
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if form.validate_on_submit():
            if password == confirm_password:
                Returning_Value = database.signup(first_name, last_name, username, email, password)
                if Returning_Value == True:
                    flash('Account created successfully!', 'success')
                    return redirect(url_for('home'))   
                else:
                    flash('Account Creation Unsuccessful', 'danger')
                    return redirect(url_for('signup')) 
            else:
                Returning_Value = False
                print(Returning_Value)
    print(Returning_Value)
    return render_template('signup.html', title="Signup", form=form, user=user)

if __name__ == "__main__":
    root.run(host='0.0.0.0', port=80, debug=True)