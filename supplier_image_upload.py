#!/usr/bin/env python3
import requests, os
url = "http://localhost/upload/"
USER = os.getenv('USER')
imdir = '/home/{}/supplier-data/images/'.format(USER)
files = os.listdir(imdir)
for imname in files:
  if not imname.startswith('.') and 'jpeg' in imname:
    impath = imdir + imname
    with open(impath, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
