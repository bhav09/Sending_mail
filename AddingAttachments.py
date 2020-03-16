#adding attachments like images
import smtplib
import os
from email.message import EmailMessage
import imghdr #for python to determine what type of the image is being attached

email = os.environ.get('MY_EMAIL')
password = os.environ.get('GMAIL_APP_PASS')
msg=EmailMessage()
receivers=['bhavishyapandit9@gmail.com','bhavishyapandit@rocketmail.com']
msg['Subject']='Adding Multiple  Attachments'
msg['From']=email
msg['To']=receivers
msg.set_content('Find the attachments.')
attachments=['C:/Users/91884/Pictures/images.jpg','C:/Users/91884/Pictures/images (1).jpg']

#adding attachments
for file in attachments:
    with open(file,'rb')  as f:#rb means read byte
        file_data=f.read()
        file_type=imghdr.what(f.name)
        file_name=f.name
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename='images')

#sending mail
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email,password)
    smtp.send_message(msg)
print('Mail sent')
