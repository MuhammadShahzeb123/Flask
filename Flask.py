from flask import Flask, render_template
import requests
import json



root = Flask(__name__)
def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    return response['url']

Data = [
    {
        "name": "Shahzeb",
        "class": "Metric",
        "Marks": "475",
        "link": "https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035206",
        "pic":"https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200131.jpg"
    },
        {
        "name": "Zaryab",
        "class": "Metric",
        "Marks": "475",
        "link": "https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035198",
        "pic":"https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200119.jpg"
    },
    {
        "name": "Sulemaan",
        "class": "9th Class",
        "Marks": "471",
        "link": "https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-ssc1.php?rollNo=9035194",
        "pic":"https://portal.fbise.edu.pk/fbise-conduct/std-img/img-ssc1/281200123.jpg"
    }
]

div_style = """
justify-content: center;
background-color: #000;
color: #fff;
transform: translate(0, 0);
transition: transform 0.5s ease-in-out;
onmouseover="this.style.transform = 'translate(50px, 20px)'";
display: flex;
"""


@root.route("/")
def index():
    return '<h1 style="margin-left: 123px;">Hello, World!</h1>'


@root.route("/Home")
def Home():
    return render_template('home.html', items=Data, style=div_style)


@root.route("/base")
def base():
    return render_template('base.html')


@root.route('/memes')
def memes():
    subreddit = get_meme()
    return render_template("memes.html",subreddit=subreddit)



root.run(host='0.0.0.0', port=443, debug=True)