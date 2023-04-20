#!/usr/bin/python3

#Tyler Housden
#Received help from reviewing Sierra and company code

#Import libraries
import os, time, smtplib 
from datetime import datetime
from getpass import getpass 

# Assign variables
currentTime = datetime.now()
up = "Up"
down = "Down"


#prompts for email to use for notifications.
email = input("Please enter your email address\n")
pw = getpass("Please enter the password\n")
#asks user for input of ip address
IP = input("Please enter an IP address\n")
print("\n")

# function for ping and comparing previous ping status with current.
def ping_test(IP): 
    global last
    ping_result = os.system("ping -c 1 " + IP)
        #Check if host is up or down
    if ping_result == 0:
        stat = up
        
    elif ping_result != 0:
        stat = down
    return stat
def send_message(stat):

    #create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(email, pw)
    # Message 
    message = f"Server is {stat.lower()}"
    s.sendmail(email,email, message)
    # Terminate Session
    s.quit()

last = ping_test(IP)

#Infinite loops to keep pinging target
while True:
    current_stat = ping_test(IP)
    if current_stat != last:
#calls function 
        send_message(current_stat)
        last = current_stat

# gives 2 second wait time before continuing loop 
    time.sleep(2)
