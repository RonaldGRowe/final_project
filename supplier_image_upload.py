#! /usr/bin/env python3

import os
import requests

folder = './supplier-data/images'
folder_files = []
for file in os.listdir(folder):
  if os.path.isfile(os.path.join(folder, file)):
    if file[-4:] == 'jpeg':
      folder_files.append(file)
url = " http://35.232.195.35/upload/"
for file in folder_files:
  with open(folder+'/'+file, 'rb') as upload:
    r = requests.post(url, files={'file': upload})
