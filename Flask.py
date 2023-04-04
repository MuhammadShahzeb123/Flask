from flask import Flask, render_template
import requests
import json

root = Flask(__name__)
def get_meme():
    url = "https://meme-api.com/gimme"
    responce = json.loads(requests.request("GET", url).text)
    meme_large = responce['preview'][-2]
    subreddit = responce['subreddit']
    return subreddit, meme_large

@root.route('/')
def index():
    meme_pic, subreddit = get_meme()
    return render_template("index.html",meme_pic=meme_pic,subreddit=subreddit)

root.run(host='0.0.0.0', port=5000)