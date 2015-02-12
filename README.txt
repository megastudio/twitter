
# Login tokens

You have to obtain login tokens and keys to be able to use this script.

The process is:
- register for Twitter
- add your mobile phone at: https://twitter.com/settings/devices
- go to https://apps.twitter.com/
- click on "Create new app"
- write somethig to the "name" and "description", it can be anything
- write anything to "website", it doesn't matter, can be https://twitter.com for example
- select the "Keys and Access Tokens" tab
- click on "Generate access token" button
- copy the data into config.py
    TW_CONSUMER_KEY <- Consumer Key (API Key)
    TW_CONSUMER_SECRET <- Consumer Secret (API Secret)
    TW_ACCESS_TOKEN <- Access Token
    TW_ACCESS_TOKEN_SECRET <- Access Token Secret


# Installation

You need to install the required Python modules by running:

```
    pip install -r requirements.txt
```


# Running the script

For streaming all tweets type:

```
    python twitter_stream.py
```

Filtering by "restaurant" keyword:

```
    python twitter_stream.py --track=restaurant
```

Filtering by multiple keywords:

```
    python twitter_stream.py --track=restaurant,bar,spa
```

Filtering by locations (San Francisco):

```
    python twitter_stream.py --locations=[-122.75,36.8,-121.75,37.8]
```

The four numbers are the bounding box of the location. More bounding box can be 
filtered, for example (San Francisco and New York City):

```
    python twitter_stream.py --locations=[-122.75,36.8,-121.75,37.8,-74,40,-73,41]
```

For details see the "locations" block [in the documentation](https://dev.twitter.com/streaming/overview/request-parameters).
