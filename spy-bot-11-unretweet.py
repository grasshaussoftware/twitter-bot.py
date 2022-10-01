import tweepy
from credorg import *
import time
from time import sleep

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Un-Tweet-Bot v1.0 by deusopus (deusopus@gmail.com)")

while True:
    for tweet in tweepy.Cursor(api.user_timeline, screen_name="@cannacoin_org").items():
        try:
            print('\nRe-Tweet by: @' + tweet.user.screen_name)
            target = (tweet.id)
            print(tweet.text)
            api.unretweet(target)
            print("**UNRETWEETED**")
            sleep(15)
        except tweepy.errors.TweepyException as e:
            print(e)
