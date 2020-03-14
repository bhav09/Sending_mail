#we are using a local debug server because we cannot really send mails to other people  for testing .
# #So for testing purposes we are sending these mails to ourselves

#python -m smtpd -c DebuggingServer -n localhost:1025

import os
email_id=os.environ.get('MY_EMAIL')
email_pass=os.environ.get('GMAIL_APP_PASS')
import smtplib

with smtplib.SMTP('localhost',1025) as smtp:
    '''  # ehlo () identifies the mail server that we are using
    smtp.ehlo()

    #encrypt the traffic
    smtp.starttls()

    #to re identify ourselves as an encrypted connection
    smtp.ehlo()

    smtp.login(email_id,email_pass)
    '''
    subject = 'SMTP DEMO: DebuggingServer'
    body = 'Man ! This is Amazing .. !!'

    msg = f"Subject:{subject}\n\n{body}"
    #sender's mail and then the receivers mail
    smtp.sendmail(email_id,'bhavishyapandit9@gmail.com',msg)
print('Mail Sent !')
