"""
Uses SQLAlchemy to save the tweets into an SQLite database

There is only one table, called 'tweets'. The fields:
- id: primary key
- stamp: the publishing timestamp of the tweet
- tweet_id: the ID of the tweet in Twitter's database
- user_id: the ID of the user, the name can change, the ID is not
- text: the tweet text
- from_stream: True if we got it from calling the stream API
               False if we got it from search API
"""

import os

from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, DateTime, Index, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy


DB_FOLDER = 'db'
DB_PATH = os.path.join(DB_FOLDER, 'database.db')


if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    stamp = Column(DateTime)
    tweet_id = Column(Integer)
    user_id = Column(Integer)
    text = Column(String)
    from_stream = Column(Boolean)


def init_session():
    """
    Initializes the session by creating the database if not exists
    """
    engine = create_engine('sqlite:///'+DB_PATH)

    if not os.path.exists(DB_PATH):
        Base.metadata.create_all(engine)

    # try to create index, do nothing if the index already exists
    index = Index('index_tweet_tweet_id', Tweet.tweet_id)
    try:
        index.create(engine)
    except sqlalchemy.exc.OperationalError:
        pass

    session = sessionmaker(bind=engine)()
    return session


def add_tweet(stamp, tweet_id, user_id, text, from_stream):
    """
    Saves the tweet into the table if the tweet is no exists yet
    No need to update because the tweets can't change
    """
    if not tweet_exists(tweet_id):
        tweet = Tweet(
            stamp=stamp,
            tweet_id=tweet_id,
            user_id=user_id,
            text=text,
            from_stream=from_stream
            )
        session.add(tweet)
        session.commit()


def tweet_exists(tweet_id):
    """
    Uses Twitter's ID
    """
    row = session.query(Tweet).filter(Tweet.tweet_id==tweet_id).first()
    return bool(row)


session = init_session()
