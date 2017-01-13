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

  def setlastid(self, id):
    self.red.set(self.lastreplyid, id) 

  def getlastid(self):
    return self.red.get(self.lastreplyid)

  def addid(self, id):
    self.red.sadd(self.allrepliyids, id)

  def inset(self, id):
    val = self.red.sismember(self.allrepliyids, id)
    return True if val == 1 else False