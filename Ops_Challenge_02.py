#!/usr/bin/python3

#Import libraries
import os, time
from datetime import datetime
#asks user for input of ip address
IP = input("Please enter an IP address\n")
#set variable for timestamp
currentTime = datetime.now()
#Infinite loops to keep pinging target
while True:
#creates function for ping and status 
    def uptime(IP):
        response = os.system("ping -c 1 " + IP)
        #Check if host is up or down
        if response == 0:
            ping_status = ("Network is active")
        else:
            ping_status = ("Network is down")
        #outputs ping status 
        return ping_status
    #assigns uptime function with IP variable to pingstatus2 variable
    ping_status_2 = uptime(IP)
    #outputs pingstatus2 variable
    print(ping_status_2)
    #prints time stamp at the end of each ping.
    print (currentTime)
    #sleeps command for 2 seconds before completing the loop and running from the top.
    time.sleep(2)




