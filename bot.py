#!/usr/bin/env python3
from mentions import Mentions
from sendtweet import SendTweet

m = Mentions()
mention_list = m.mentions()

tweeter = SendTweet()

for m in mention_list:
  tweet = 'hello @{}, thanks for the mention...'.format(m.user)
  print (tweet)
  tweeter.tweet(tweet, m.id)