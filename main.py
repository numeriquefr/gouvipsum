import random
import os

import tweepy


class Twitter(object):
    def __init__(self):
        super(Twitter, self).__init__()
        auth = tweepy.OAuthHandler(
            os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"]
        )
        auth.set_access_token(
            os.environ["TWITTER_ACCESS_TOKEN"],
            os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        )

        self.api = tweepy.API(auth)
        self.api.verify_credentials()

    def tweet(self, text):
        return self.api.update_status(text)


with open("words.txt") as f:
    words = set([l.strip() for l in f.readlines()])

nb_words = random.randint(3, 5)
sentence = " ".join(random.sample(words, nb_words))
Twitter().tweet(sentence)
