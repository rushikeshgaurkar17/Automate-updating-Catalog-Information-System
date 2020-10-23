#! /usr/bin/env python3

import os
import requests

mydir = os.listdir('/data/feedback')
dict = {}
my_values = ("title","name","date","feedback")
for file in mydir:
 ffile = open('/data/feedback/' + file, "r")
 count = 0
 for line in ffile:
  if count == 0:
   dict['title'] = line
  elif count == 1:
   dict['name'] = line
  elif count == 2:
   dict['date'] = line
  else:
   dict['feedback'] = line
  count = count+1
 response = requests.post(r'http://34.123.244.18/feedback/', json=dict)
 print('Response', response.status_code)
 ffile.close()
