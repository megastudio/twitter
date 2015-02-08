"""Twitter search

Usage:
  twitter_search.py [--q=<q>] [--geocode=<g>]
  twitter_search.py (-h | --help)
  twitter_search.py --version

Options:
  -h --help      Show this screen
  --version      Show version
  --q=<q>        The query
                 For example: --q=bar
                 Multiple search terms: --q="bar restaurant"
                 For details see https://dev.twitter.com/rest/public/search
                   the "Query operators" block
  --geocode=<g>  The locations to be filtered
                 For example: --geocode=37.781157,-122.398720,1mi
                 For details see https://dev.twitter.com/rest/reference/get/search/tweets
                   the "Parameters / geocode" block
"""

from modules.args import get_args_search
from modules.twitter import search


q, geocode = get_args_search(__doc__, "Twitter search 0.1")
search(q, geocode)
