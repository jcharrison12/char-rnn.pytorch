# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:44:57 2019

@author: jchar
"""

import tweepy
import run_generate
import sys

def main():
  consumer_key = sys.argv[1]
  consumer_secret = sys.argv[2]
  access_token = sys.argv[3]
  access_token_secret = sys.argv[4]

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)

  user = api.me()
  print(user.name)
  
  pt_file= sys.argv[5]
  text_file= sys.argv[6]
  tweet=run_generate.clean_title(pt_file, text_file)
  api.update_status(tweet)
  print('Done')
  
if __name__ == '__main__':
	main()
