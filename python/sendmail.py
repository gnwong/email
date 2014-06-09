#!/usr/bin/python

import smtplib

# You also need to edit the message to reflect this information
sender     = "myemail@gmail.com" 
password   = "mypassword"              
recipients = "recipient@domain.com"

# Make the message here
message = """From: My Name <myemail@gmail.com>
To: Recipient <recipient@domain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: Automated Email

This is an automated e-mail message that has been sent
using Python's <b>smtplib</b> library.<br><br>

Note that setting "Content-type" to "text/html" allows us
to embed html languge in the message.
"""

## No need to edit things below here!

# We wrap this in a try/except block because
# smtplib throws exceptions
print("Attempting to send email now...")
try:
  server = smtplib.SMTP('smtp.gmail.com:587')
  username = sender
  password = password
  server.ehlo()
  server.starttls()
  server.login(username,password)
  server.sendmail([sender],recipients,message) 
  server.quit()
  print("Success!")
except smtplib.SMTPException as e:
  print("Error: Unable to send email with exception:")
  print(e)
