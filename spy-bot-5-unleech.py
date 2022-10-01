import tweepy
from cred import *
import time
from time import sleep


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


print("Leech-B-Gone-Bot v1.0 by deusopus (deusopus@gmail.com)")


while True:
    try:


        if UNFOLLOW:
            my_screen_name = api.get_user(screen_name='@cannacoin_org')
            for follower in my_screen_name.friends():
                relStatus = api.get_friendship(source_id = my_screen_name.id , source_screen_name = my_screen_name.screen_name, target_id = follower.id, target_screen_name = follower.screen_name)
                if relStatus [0].followed_by:
                    print('{} he is following You'.format(follower.screen_name))
                else:
                    print('{} he is not following You'.format(follower.screen_name))
                    api.destroy_friendship(screen_name = follower.screen_name)
                    sleep(3)
    except tweepy.errors.TweepyException as e:
        print(e)
