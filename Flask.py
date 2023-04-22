from flask import Flask, render_template
import Data


root = Flask(__name__)


@root.route("/Home")
def Home():
    return render_template('home.html', title="Home")

@root.route("/ai")
def ai():
    pass

@root.route('/memes')
def memes():
    subreddit = Data.Main.get_meme()
    return render_template("memes.html",subreddit=subreddit)

root.run(host='0.0.0.0', port=80, debug=True)