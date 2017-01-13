#!/usr/bin/env python3

class Mention:
  def __init__(self):
    self.user = ''
    self.text = ''
    self.id = 0

class Mentions:

  def __init__(self, creds):
    self.T = creds

    # this twitter bot has been around for a while
    # we'd like to ignore old tweets
    #
    # an old tweet from the mentions
    self.RESTRICT_BY_ID = '534033245575213056'
    # nothing before 2017 (>2016)
    self.NOT_BEFORE_YEAR = 2016

  def mentions(self, since=None):
    
    if since == None:
      self.RESTRICT_BY_ID

    mention_list = []
    search = self.T.GetMentions(include_entities=False) #, since_id=since)
    for s in search:
      year = s.created_at.split(' ')[-1]
      yint = int(year)
      if yint > self.NOT_BEFORE_YEAR:
        mention = Mention()
        mention.user = s.user.screen_name
        mention.text = s.text
        mention.id = s.id
        mention_list.append(mention)
    return mention_list