#!/usr/bin/env python3
from login import Login

class Mention:
  def __init__(self):
    self.user = ''
    self.text = ''
    self.id = 0
class Mentions:

  def __init__(self):
    # get creds
    twitterlogin = Login()
    self.T = twitterlogin.api

    # this twitter bot has been around for a while
    # we'd like to ignore old tweets
    self.RESTRICT_BY_ID = '534033245575213056'
    self.NOT_BEFORE_YEAR = 2016

  def mentions(self):
    mention_list = []
    search = self.T.GetMentions(include_entities=False, since_id=self.RESTRICT_BY_ID)
    for s in search:
      year = s.created_at.split(' ')[-1]
      yint = int(year)
      if yint > self.NOT_BEFORE_YEAR:
        mention = Mention()
        mention.user = s.user.screen_name
        mention.text = s.text
        mention.id = s.id
        #print ('{}: {} --- {}\n'.format(s.user.screen_name, year, s.text))
        mention_list.append(mention)
    return mention_list