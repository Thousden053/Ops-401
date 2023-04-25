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



# #import libraries
# from cryptography.fernet import Fernet

# # Declare Functions

# # Function for writing key.
# def write_key():
#     # Generate key and save it to a file
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# # Function for loading key
# def load_key():
#     # Load key from file named key.key
#     return open("key.key", "rb").read()

# # Generate and write a new key
# write_key()

# # Load generated key
# key = load_key()

# print("Your key is: " + str(key.decode('utf-8')))

# while True:
#     menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Exit"]
#     for i in menu:
#         print(i)
#     mode = input("Please select a mode: ")
#     if mode == "1" or mode == "2":
#         file_name = input("Enter file name: ")
#         if mode == "1":
#             with open(file_name, "rb") as file:
#                 file_data = file.read()
#             print (f"Your message in plain text: {file_data}")
#             encryption = Fernet(key)
#             encrypted = encryption.encrypt(file_data)
#             with open(file_name, "wb") as file:
#                 file.write(encrypted)
#             print("Encrypted message is: " + encrypted.decode('utf-8'))
#         elif mode == "2":
#             with open(file_name, "rb") as file:
#                 file_data = file.read()
#             print("Encrypted message is: " + file_data.decode('utf-8'))
#             decryption = Fernet(key)
#             decrypted = decryption.decrypt(file_data)
#             with open(file_name, "wb") as file:
#                 file.write(decrypted)
#             print (f"Your message in plain text: {decrypted.decode('utf-8')}")
#     elif mode == "3" or mode == "4":
#         message = input("Enter message: ")
#         if mode == "3":
#             encryption = Fernet(key)
#             encrypted = encryption.encrypt(message.encode('utf-8'))
#             print("Encrypted message is: " + encrypted.decode('utf-8'))
#         elif mode == "4":
#             decryption = Fernet(key)
#             decrypted = decryption.decrypt(message.encode('utf-8'))
#             print("Decrypted message is: " + decrypted.decode('utf-8'))
#     elif mode == "5":
#         exit()






# Stretch goal



#import libraries
from cryptography.fernet import Fernet
import tarfile

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

# Function for compression
def compress(file_name, archive_name): 
    with tarfile.open(archive_name, mode="w:gz") as tar:
        tar.add(file_name)
    tar.close()

def decompress(archive_name, output_folder):
    with tarfile.open(archive_name, mode="r:gz") as tar:
        tar.extractall()
    tar.close()


# Generate and write a new key
write_key()

# Load generated key
key = load_key()
showkey = input("Would you like to see the key? (y/n) ").lower()
if showkey == "y" or showkey == "yes":
    print("Your key is: " + str(key.decode('utf-8')))
else:
    pass

while True:
    menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Exit"]
    for i in menu:
        print(i)
    mode = input("Please select a mode: ")
    if mode == "1" or mode == "2":
        file_name = input("Enter file name: ")
        if mode == "1":
            with open(file_name, "rb") as file:
                file_data = file.read()
            print (f"Your message in plain text: {file_data}")
            encryption = Fernet(key)
            encrypted = encryption.encrypt(file_data)
            with open(file_name, "wb") as file:
                file.write(encrypted)
            print("Encrypted message is: " + encrypted.decode('utf-8'))
            compressfile = input("Would you like to compress the file? (y/n) ").lower()
            if compressfile == "y" or compressfile == "yes":
                compressname = input("Name the archive to be created:\n")
                compressname = compressname + ".tar.gz"
                compress(file_name,compressname)
        elif mode == "2":
            with open(file_name, "rb") as file:
                file_data = file.read()
            print("Encrypted message is: " + file_data.decode('utf-8'))
            decryption = Fernet(key)
            decrypted = decryption.decrypt(file_data)
            with open(file_name, "wb") as file:
                file.write(decrypted)
            print (f"Your message in plain text: {decrypted.decode('utf-8')}")
            decompressfile = input("Would you like to decompress the file? (y/n) ").lower()
            if decompressfile == "y" or decompressfile == "yes":
                decompressname = input("Name the archive to be created:\n")
                decompressname = compressname + ".tar.gz"
                decompress(decompressname)
    elif mode == "3" or mode == "4":
        message = input("Enter message: ")
        if mode == "3":
            encryption = Fernet(key)
            encrypted = encryption.encrypt(message.encode('utf-8'))
            print("Encrypted message is: " + encrypted.decode('utf-8'))
        elif mode == "4":
            decryption = Fernet(key)
            decrypted = decryption.decrypt(message.encode('utf-8'))
            print("Decrypted message is: " + decrypted.decode('utf-8'))
    elif mode == "5":
        exit()