import tweepy
import time
from time import sleep
from credorg import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Fav-RT-KW Bot v1.0 by deusopus (deusopus@gmail.com)")



def tweet_retweet():


    # check that bot has not already favorited the tweet
    # Favorite the tweet

    if not tweet.favorited:
        tweet.favorite()
        print('Liked')
        sleep(3)

    # Check that bot has not already retweeted the tweet
    # Retweet the tweet

    if not tweet.retweeted:
        tweet.retweet()
        print('Retweeted')
        sleep(500)


keywords = '@norml -filter:retweets'

while True:

    for tweet in tweepy.Cursor(api.search_tweets, q=keywords, lang='en').items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print(tweet.text)
            
            tweet_retweet()
            
                            
        except tweepy.errors.TweepyException as e:
            print(e)