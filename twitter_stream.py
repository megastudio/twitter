"""Twitter stream listener

Usage:
  twitter_stream.py [--track=<tr>] [--locations=<ls>]
  twitter_stream.py (-h | --help)
  twitter_stream.py --version

Options:
  -h --help         Show this screen
  --version         Show version
  --track=<tr>      The keyword to be filtered, for example: --track=bar,restaurant
  --locations=<ls>  The locations to be filtered, for example: --locations=[-122.75,36.8,-121.75,37.8]

"""

import datetime
import json
import sys

import docopt
import tweepy

import config


LOG_PATH = 'twitter_stream.log'


class Listener(tweepy.streaming.StreamListener):

    def on_data(self, data):
        d = json.loads(data)

        text = d['text']
        stamp = datetime.datetime.fromtimestamp(int(d['timestamp_ms']) / 1000)
        user_id = d['user']['id']

        log("")
        log("Tweet from user #{} at {}".format(user_id, stamp))
        log(text.encode('utf-8'))

        return True

    def on_error(self, code):
        log("Error code: {}".format(code))

        if code == 420:
            log("Connecion failed, please wait at least 1 minute before restarting the process")
            log("For details see https://dev.twitter.com/streaming/overview/connecting")
            log("")
            return False


def get_args():
    args = docopt.docopt(__doc__, version='Twitter stream listener 0.1')
    track_text = args.get('--track')
    locations_text = args.get('--locations')

    if track_text:
        track = track_text.split(',')
    else:
        track = None

    if locations_text:
        try:
            locations = json.loads(locations_text)
        except:
            log("Unable to parse locations")
            sys.exit()
    else:
        locations = None

    log("Parameters:")
    log(" track: {}".format(track))
    log(" locations: {}".format(locations))
    log("")

    return track, locations


def listen_to(track=None, locations=None):
    log("Connecting to Twitter...")
    auth = tweepy.OAuthHandler(config.TW_CONSUMER_KEY, config.TW_CONSUMER_SECRET)
    auth.set_access_token(config.TW_ACCESS_TOKEN, config.TW_ACCESS_TOKEN_SECRET)

    log("Initializing streaming API...")
    stream = tweepy.Stream(auth, Listener())
    stream.filter(track=track, locations=locations)


def log(text):
    print text

    now = datetime.datetime.now()
    with open(LOG_PATH, 'a') as f:
        f.write('{} - {}\n'.format(now, text))


track, locations = get_args()
listen_to(track, locations)
