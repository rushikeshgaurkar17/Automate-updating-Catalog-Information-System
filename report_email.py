#!/usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate_email, send_email

def pdf_body(input_for,desc_dir):
  res = []
  wt = []
  for item in os.listdir(desc_dir):
    filename=os.path.join(desc_dir,item)
    with open(filename) as f:
      line=f.readlines()
      weight=line[1].strip('\n')
      name=line[0].strip('\n')
      print(name,weight)
      res.append('name: ' +name)
      wt.append('weight: ' +weight)
      print(res)
      print(wt)
  new_obj = ""
  for i in range(len(res)):
    if res[i] and input_for == 'pdf':
      new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
  return new_obj

if __name__ == "__main__":
  user = os.getenv('USER')
  dd = '/home/{}/supplier-data/descriptions/'.format(user)
  cd = datetime.date.today().strftime("%B %d, %Y")
  title = 'Processed Update on ' + str(cd)
  generate_report('/tmp/processed.pdf', title, pdf_body('pdf',dd))
  esub = 'Upload Completed - Online Fruit Store'
  ebody = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email'
  msg = generate_email("automation@example.com", '{}@example.com'.format(user), esub, ebody, "/tmp/processed.pdf")
  send_email(msg)