import datetime
import json

import tweepy

from modules.log import log
from modules import database
import config


class Listener(tweepy.streaming.StreamListener):

    def on_data(self, data):
        d = json.loads(data)

        if 'text' in d:
            process_tweet(d, from_stream=True)

        return True

    def on_error(self, code):
        log("Error code: {}".format(code))

        if code == 420:
            log("Connecion failed,"
                " please wait at least 1 minute before restarting the process")
            log("For details see"
                " https://dev.twitter.com/streaming/overview/connecting")
            log("")
            return False


def process_tweet(d, from_stream):
    text = d['text']
    stamp = datetime.datetime.strptime(d['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    user_id = d['user']['id']

    log("")
    log("Tweet from user #{} at {}".format(user_id, stamp))
    log(text.encode('utf-8'))

    database.add_tweet(stamp, user_id, text, from_stream=from_stream)


def listen_to(track=None, locations=None):
    auth = connect()

    log("Initializing streaming API...")
    stream = tweepy.Stream(auth, Listener())
    stream.filter(track=track, locations=locations)


def search(track=None, locations=None):
    auth = connect()
    api = tweepy.API(auth)
    results = api.search(q="Mice")

    for result in results:
        d = result._json
        process_tweet(d, from_stream=False)


def connect():
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
