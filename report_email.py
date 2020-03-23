#! /usr/bin/env python3

import os
import datetime
import reports
import emails


def prepare_report_body():
  folder = 'supplier-data/descriptions'
  body = []
  for file in os.listdir(folder):
    if os.path.isfile(os.path.join(folder, file)):
      files.append(file)
  for file in files:
    with open(folder+'/'+file, 'r') as description:
      name = description.readline().strip()
      weight = description.readline().strip()
      body.append('<br/>'+'name:'+name+'<br/>'+'weight:'+weight+'<br/>')
  return body

def current_date()
  date = datetime.datetime.now()
  date = date.strftime("%B %d %Y")
  return date


if __name__ == "__main__":
  report_body = prepare_report_body()
  title = "Processed Update on {}".format(current_date())
  reports.generate_report('tmp/processed.pdf', title, report_body)
  sender = automation@example.com
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
  message = emails.generate_email_with_attachment(sender, receiver, subject, email_body, "/tmp/proccessed.pdf")
  emails.send_email(message)
