#! /usr/bin/env python3

import os
import requests

feedback_list = []
feedback_form = {'name': " ", 'weight': " ", 'description': " ", 'image_name': " "}
folder = './supplier-data/descriptions'
image_folder = './supplier-data/iamges'
for file in os.listdir(folder):
  if os.path.isfile(os.path.join(folder, file)):
    with open(folder+'/'+file, 'r') as feedback:
     feedback_form['name'] = feedback.readline().strip()
     weight = feedback.readline().strip()
     feedback_form['weight'] = int(weight.strip(' lbs'))
     feedback_form['description'] = feedback.readline().strip()
     feedback_form['image_name'] = image_folder+'/'+file.strip('txt')+'jpeg'
     response = request.post("http://35.223.128.250/fruits", data=feedback_form)
     print(response.status_code)
     print(response.raise_for_status())
