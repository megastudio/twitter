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
