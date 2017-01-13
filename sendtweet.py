#!/usr/bin/env python3
from twitter import TwitterError
from red import RedSet
from translation import Translators
import random

class SendTweet:

  def __init__(self, creds):
    self.T = creds
    self.MAX = 140
    self.vague = 'Hello @{}, please give us a bit more to go on such as first name folowed by last name'
    self.toomany = 'Hello @{}, we found {} results, try to narrow it down a bit'
    self.noresults = 'Hello @{}, no results were found for your query. Please try again.'
    self.redisdb = RedSet()
    self.hashes = Translators()
    self.sunshine = '#sunshinelist'

  def nores(self, mention):
    # ensure only one @ is put before the reply handle
    u = mention.user.lstrip('@')
    tweet = self.noresults.format(u)
    r = self.send(tweet, mention.id)
    return r


  def replyvague(self, mention):
    # ensure only one @ is put before the reply handle
    u = mention.user.lstrip('@')
    tweet = self.vague.format(u)
    r = self.send(tweet, mention.id)
    return r

  def replytoomany(self, mention, count):
    # ensure only one @ is put before the reply handle
    u = mention.user.lstrip('@')
    tweet = self.toomany.format(u, count)
    r = self.send(tweet, mention.id)
    return r

    
  def tweet(self, result, mention):

    u = mention.user.lstrip('@')
    text = self.construct(result, mention.user)
    r = self.send(text,mention.id)
    return r
  

  def construct(self, result, user):
    name = '{} {}'.format(result.first, result.last)
    sal = '${:0,.2f}'.format(result.salary)
    year = str(result.year)
    try:
      hashtag = self.hashes.hashtags[result.school]
    except:
      hashtag = '#sunshinelist #ongov #onpoli'
    
    tweet = 'Hello @{}, {} made {} in {} {}'.format(user, name, sal, year, hashtag)
    return tweet

  def send(self, text, id):
    try:
      truncated = text[:self.MAX]
      
      #only add sunshine list hashtag occasionally
      rint = random.randint(0,10)
      if rint == 5:
        if len(truncated) + len(self.sunshine) < 140:
          truncated = '{} {}'.format(truncated, self.sunshine)

      self.T.PostUpdate(truncated, in_reply_to_status_id=id)
      self.redisdb.setlastid(id)
      self.redisdb.addid(id)      
    except TwitterError as twe:
      self.redisdb.setlastid(id)
      self.redisdb.addid(id)
      self.redisdb.adderr(id)