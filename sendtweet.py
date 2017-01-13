#!/usr/bin/env python3
from twitter import TwitterError

class SendTweet:

  def __init__(self, creds):
    self.T = creds
    self.MAX = 140

  def tweet(self, text, inreplyto):
    try:
      truncated = text[:self.MAX]
      self.T.PostUpdate(truncated, in_reply_to_status_id=inreplyto)
      return 200
    except TwitterError as twe:
      return 187