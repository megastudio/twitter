"""
Uses the great docopt command-line interface description language
See http://docopt.org/
"""

import json
import sys

import docopt

from modules.log import log


def get_args_search(doc, version):
    # read the arguments, we use 'q' and 'geocode' here
    # full list and details: http://tweepy.readthedocs.org/en/v3.2.0/api.html#API.search
    args = docopt.docopt(doc, version=version)
    q = args.get('--q')
    geocode = args.get('--geocode')

    # log it
    log("Parameters:")
    log("  q: {}".format(q))
    log("  geocode: {}".format(geocode))
    log("")

    return q, geocode


def get_args_stream(doc, version):
    # read the arguments, we use 'track' and 'locations' here
    # full list and details: https://dev.twitter.com/streaming/overview/request-parameters
    args = docopt.docopt(doc, version=version)
    track_text = args.get('--track')
    locations_text = args.get('--locations')

    # the track can be a list of terms separated by comma
    # https://dev.twitter.com/streaming/overview/request-parameters#track
    if track_text:
        track = track_text.split(',')
    else:
        track = None

    # the location is a list of longitude,latitude pairs
    # https://dev.twitter.com/streaming/overview/request-parameters#locations
    if locations_text:
        try:
            locations = json.loads(locations_text)
        except:
            log("Unable to parse locations")
            sys.exit()
    else:
        locations = None

    # log it
    log("Parameters:")
    log("  track: {}".format(track))
    log("  locations: {}".format(locations))
    log("")

    return track, locations
