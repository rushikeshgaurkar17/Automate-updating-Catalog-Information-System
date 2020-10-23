#!/usr/bin/env python3

import os, sys
from PIL import Image

user = os.getenv('USER')
imdir = '/home/{}/supplier-data/images/'.format(user)
for imname in os.listdir(imdir):
  if not imname.startswith('.') and 'tiff' in imname:
    impath = imdir + imname
    path = os.path.splitext(impath)[0]
    img = Image.open(impath)
    npath = '{}.jpeg'.format(path)
    img.convert('RGB').resize((600,400)).save(npath, "JPEG")
