# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:12:44 2020

@author: Rachit
"""

import tweepy 
from textblob import TextBlob

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret' 


access_token = 'access_token'
access_token_secret = 'access_token_secret'

#authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Corona')

for tweet in public_tweets:
    print(tweet.text)
    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
    
