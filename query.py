#!/usr/bin/env python3
import requests, urllib, json
from result import Result


class Query:
  """
  an incoming tweet is scanned for mentions of a university
  this is stored in school
  
  other data is filtered out and remaining words are stored in names

  we take only the first 2 words in names and run 2 queries

  first query uses name[0] as first name and name[1] as last name
  second query uses name[1] as first name and name[0] as last name 

  TODO determine which results to use
  
  """

  def __init__(self):
    self.school = None
    self.names = []

  def get(self, service_url):
    """
    at least one name should be sent

    if one name is sent, it will be treated as a last NameError

    if two names are sent they will be treated as first & last in that order

    TODO if no hits are obtained for either case we may switch first / last order
    """
    params = None

    nameslen = len(self.names)
    
    # this case is handled by bot.py
    if nameslen == 0:
      return
    
    elif nameslen == 1:
      params = {'school': self.school, 'last': self.names[0], 'year': '2015'}
    
    else:
      params = {'school': self.school, 'first': self.names[0], 'last': self.names[1], 'year': '2015'}

    if params is not None:
      u = service_url + urllib.parse.urlencode(params)

      print ('making request: {}\n'.format(u))

      req = requests.get(u)

      

      request_status = req.status_code

      jdict = json.loads(req.text)

      rows = jdict['rows']
      count = jdict['count']
      
      # returned in the data object
      service_status = jdict['status']

      print('results: {}\n'.format(count))
      result_array = []
      for row in rows:
        result = Result(row)
        result_array.append(result)
      return result_array