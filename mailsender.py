# -*- coding: cp1254 -*-

from email.mime.text import MIMEText
import time
import smtplib
#import schedule
import getpass

sender = input("Enter your mail:")  
password = getpass.getpass("Enter your password:")    # We get information from user
receiver = input("Enter receiver(.txt):") 
subject =  input("Enter subject:")
message =  input("Enter your message(.txt):")


file = open(receiver)           # opening recevier's .txt file
info = file.readlines()         # reading by list

file1 = open(message, "r+")     # opening message's .txt file
info1 = file1.readline(400)     # reading by straight

mail = MIMEText(info1, "html", "cp1254")  # turning message into html type
mail["From"] = sender
mail["Subject"] = subject
mail["To"] = ",".join(info) 
mail = mail.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)   # connecting the server 
server.ehlo()
server.starttls()
server.login(sender, password)

print("Login Success")
# if you are develoaper you can set day with schedule and make this active
"""
def job():
    server.sendmail(sender, info, mail)    
schedule.every().monday.at("15.30").do(job)
"""

print ("Email has sended")
"""
while True:
    schedule.run_pending()
    time.sleep(10)
   """

server.quit()

time.sleep(10)

exit()
