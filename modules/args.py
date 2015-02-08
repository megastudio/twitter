import json
import sys

import docopt

from modules.log import log


def get_args_search(doc, version):
    args = docopt.docopt(doc, version=version)
    q = args.get('--q')
    geocode = args.get('--geocode')

    log("Parameters:")
    log("  q: {}".format(q))
    log("  geocode: {}".format(geocode))
    log("")

    return q, geocode


def get_args_stream(doc, version):
    args = docopt.docopt(doc, version=version)
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
    log("  track: {}".format(track))
    log("  locations: {}".format(locations))
    log("")

    return track, locations
