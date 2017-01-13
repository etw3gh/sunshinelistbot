#!/usr/bin/env python3
from translation import Translators
from query import Query

class TokenizeTweet:
  def __init__(self):
    self.hashes = Translators()
    self.shortcutkeys = self.hashes.uni_short.keys()

  def haskey(self, test, keys):
    return [s for s in keys if test in s]


  def tokenize(self, tweet):
    try:
      tweet = tweet.strip().lower()
      tweetlen = len(tweet)
      words = tweet.split(' ')
      numwords = len(words)
      if numwords < 3:
        pass
      
      help = []
      query = Query()
      for word in words:
        word = word.strip()
        if word in self.hashes.ignore or word[0] == '#' or word[0] == '@':
          continue

        if word in self.hashes.help:
          help.append(word)
          continue
        
        check = self.haskey(word, self.shortcutkeys)
        if len(check) > 0:
          if query.school is None:
            query.school = self.hashes.uni_short[word]
          continue  

        query.names.append(word)
      
      return self.query
    except Exception as tokex:
      print(tokex)
      return query
