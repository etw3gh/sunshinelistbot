#!/usr/bin/env python3
from mentions import Mentions
from sendtweet import SendTweet
from tokenizetweet import TokenizeTweet
from login import Login
from result import Result
from query import Query

from red import RedSet
import sys, os
from time import sleep

sleeptime = 65
sleeptesting = 10

service_url = "http://openciti.ca/cgi-bin/mp/get?"

# processes incoming tweets
tokenizer = TokenizeTweet()

# aquire credentials from API Keys stored in environment variables
twitterlogin = Login()
creds = twitterlogin.api

# sends outgoing tweets (responses to salary data requests)
tweeter = SendTweet(creds)

# simple persistent storage to prevent duplicate tweets and twitter search cursor
redisdb = RedSet()

# get mentions for the twitter handle associated with the API Keys
getmentions = Mentions(creds)

while True:
  try:
    # get the last id so searches can exclude previously answered tweets
    lastid = redisdb.getlastid()
    # get a list of tweets mentioning the bot account  
    mention_list = getmentions.mentions(lastid)

    # process and respond if necessary
    for m in mention_list:
      print ('processing: ' + str(m.id))
      # proceed only if we've not stored the id in this set
      if not redisdb.inset(m.id):
        #uery = Query()
        query = tokenizer.tokenize(m.text)
        print(query.school)
        print(query.names)

        if len(query.names) > 0:
          results = query.get(service_url)
          lenres = len(results)
          if lenres == 0:
            tweeter.nores(m)
          elif lenres > 7:
            tweeter.replytoomany(m, len(results))
            continue
             
          for result in results:
            print(str(result))
            tweeter.tweet(result, m)
        else:
          tweeter.replyvague(m)

    print ('sleeping....')
    sleep(sleeptime)

  except Exception as ex:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print ('{}: {} ({})  -- \n\n'.format(fname, exc_tb.tb_lineno, str(ex), exc_type))
    #sleep(60)
    break