#!/usr/bin/env python3
from login import Login

class Mention:
  def __init__(self):
    self.user = ''
    self.text = ''
    self.id = 0

  def __str__(self):
    return 'from: {} ({}): {}'.format(self.user, self.id, self.text)

class Mentions:

  def __init__(self, creds):
    self.T = creds

    self.RESTRICT_BY_ID = '820379627248095232'
    # nothing before 2017 (>2016)
    self.NOT_BEFORE_YEAR = 2016

  def mentions(self, since=None):
    if since == None:
      self.RESTRICT_BY_ID

    mention_list = []
    search = self.T.GetMentions(include_entities=False, since_id=since)
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

if __name__ == '__main__':

  # aquire credentials from API Keys stored in environment variables
  twitterlogin = Login()
  creds = twitterlogin.api

  m = Mentions(creds)
  mlist = m.mentions()

  for mention in mlist:
    print (str(mention))
