from flask import Flask, render_template
import Data


root = Flask(__name__)


@root.route("/Home")
def Home():
    return render_template('home.html', title="Home", items = [{'name':'Shahzeb', 'link':'https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035206', 'marks': "475", 'class': 'Metric', 'pic': 'https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200131.jpg'}])

@root.route("/Ai")
def ai():
    return render_template('ChatGPT.html', title="Ai")

@root.route("/About")
def about():
    return render_template('about.html', title="About")

@root.route("/Code")
def code():
    return render_template('code.html', title="Code")

@root.route('/Memes')
def memes():
    subreddit = Data.Main.get_meme()
    return render_template("memes.html",subreddit=subreddit, title="Memes")

root.run(host='0.0.0.0', port=80, debug=True)