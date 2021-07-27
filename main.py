import smtplib
import datetime as dt
import time

# send the email
def send_email():
  FROM = "email@gmail.com"
  TO = "email@gmail.com"
  SUBJECT = "lorem ipsum"
  TEXT = """lorem ipsum"""
  message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
  
  SERVER = smtplib.SMTP("smtp.gmail.com", 587)
  SERVER.starttls()
  SERVER.login(FROM, "password")
  SERVER.sendmail(FROM, TO, message)
  SERVER.quit()

# send email at time
def send_at(send_time):  
  time.sleep(send_time.timestamp() - time.time())
  send_email(SUBJECT,TEXT)
  print("email sent!")

# Send a reccuring email
init_time = dt.datetime(2021,7,26,23,35,0) # time first email sent
end_time = dt.datetime (2021,7,27,23,36,0) # time period ends
interval = dt.timedelta(minutes=2*60) # interval between each email

# loop
send_time = init_time
while (time.time() < end_time.timestamp()):
  send_at(send_time)
  send_time = init_time + interval
