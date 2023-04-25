#!/usr/bin/python3

#Tyler Housden

#My draft
# #import libraries
# from cryptography.fernet import Fernet

# # Declare Functions

# #Function for writing key.
# def write_key():
#     #generate key and save it to a file
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# # Function 
# def load_key():

#     #load key from file name key.key
#     return open("key.key", "rb").read()

# #generate and write a new key
# write_key()

# # #load generated key
# key = load_key()

# print("Your key is: " + str(key.decode('utf-8')))

# while True:
#     menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encyrpt a message", "4: Decrypt a message", "5: Exit"]
#     for i in menu:
#         print(i)
#     mode = input("Please select a mode: ")
#     if mode == "1" or mode == "2":
#         file_name = input("Enter file name: ")
#         if mode == "1":
#             file_name.encode()
#             print (f"Your message in plain text: {file_name}")
#             encryption = Fernet(key)
#             encrypted = encryption.encrypt(file_name)
#             print("Encrypted message is: " + encrypted.decode('utf-8'))
#         elif mode == "2":
#             file_name.encode()
#             print("Encrypted message is: " + file_name)
#             decryption = Fernet(key)
#             decrypted = decryption.decrypt(file_name)
#             print (f"Your message in plain text: {file_name}")
#     elif mode == "3" or mode == "4":
#         message = input("Enter message: ")
#         if mode == "3":
#             encryption = Fernet(key)
#             encrypted = encryption.encrypt(message)
#             print("Encrypted message is: " + encrypted.decode('utf-8'))
#         elif mode == "4":
#             decryption = Fernet(key)
#             decrypted = decryption.decrypt(message)
#             print("Decrypted message is " + decrypted.decode('utf-8'))
#     elif mode == "5":
#         exit()

# After I ran it through GPT, only to fix a small error.
# Still having troubles with decrypting



from cryptography.fernet import Fernet

# Declare Functions
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def display_menu():
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Exit"]
    for i in menu:
        print(i)

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

def process_message(mode, message, key):
    fernet = Fernet(key)
    if mode == "3":
        return fernet.encrypt(message.encode('utf-8'))
    elif mode == "4":
        return fernet.decrypt(message.encode('utf-8'))
    
    

# Generate and write a new key
write_key()
key = load_key()

print("Your key is: " + str(key.decode('utf-8')))

while True:
    display_menu()
    mode = input("Please select a mode: ")

    if mode in ["1", "2"]:
        file_name = input("Enter file name: ")
        processed_data = process_file(mode, file_name, key)
        if mode == "1":
            print("Encrypted message is: " + processed_data.decode('utf-8'))
        elif mode == "2":
            print("Decrypted message is: " + processed_data.decode('utf-8'))
    elif mode in ["3", "4"]:
        message = input("Enter message: ")
        processed_data = process_message(mode, message, key)
        if mode == "3":
            print("Encrypted message is: " + processed_data.decode('utf-8'))
        elif mode == "4":
            print("Decrypted message is: " + processed_data.decode('utf-8'))
    elif mode == "5":
        exit()

