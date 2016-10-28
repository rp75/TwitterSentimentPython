import tweepy
from textblob import TextBlob
consumer_key = '<Your key>'
consumer_secret = '<Your key>'
access_token = '<Your key>'
access_token_secret = '<Your key>'

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
TwitterApi= tweepy.API(auth)
public_tweets = TwitterApi.search("Tatagroup")


tweet_data = {'Tweet': [],
        'Polarity': [],
        'Subjectivty': []}

import pandas as pd
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)

    tweet_data["Tweet"].append(tweet.text)
    tweet_data["Polarity"].append(str(analysis.sentiment.polarity))
    tweet_data["Subjectivty"].append(str(analysis.sentiment.subjectivity))

df = pd.DataFrame(tweet_data, columns = ['Tweet', 'Polarity', 'Subjectivty'])
df
