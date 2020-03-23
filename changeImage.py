#!/usr/bin/env python3

import os
from PIL import Image


folder = './supplier-data/images'
files = []
for file in os.listdir(folder):
  if os.path.isfile(os.path.join(folder, file)):
    files.append(file)
for file in files:
  if file != "README" and file != "LICENSE":
    img_location = folder+'/'+file
    new_name_location = folder+'/'+file[:3]+'.jpeg'
    img = Image.open(img_location)
    img = img.convert('RGB')
    new_img = img.resize((600,400))
    new_img.save(new_name_location, "JPEG")
