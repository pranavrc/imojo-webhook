#!/usr/bin/env python

from flask import Flask, request, Response, render_template
import twitter
from twitter_keys import consumer_key, consumer_secret, oauth_token, oauth_secret

app = Flask(__name__)

@app.route('/')

def index():
    if request.method == 'GET':
        return 'OK'
    if request.method == 'POST':
        status = request.form['buyer_name'] + '(' + request.form['buyer'] + ') claimed ' + request.form['offer_title']
        twitter_post(consumer_key, consumer_secret, oauth_token, oauth_secret, status)

def twitter_post(consumer_key, consumer_secret, oauth_token, oauth_secret, post_status):
    t = twitter.Twitter(auth = twitter.OAuth(oauth_token, oauth_secret, consumer_key, consumer_secret))
    t.statuses.update(status = post_status)

if __name__ == "__main__":
    app.run(debug = True)
