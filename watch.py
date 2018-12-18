#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import smtplib

######### Edit only this #############
minutes = 5                                 # Check the page in x minute intervals. Default: 5 minutes
smtp_server = "smtp.yoursmtpserver.com"     # SMTP server address. example: smtp.mail.yahoo.com
from_email = 'your@email.com'               # Your email address
to_email  = 'to@email.com'                  # The emil address where you want to send the mail
subject='subject'                           # Subject
message_text = 'message'                    # Message

username = str('your@email.com')            # Your username/email address
password = str('yourPassword')              # Your password to your email address

website_link = 'http://example.com'         # The website you want to watch
######### Edit only this #############

message = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_email, to_email, subject, date, message_text )
os.system('wget ' + website_link + ' -O ./old.html')

while True:
    os.system('wget ' + website_link + ' -O ./new.html')
    os.system('diff ./old.html ./new.html > ./result.txt')
    os.system('mv ./new.html ./old.html')
    lines = 0
    f = open("result.txt","r")
    for line in f:
        lines += 1
    if lines > 0:
        try :
            server = smtplib.SMTP(smtp_server,587)
            server.starttls()
            server.login(username,password)
            server.sendmail(from_email, to_email,message)
            server.quit()
            print 'E-mail sent!'
            break
        except :
            print 'Error.'
    os.system('rm ./result.txt')
    time.sleep(60*minutes)
