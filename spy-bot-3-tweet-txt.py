import tweepy
from time import sleep

from credorg import *

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Tweet-TXT-Bot v1.0 by deusopus (deusopus@gmail.com)")

# Open text file verne.txt (or your chosen file) for reading
my_file = open('tweets.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Tweet a line every 5 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(300)
             else:
                pass
        except tweepy.errors.TweepyException as e:
            print(e)

while True:

    tweet()
