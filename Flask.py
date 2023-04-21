from flask import Flask, render_template
import requests
import json


root = Flask(__name__)
def get_meme():
    url = "https://meme-api.com/gimme"
    responce = json.loads(requests.request("GET", url).text)
    subreddit = responce['url']
    return subreddit

@root.route("/")
def index():
    return "Hello, World!"

@root.route('/memes')
def memes():
    subreddit = get_meme()
    return render_template("index.html",subreddit=subreddit)

root.run(host='0.0.0.0', port=443, debug=True)