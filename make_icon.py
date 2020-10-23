#!/usr/bin/env python3
import os
from PIL import Image

mydir = os.listdir()
for file in mydir:
 if file.startswith('ic_'):
  image = Image.open(file)
  image = image.rotate(-90)
  new_image = image.resize((128,128))
  new_image.convert('RGB').save('/opt/icons/'+file+'.jpeg')
