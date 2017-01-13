from translation import Translators
from query import Query

class TokenizeTweet:
  def __init__(self):
    self.hashes = Translators()
    self.shortcutkeys = self.hashes.uni_short.keys()

  def haskey(self, test, keys):
    return [s for s in keys if test in s]


  def tokenize(self, tweet):
    tweet = tweet.strip().lower()
    tweetlen = len(tweet)
    words = tweet.split(' ')
    numwords = len(words)
    if numwords < 3:
      pass
    
    possible_names = []
    hashtags = []
    help = []
    # save good data here
    final_query = Query()

    for word in words:
      word = word.strip()
      if word in self.hashes.ignore:
        continue
      if word in self.hashes.help:
        help.append(word)
        continue
      
      if word[0] == '#':
        hashtags.append(word)
        word = word.lstrip('#')
        pass
      
      if word[0] == '@':
        pass
      

      
      check = self.haskey(word, self.shortcutkeys)
      if len(check) > 0:
        if final_query.school is None:
          final_query.school = self.hashes.uni_short[word]
        continue  

      possible_names.append(word)
    
    for name in possible_names:
      continue

