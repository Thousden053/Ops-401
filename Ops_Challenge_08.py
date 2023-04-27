#!/usr/bin/python3

#Tyler Housden

# took my code from yesterday and asked chat gpt to show me how to implement "dry".
# took that code and added todays code to it.

import os, time
from cryptography.fernet import Fernet

# Declare Functions

# Function for writing key.
def write_key():
    # Generate key and save it to a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function for loading key
def load_key():
    # Load key from file named key.key
    return open("key.key", "rb").read()

# Function for displaying the menu
def display_menu():
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Encrypt a folder", "6: Decrypt a folder", "7: Exit"]
    for i in menu:
        print(i)

# Function for processing files
def process_file(mode, file_name, key):
    with open(file_name, "rb") as file:
        file_data = file.read()

    fernet = Fernet(key)

    if mode == "1":
        encrypted = fernet.encrypt(file_data)
        with open(file_name, "wb") as file:
            file.write(encrypted)
        return encrypted
    elif mode == "2":
        decrypted = fernet.decrypt(file_data)
        with open(file_name, "wb") as file:
            file.write(decrypted)
        return decrypted

# Function for processing messages
def process_message(mode, message, key):
    fernet = Fernet(key)

    if mode == "3":
        return fernet.encrypt(message.encode('utf-8'))
    elif mode == "4":
        return fernet.decrypt(message.encode('utf-8'))

# Function for encrypting a folder
def encrypt_folder(folder_path, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypted = process_file("1", file_path, key)
            print(f"Encrypted {file_path}: {encrypted.decode('utf-8')}")

# Function for decrypting a folder
def decrypt_folder(folder_path, key):
    fernet = Fernet(key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypted = process_file("2", file_path, key)
            print(f"Decrypted {file_path}: {decrypted.decode('utf-8')}")

# Generate and write a new key
write_key()

# Load generated key
key = load_key()
#prints key
print("Your key is: " + str(key.decode('utf-8')))

# Main loop
while True:
    display_menu()
    mode = input("Please select a mode: \n")

    if mode in ["1", "2"]: #checks if mode is 1 or 2 from previous input
        file_name = input("Enter file name: ") #asks for file name
        processed_data = process_file(mode, file_name, key) #stores process_file function into processed_data
        if mode == "1":
            print("Encrypted message is: " + processed_data.decode('utf-8'))
        elif mode == "2":
            print("Decrypted message is: " + processed_data.decode('utf-8'))

    elif mode in ["3", "4"]: #checks if mode is 3 or 4 from previous input
        message = input("Enter message: ") #asks for a message
        processed_data = process_message(mode, message, key) #stores process_message function into processed_data
        if mode == "3":
            print("Encrypted message is: " + processed_data.decode('utf-8'))
                # ... (message processing continued)
        elif mode == "4":
            print("Decrypted message is: " + processed_data.decode('utf-8'))

    elif mode == "5":
        folder_path = input("Enter folder path to encrypt: ") #asks for a folder path
        encrypt_folder(folder_path, key) #calls on function and encrypts folder and its contents

    elif mode == "6":
        folder_path = input("Enter folder path to decrypt: ") #asks for a folder path
        decrypt_folder(folder_path, key)#calls on function and decrypts folder and its contents

    elif mode == "7":
        exit()
    else:
        print(f"""
You entered {mode}
That is an invalid input.
Please input a number between 1 and 7.
""")
        time.sleep(2)
        

