import os
import smtplib
from email.message import EmailMessage

email_id=os.environ.get('MY_EMAIL')
password=os.environ.get('GMAIL_APP_PASS')
msg=EmailMessage()
msg['Subject']='Organised Mail'
msg['From']=email_id
msg['To']=email_id
msg.set_content('What a beautiful day it is.')
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_id,password)
    smtp.send_message(msg)
print('Mail Sent!')