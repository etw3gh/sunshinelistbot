#!/usr/bin/env python3
from login import Login

class SendTweet:

  def __init__(self):
    # get creds
    twitterlogin = Login()
    self.T = twitterlogin.api

  def tweet(self, text, inreplyto):
    self.T.PostUpdate(text, in_reply_to_status_id=inreplyto)