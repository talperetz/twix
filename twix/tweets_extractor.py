import csv
import tweepy
import json


def to_csv(tweets, path):
    delimited_tweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

    with open(path, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(delimited_tweets)


def to_json(tweets, path):
    tweets_dict = {attr: getattr(tweet, attr) for tweet in tweets for attr in ["id_str", "created_at", "text"]}
    with open(path, 'r') as f:
        json.dump(tweets_dict, f)


class TweetsExtractor:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key,
                                   consumer_secret)
        auth.set_access_token(access_token,
                              access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    def get_all_tweets(self, screen_name, path, fmt='csv', tweets_per_iter=200):
        tweets = []
        new_tweets = self.api.user_timeline(screen_name=screen_name, count=tweets_per_iter)
        tweets.extend(new_tweets)

        # save the id of the oldest tweet less one
        oldest = tweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            new_tweets = self.api.user_timeline(screen_name=screen_name, count=tweets_per_iter, max_id=oldest)
            tweets.extend(new_tweets)
            oldest = tweets[-1].id - 1

        if fmt == 'csv':
            to_csv(tweets, path)
        elif fmt == 'json':
            to_json(tweets, path)
        else:
            raise NameError("supported formats are 'json' and 'csv'")


if __name__ == '__main__':
    te = TweetsExtractor('your_consumer_key', 'your_consumer_secret', 'your_access_token', 'your_access_token_secret')
    te.get_all_tweets(screen_name='netanyahu', fmt='csv', path='../bb.csv')
