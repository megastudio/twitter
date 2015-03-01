"""
Calling Twitter API with the help of tweepy
"""

import datetime
import json

import tweepy

from modules.log import log
from modules import database
import config


class Listener(tweepy.streaming.StreamListener):
    """
    The listener for getting notification about new tweets
    """

    def on_data(self, data):
        """
        Called by Twitter when a new tweet is created
        """
        d = json.loads(data)

        if 'text' in d:
            process_tweet(d, from_stream=True)

        return True

    def on_error(self, code):
        """
        Called by tweepy when an error happened
        420 is a special error code, see the details below
        """
        log("Error code: {}".format(code))

        if code == 420:
            log("Connecion failed,"
                " please wait at least 1 minute before restarting the process")
            log("For details see"
                " https://dev.twitter.com/streaming/overview/connecting")
            log("")
            return False


def process_tweet(d, from_stream):
    """
    General function to process the dictionary returned by both the search and the stream API
    """
    tweet_id = d['id']
    text = d['text']
    stamp = datetime.datetime.strptime(d['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    user_id = d['user']['id']

    log("")
    log("Tweet from user #{} at {}".format(user_id, stamp))
    log(text.encode('utf-8'))

    database.add_tweet(stamp, tweet_id, user_id, text, from_stream=from_stream)


def listen_to(track=None, locations=None):
    """
    Connects to Twitter API and starts the streaming listener with the given params
    Runs continuously while user presses Ctrl+C or Ctrl+Z
    """
    auth = connect()

    log("Initializing streaming API...")
    stream = tweepy.Stream(auth, Listener())
    stream.filter(track=track, locations=locations)


def search(q=None, geocode=None):
    """
    Connects to Twitter API and searches by using the parameters
    Gets the results, saves to database, and quits
    """
    auth = connect()
    api = tweepy.API(auth)
    results = api.search(q=q, geocode=geocode)

    for result in results:
        d = result._json
        process_tweet(d, from_stream=False)


def connect():
    """
    Connects to Twitter services by using the tokens and keys
    """
    log("Connecting to Twitter...")
    auth = tweepy.OAuthHandler(
        config.TW_CONSUMER_KEY,
        config.TW_CONSUMER_SECRET
        )
    auth.set_access_token(
        config.TW_ACCESS_TOKEN,
        config.TW_ACCESS_TOKEN_SECRET
        )
    return auth
