#!/usr/bin/env python 3

import email
import mimetypes
import smtplib
import os

def generate_email(sender, recipient, subject, body, atp):
  msg = email.message.EmailMessage()
  msg["From"] = sender
  msg["To"] = recipient
  msg["Subject"] = subject
  msg.set_content(body)

  if not atp == "":
    atf = os.path.basename(atp)
    mtp, _ = mimetypes.guess_type(atp)
    mtp, mstp = mtp.split('/', 1)

    with open(atp, 'rb') as ap:
      msg.add_attachment(ap.read(), maintype=mtp, subtype=mstp, filename=atf)

  return msg

def send_email(msg):
  mServer = smtplib.SMTP('localhost')
  mServer.send_message(msg)
  mServer.quit()