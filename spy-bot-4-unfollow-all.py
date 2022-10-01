import tweepy
import time
from time import sleep
from credorg import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


print("Unfollow-Bot v1.0 by deusopus (deusopus@gmail.com)")


while True:
    try:
        my_screen_name = api.get_user(screen_name="@cannacoin_org")
        for follower in my_screen_name.friends():
            api.destroy_friendship(screen_name = follower.screen_name)
            print(follower.screen_name + ' Unfollowed')
            sleep(15)

    except tweepy.errors.TweepyException as e:
        print(e)
