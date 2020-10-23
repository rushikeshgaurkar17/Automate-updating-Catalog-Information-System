#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails
import os

def check_localhost():
  localhost = socket.gethostbyname('localhost')
  return localhost == "127.0.0.1"

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def check_memory_usage():
  mu = psutil.virtual_memory().available
  total = mu / (1024.0 ** 2)
  return total > 500

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 80

def send_email(subject):
  email = emails.generate_email("automation@example.com", '{}}@example.com'.format(os.getenv('USER')), subject, "Please check your system and resolve the issue as soon as practicable", "")
  emails.send_email(email)

if not check_cpu_usage() :
  subject="Error - CPU usage is over 80%"
  print(subject)
  send_email(subject)

if not check_memory_usage():
  subject = "Error - Available memory is less than 500MB"
  print(subject)

if not check_disk_usage('/') :
  subject = "Error - Available disk space is less than 20%"
  print(subject)
  send_email(subject)

if not check_localhost():
  subject = "Error - localhost cannot be resolved to 127.0.0.1"
  print(subject)
  send_email(subject)
