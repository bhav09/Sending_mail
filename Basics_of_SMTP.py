'''SMTP stands for simple mail transfer protocol.'''
import os
email_id=os.environ.get('MY_EMAIL')
email_pass=os.environ.get('GMAIL_APP_PASS')
import smtplib

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    # ehlo () identifies the mail server that we are using
    smtp.ehlo()

    #encrypt the traffic
    smtp.starttls()

    #to re identify ourselves as an encrypted connection
    smtp.ehlo()

    smtp.login(email_id,email_pass)

    subject = 'Demo for SMTP'
    body = 'Hey , how you doing?'

    msg = f"Subject:{subject}\n\n{body}"
    #sender's mail and then the receivers mail
    smtp.sendmail(email_id,'bhavishyapandit9@gmail.com',msg)
print('Mail Sent !')


