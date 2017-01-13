#!/usr/bin/env python3
class Result:
  def __init__(self, rowDict):
    self.school = rowDict['school']
    self.last = rowDict['last']
    self.first = rowDict['first']
    self.title = rowDict['title']
    self.salary = rowDict['salary']
    self.taxable = rowDict['taxable']
    self.year = rowDict['year']

  def __str__(self):
    tostr = 'school: {}, name: {}, title: {}, salary: {}, taxable: {}, year: {}'
    name = "{} {}".format(self.first, self.last)
    output = tostr.format(self.school, name, self.title, self.salary, self.taxable, self.year)
    return output