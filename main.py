import smtplib
import datetime as dt
import time

def send_email(SUBJECT,TEXT):
  FROM = "email@gmail.com"
  TO = "email@gmail.com"
  message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

  SERVER = smtplib.SMTP("smtp.gmail.com", 587)
  SERVER.starttls()
  SERVER.login(FROM, "password")
  SERVER.sendmail(FROM, TO, message)
  SERVER.quit()

SUBJECT = "lorem ipsum"

TEXT = """lorem ipsum"""

def send_email_time():
  send_time = dt.datetime(2021,7,26,23,35,0) #time in AEST
  time.sleep(send_time.timestamp()-time.time())
  send_email(SUBJECT,TEXT)
