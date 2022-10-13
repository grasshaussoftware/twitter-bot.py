import tweepy
import time
from time import sleep
from cred import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


print("Follow-Who-They-Follow Bot v1.0 by deusopus (deusopus@gmail.com)")


target_screen_name = api.get_user(screen_name='@LolliScroggin')

while True:
    try:

        for follower in target_screen_name.friends():
            if not follower.protected:
                if not follower.following:
                    api.create_friendship(screen_name = follower.screen_name)
                    print(follower.screen_name + ' followed from @' + target_screen_name.screen_name)
                    target_screen_name = follower
                    sleep(500)
    except tweepy.errors.TweepyException as e:
        print(e)
