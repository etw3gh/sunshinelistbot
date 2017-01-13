#!/usr/bin/env python3

from twitter import TwitterError

class SendTweet:

  def __init__(self, creds):
    self.T = creds

  def tweet(self, text, inreplyto):
    try:
      self.T.PostUpdate(text, in_reply_to_status_id=inreplyto)
      return 200
    except TwitterError as twe:
      return 187