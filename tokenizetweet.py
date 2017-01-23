#!/usr/bin/env python3
from translation import Translators
from query import Query
from datetime import date
import sys, os

class TokenizeTweet:
  def __init__(self):
    self.hashes = Translators()
    self.shortcutkeys = self.hashes.uni_short.keys()

  def haskey(self, test, keys):
    return [s for s in keys if test in s]

  def purge_unwanted(self, L):
    return [x for x in L if x[0]!='#' and x[0]!='@' and x not in self.hashes.ignore]

  def purge_lista_of_listb(self, a, b):
    return [x for x in a if x not in b]

  def extract_numbers(self, a):
    return [x for x in a if x.isnumeric()]

  def purge_non_years_from_numeric(self, a):
    Y = date.today().year
    return [ x for x in a if len(x)==4 and int(x)>=1996 and int(x)<Y]

  def tokenize(self, tweet):
    try:
      tweet = tweet.strip().lower()
      tweetlen = len(tweet)
      words = tweet.split(' ')
      numwords = len(words)
      if numwords < 3:
        pass

      query = Query()

      # strip out unwanted (hashtags, mentions and ignores)
      try:
        words = self.purge_unwanted(words)
      except IndexError:
        pass

      #if the length changes after help keywords are purged, set help to True
      wlen = len(words)
      words = self.purge_lista_of_listb(words, self.hashes.help)

      if len(words) < wlen:
        query.help = True

      #extract numbers
      nums = self.extract_numbers(words)

      #get first 2 years for range, sort in ascending order
      yrs = sorted(self.purge_non_years_from_numeric(nums)[0:2])

      #the web service will detect a hypenated year as a range
      query.years = '-'.join(yrs)


      #remove numbers before proceeding
      words = self.purge_lista_of_listb(words, nums)
      
      # iterate over remaining words until a school name is found
      # if used, remove from list
      for word in words:
        word = word.strip()
        if word == '':
          continue
        check = self.haskey(word, self.shortcutkeys)
        if len(check) > 0:
          if query.school is None:
            query.school = self.hashes.uni_short[word]
            wordindex = words.index(word)
            del words[wordindex]
          continue  
      
      # raise excepions unless help flag is True, then the bot will send out a help tweet
      if query.school is None:
        if query.help == True:
          return query
        raise Exception('no school found')
      if len(words) == 0:
        if query.help == True:
          return query        
        raise Exception('no names found')

      # whatever remains, push the first two onto the names stack
      query.names.extend(words[0:2])

      return query

    except Exception as ex:
      exc_type, exc_obj, exc_tb = sys.exc_info()
      fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
      print ('{}: {} ({})  -- \n\n'.format(fname, exc_tb.tb_lineno, str(ex), exc_type))
      raise Exception(str(ex))
      
