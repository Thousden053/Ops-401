#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt

import time
import getpass

# Define functions
def iterator():
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)

def check_password():
    password = getpass.getpass("Enter the password you want to check: ")
    filepath = input("Enter your dictionary filepath: ")
    with open(filepath, encoding="ISO-8859-1") as file:
        for line in file:
            if password == line.strip():
                print("The password was found in the word list.")
                return
    print("The password was not found in the word list.")

# Main
while True:
    mode = input("""
    Brute Force Wordlist Attack Tool Menu
    1 - Offensive, Dictionary Iterator
    2 - Defensive, Password Recognized
    3 - Exit
    Please enter a number: 
    """)
    if mode == "1":
        iterator()
    elif mode == "2":
        check_password()
    elif mode == "3":
        break
    else:
        print("Invalid selection.")
