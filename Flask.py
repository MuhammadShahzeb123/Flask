from flask import Flask, render_template, url_for, request, flash, redirect, session
from Functions import LoginForm, RegistrationForm, DataBase, ChatInput, ChatGPT
import Data

database = DataBase()
root = Flask(__name__)
root.config['SECRET_KEY'] = '0b582cabd95b82f5ec0f4061826b4c36'
gpt = ChatGPT()


@root.route("/home")
def home():
    return render_template('home.html', title="HOME", content="Hello World", session=session, data=Data)


@root.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    Returning_Value = None
    if request.method == "POST":
        if form.validate_on_submit():
            email = request.form.get("email")
            password = request.form.get("password")
            Returning_Value = database.login(email, password)
            if Returning_Value == True:
                
                username = session['username'] = database.username_retriever(email)
                flash(f'Logged in Successfully for {username}', 'success')
                session['username'] = database.username_retriever(email)
                return redirect(url_for('home'))
            else:
                flash('Login Failed, Invalid Email or Password', 'danger')
    return render_template('login.html', title="Login", form=form, session=session)

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
        if form.validate_on_submit():
                Returning_Value = database.signup(first_name, last_name, username, email, password)
                if Returning_Value == True:
                    flash(f'Account created for {username}!', 'success')
                    session['username'] = database.username_retriever(email)
                    return redirect(url_for('home'))
                else:
                    flash('Account Creation Unsuccessful', 'danger')
                    Returning_Value = False
                    return redirect(url_for('signup'))
    return render_template('signup.html', title="Signup", form=form, session=session)


@root.route('/gpt4', methods=['GET', 'POST'])
def gpt4():
    form = ChatInput()
    if request.method == "POST":
        chat_input = request.form.get('chat_input')
        gpt.ask(chat_input)
        print(gpt.messages)
    return render_template('chatgpt.html', title="GPT-4", form=form, chat=gpt.messages, session=session)

@root.route('/', methods=['GET', 'POST'])
def default():
    return home()

@root.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect('/')

@root.route('/code4', methods=["GET", "POST"])
def code4():
    return "<h1>Under Contruction</h1>"

@root.route('/me', methods=['GET', 'POST'])
def me():
    return render_template('me.html', title="My Account", session=session)

if __name__ == "__main__":
    root.run(host='0.0.0.0', port=80, debug=True)