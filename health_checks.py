#! /usr/bin/env python3

import shutil
import psutil
import socket
import emails
import os

error_subject = []

ip_address = socket.gethostbyname('localhost')
if ip_address != "127.0.0.1":
  error_subject.append("localhost cannot be resolved to 127.0.01")

total, used, free = shutil.disk_usage('/')
percent_free = (free/total) * 100
if percent_free < 20:
  error_subject.append("Available disk space is less than 20%")


cpu_percent_available = psutil.cpu_percent(interval=1)
if cpu_percent_available > 80:
  error_subject.append("CPU usage is over 80%")


free_memory = psutil.virtual_memory()
mb = 1024 * 1024
free_memory = free_memory.available/mb
if free_memory < 500:
  error_subject.append("Available memory is less than 500MB")

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Error - " + error_subject
body = "Please check your system and resolve the issue as soon as possible."
message = emails.generate_email(sender, receiver, subject, body)
if error_subject != []:
  emails.send_email(message)
