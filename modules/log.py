import datetime
import os


LOG_FOLDER = 'log'
LOG_PATH = os.path.join(LOG_FOLDER, 'twitter_stream.log')


if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)


def log(text):
    print text

    now = datetime.datetime.now()
    with open(LOG_PATH, 'a') as f:
        f.write('{} - {}\n'.format(now, text))
