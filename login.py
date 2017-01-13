#!/usr/bin/env python3
import os, twitter

class Login:

  def __init__(self):
    cs = os.environ['CS']
    ck = os.environ['CK']
    ats = os.environ['ATS']
    at = os.environ['AT']
    self.api = twitter.Api(consumer_key=ck, consumer_secret=cs, access_token_key=at, access_token_secret=ats)
