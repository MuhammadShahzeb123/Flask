from flask import Flask, render_template, request
import Data


root = Flask(__name__)




@root.route("/Home")
def Home():
    items = Data.Main()
    return render_template('home.html', title="HOME", items = items.Result_data())

@root.route("/Ai")
def ai():
    return render_template('ChatGPT.html', title="ChatGPT")

@root.route('/submit_text', methods=['POST'])
def submit_text():
    user_input = request.form['user_input']
    return f"<h2>{user_input}</h2>"

@root.route("/About")
def about():
    return render_template('about.html', title="About")

@root.route("/Code")
def code():
    return render_template('code.html', title="Code it")

@root.route('/Memes')
def memes():
    subreddit = Data.Main.get_meme()
    return render_template("memes.html",subreddit=subreddit, title="Memes - Stay Happy")

root.run(host='0.0.0.0', port=80, debug=True)