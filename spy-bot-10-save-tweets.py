import sys
import tweepy


from cred import *
from config import QUERY, UNFOLLOW, FOLLOW, LIKE, RETWEET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

print("Tweet-Bot v1.0 by deusopus (deusopus@gmail.com)")
print("Search criteria :", QUERY) #parses through tweets for the hashtag in config.py
print("UnFollow leech accounts :", UNFOLLOW)
print("Like user's tweets :", LIKE)
print("Retweet user's tweets :", RETWEET)
print("Follow user's account :", FOLLOW)

while True:

    for tweet in tweepy.Cursor(api.search_tweets, 'QUERY').items():
        try:
            print('\nTweet by: @' + tweet.user.screen_name)


            print(tweet.text)

            original_stdout = sys.stdout # Save a reference to the original standard output

            with open('tweet-stream.txt', 'w') as f:
                sys.stdout = f # Change the standard output to the file we created.
                print('\n' + tweet.text)
                sys.stdout = original_stdout # Reset the standard output to its original value

        except tweepy.errors.TweepyException as e:
            print(e)
