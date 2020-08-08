#!/usr/bin/env python
from datetime import datetime
import os
import re
import tweepy
from flask import Flask, request, send_from_directory
from werkzeug.contrib.atom import AtomFeed
from . import settings

app = Flask(__name__)
auth = tweepy.OAuthHandler(
    settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET
)
auth.set_access_token(
    settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/home")
def home():
    retweet = (
        False
        if request.args.get("retweet", "true", type=str).lower() == "false"
        else True
    )
    replies = (
        False
        if request.args.get("replies", "true", type=str).lower() == "false"
        else True
    )
    return generate_response(
        api.me().screen_name,
        api.home_timeline(count=200, tweet_mode="extended"),
        retweet,
        replies,
    )


@app.route("/<username>", methods=["GET"])
def feed(username):
    retweet = (
        False
        if request.args.get("retweet", "true", type=str).lower() == "false"
        else True
    )
    replies = (
        False
        if request.args.get("replies", "true", type=str).lower() == "false"
        else True
    )
    return generate_response(
        username,
        api.user_timeline(username, count=200, tweet_mode="extended"),
        retweet,
        replies,
    )


def get_tweet_media_url(tweet):
    ret_val = False
    media = tweet.entities.get("media", [])
    if media:
        ret_val = media[0].get("media_url")

    return ret_val


def generate_response(username, tweets, retweet, replies):
    feed_title = "@{}".format(username)
    subtitle = "Timeline as of {date}".format(date=datetime.now())
    feed = AtomFeed(feed_title, feed_url="/", url="/", subtitle=subtitle)
    if not retweet:
        tweets = [t for t in tweets if not t.retweeted and "RT @" not in t.full_text]
    if not replies:
        tweets = [t for t in tweets if t.in_reply_to_status_id is None]

    for tweet in tweets:
        content = re.sub(r"(http\S+)", r'<a href="\1">\1</a>', tweet.full_text)
        title = re.sub(r"\s+http\S+", "", tweet.full_text)

        media = get_tweet_media_url(tweet)
        if media:
            content += '<img src="{src}" width="250" />'.format(src=media)

        feed.add(
            title=title,
            title_type="text",
            content=content,
            content_type="html",
            author=tweet.author.screen_name,
            url="https://twitter.com/{}/status/{}".format(
                tweet.author.screen_name, tweet.id
            ),
            id=tweet.id,
            published=tweet.created_at,
            updated=tweet.created_at,
        )
    return feed.get_response()
