# import the module
import tweepy

from credorg import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Twitter-DM-Bot v1.0 by deusopus (deusopus@gmail.com)")

text = 'Join us on Discord... https://discord.gg/btMwEseSDw'

while True:
# printing the latest 20 followers of the user
    for user in api.get_followers(screen_name="@cannacoin_org"):
        try:
            print (user.screen_name)
            api.update_status(f'@user.screen_name' + text)
        except tweepy.errors.TweepyException as e:
            print(e)
