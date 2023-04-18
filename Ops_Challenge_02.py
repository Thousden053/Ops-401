#!/usr/bin/python3

#Import libraries
import os, time
from datetime import datetime
#Infinite loops to keep pinging target

IP = input("Please enter an IP address\n")
currentTime = datetime.now()
while True:
#creates function for ping and status 
    def uptime(IP):
        response = os.system("ping -c 1 " + IP)
        #Check if host is up or down
        if response == 0:
            ping_status = ("Network is active")
        else:
            ping_status = ("Network is down")
        #waits 2 seconds before next response
        

        return ping_status
    ping_status_2 = uptime(IP)

    print(ping_status_2)
    print (currentTime)
    time.sleep(2)




