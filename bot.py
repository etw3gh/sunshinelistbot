#!/usr/bin/env python3
from mentions import Mentions
from sendtweet import SendTweet
from login import Login
from red import RedSet
import sys

twitterlogin = Login()
creds = twitterlogin.api



tweeter = SendTweet(creds)

redisdb = RedSet()

lastid = redisdb.getlastid()

m = Mentions(creds)
mention_list = m.mentions(lastid)

for m in mention_list:
  tweet = 'hello @{}, thanks for the mention...'.format(m.user)
  
  if not redisdb.inset(m.id):

    return_code = tweeter.tweet(tweet, m.id)

    if return_code == 200:
      redisdb.setlastid(m.id)
      redisdb.addid(m.id)
      print('OK: {} {}'.format(m.id, tweet))
    elif return_code == 187:
      print('DUPE: {} '.format(m.id)) 