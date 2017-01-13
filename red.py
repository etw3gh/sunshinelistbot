#!/usr/bin/env python

import redis, os

class RedSet:

  def __init__(self):
    # get redis connection details from environment
    r_db = 0
    r_port = 6379
    r_host = 'localhost'

    self.red = redis.StrictRedis(host=r_host, port=r_port, db=r_db)

    # store only the last id here for use with since_id
    self.lastreplyid = 'lrid'

    # store all replies here so no duplicate tweets are sent out
    self.allrepliyids = 'rids'

    # ignore these users
    self.ignorelist = 'bad'

    # unhandled errors. so we don't keep trying to answer but may get back to eventually
    self.errors = 'err'

  def adderr(self, id):
    self.red.sadd(self.errors, id)
    
  def addbad(self, id):
    self.red.sadd(self.ignorelist, id)

  def isbad(self, id):
    val = self.red.sismember(self.ignorelist, id)
    return True if val == 1 else False
  
  def setlastid(self, id):
    self.red.set(self.lastreplyid, id) 

  def getlastid(self):
    id = self.red.get(self.lastreplyid)
    return int(id)

  def addid(self, id):
    self.red.sadd(self.allrepliyids, id)

  def inset(self, id):
    val = self.red.sismember(self.allrepliyids, id)
    return True if val == 1 else False