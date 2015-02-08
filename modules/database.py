import os

from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_FOLDER = 'db'
DB_PATH = os.path.join(DB_FOLDER, 'database.db')


if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    stamp = Column(DateTime)
    user_id = Column(Integer)
    text = Column(String)
    from_stream = Column(Boolean)


def init_session():
    engine = create_engine('sqlite:///'+DB_PATH)

    if not os.path.exists(DB_PATH):
        Base.metadata.create_all(engine)

    session = sessionmaker(bind=engine)()
    return session


def add_tweet(stamp, user_id, text, from_stream):
    tweet = Tweet(
        stamp=stamp,
        user_id=user_id,
        text=text,
        from_stream=from_stream
        )
    session.add(tweet)
    session.commit()


session = init_session()
