import tweepy
import time
from time import sleep
from credorg import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Fol-Fav-RT Bot v1.0 by deusopus (deusopus@gmail.com)")

while True:

    for tweet in tweepy.Cursor(api.search_tweets, q='#avax').items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)
            print(tweet.text)



        # Check that bot is not already following the user
        # Follow the user who tweeted

        #    if not tweet.user.following:
        #        tweet.user.follow()
        #        print('Followed')
        #        sleep(5)


        # check that bot has not already favorited the tweet
        # Favorite the tweet

            if not tweet.favorited:
                tweet.favorite()
                print('Liked')
                sleep(30)


        # Check that bot has not already retweeted the tweet
        # Retweet the tweet

            if not tweet.retweeted:
                tweet.retweet()
                print('Retweeted')
                sleep(30)

                sleep(120)
        except tweepy.errors.TweepyException as e:
            print(e)
