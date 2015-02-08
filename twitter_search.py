"""Twitter search

Usage:
  twitter_search.py [--track=<tr>] [--locations=<ls>]
  twitter_search.py (-h | --help)
  twitter_search.py --version

Options:
  -h --help         Show this screen
  --version         Show version
  --track=<tr>      The keyword to be filtered
                    For example: --track=bar,restaurant
  --locations=<ls>  The locations to be filtered
                    For example: --locations=[-122.75,36.8,-121.75,37.8]
"""

from modules.args import get_args
from modules.twitter import search


track, locations = get_args(__doc__, "Twitter search 0.1")
search(track, locations)
