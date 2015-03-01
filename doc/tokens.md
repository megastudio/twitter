### Login tokens

You have to obtain login tokens and keys to be able to use this script.

The process is:
- register for Twitter
- add your mobile phone at: https://twitter.com/settings/devices
- go to https://apps.twitter.com/
- click on "Create new app"
- write somethig to the "name" and "description", it can be anything
- write anything to "website", it doesn't matter, can be https://twitter.com for example
- select the "Keys and Access Tokens" tab
- click on "Create my access token" button
- create a file called `config.py` next to the `twitter_stream.py` file:

```
TW_CONSUMER_KEY = '<Consumer Key (API Key)>'
TW_CONSUMER_SECRET = '<Consumer Secret (API Secret)>'
TW_ACCESS_TOKEN = '<Access Token>'
TW_ACCESS_TOKEN_SECRET = '<Access Token Secret>'
```