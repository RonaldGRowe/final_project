#!/usr/bin/env python3

import os
from PIL import Image


folder = '/supplier-data/images'
files = []
for file in os.listdir(folder):
  if os.path.isfile(os.path.join(folder, file)):
    files.append(file)
for file in files:
  if file != ".DS_Store":
    img_location = folder+'/'+file
    img = Image.open(img_location)
    img = img.convert('RGB')
    new_img = img.resize((600,400))
    new_img.save(img_location+'.jpeg', "JPEG")
