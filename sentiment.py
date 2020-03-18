# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:12:44 2020

@author: Rachit
"""

import tweepy 
from textblob import TextBlob

consumer_key = '76qUNMblWo2e0jc1oDaP4I0GC'
consumer_secret = 'aCSpPJnr61Pl7ntmXH85AT0Zc09Tqd9IcwVrSDJPjPmrd0cOHJ' 


access_token = '924350760267206656-lckrrcz7VAA3dV5CD5IV6Ims4q5f0D4'
access_token_secret = 'Hi23CP5Ax8RQVEj9c5KlxeJvXaj6BeHSOgE9oPtMJWpRo'

#authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Corona')

for tweet in public_tweets:
    print(tweet.text)
    
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    
    