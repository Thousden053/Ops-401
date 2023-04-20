#!/usr/bin/python3

#Import libraries
import os, time, smtplib 
from datetime import datetime
from getpass import getpass 

#prompts for email to use for notifications.

currentTime = datetime.now()
up = 0
down = 1
last = 0
email = input("Please enter your email address\n")
pw = getpass("Please enter the password\n")
#asks user for input of ip address
IP = input("Please enter an IP address\n")
print("\n")
def send_downmessage():
    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email, pw)
    # Message 
    message = ("Subject: Python script\n\nYour server is not serving " + currentTime)
    s.sendmail("pingbeat@bot.com",email, message)
    # Terminate Session
    s.quit()

def send_upmessage():
    
    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email, pw)
    # Message 
    message = ("Subject: Python script\n\n\Your server is serving " + currentTime)
    s.sendmail("pingbeat@bot.com",email, message)
    # Terminate Session
    s.quit()

def ping_test(): 
    global last
    ping_result = os.system("ping -c 1 " + IP)
        #Check if host is up or down
    if  ((ping_result != last) and (ping_result == up)):
        last = up
        send_upmessage()
    elif ((ping_result != last) and (ping_result == down)):
        last = down
        send_downmessage()

#Infinite loops to keep pinging target
while True:
#creates function for ping and status 
    ping_test()
    time.sleep(2)
