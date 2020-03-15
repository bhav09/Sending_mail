import os
import smtplib

email_id=os.environ.get('MY_EMAIL')
email_pass=os.environ.get('GMAIL_APP_PASS')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email_id,email_pass)
    subject='Mail via SSL connection'
    body=' (to SSL) I feel safe here.'
    msg=f'Subject:{subject}\n\n{body}'
    smtp.sendmail(email_id,email_id,msg)
print("Mail Sent!")