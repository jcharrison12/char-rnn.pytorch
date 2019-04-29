# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:44:57 2019

@author: jchar
"""

import tweepy
import run_generate

consumer_key = 'RgrhdfWPd2fzLc0nEjoYLMAVK'
consumer_secret = 'OtFgSDNipdVtAviQUx21z31YBQQ5aGsx7zYRDua8ilNQXp5PDp'
access_token = '1121853140159148033-klLhu8C2SduEtVyITow2YRCAeMegbd'
access_token_secret = 'L9jCFzToQaisqPlVPRj74acimTamDFhFiv7OHFgoxyO2t'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

tweet=run_generate.clean_title("all_titles.pt", "all_titles.txt.")
api.update_status(tweet)
print('Done')