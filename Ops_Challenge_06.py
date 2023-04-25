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



#import libraries
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

# Generate and write a new key
write_key()

# Load generated key
key = load_key()

print("Your key is: " + str(key.decode('utf-8')))

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
        elif mode == "2":
            with open(file_name, "rb") as file:
                file_data = file.read()
            print("Encrypted message is: " + file_data.decode('utf-8'))
            decryption = Fernet(key)
            decrypted = decryption.decrypt(file_data)
            with open(file_name, "wb") as file:
                file.write(decrypted)
            print (f"Your message in plain text: {decrypted.decode('utf-8')}")
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






# # Stretch goal
# #works, but is still in progress.


# import os
# import tarfile
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

# # Function for compression
# def compress(file_name, archive_name):
#     with tarfile.open(archive_name, mode="w:gz") as tar:
#         tar.add(file_name)

# # Function for decompression
# def decompress(file_name):
#     if file_name.endswith(".tar.gz"):
#         tar = tarfile.open(file_name, mode="r:gz")
#         tar.extractall()
#         tar.close()
#         print(f"Archive '{file_name}' decompressed.")
#     else:
#         print("Invalid file format. Please provide a '.tar.gz' file.")

# # Generate and write a new key
# write_key()

# # Load generated key
# key = load_key()

# print("Your key is: " + str(key.decode('utf-8')))

# while True:
#     menu = ["1: Encrypt a file", "2: Decrypt a file", "3: Encrypt a message", "4: Decrypt a message", "5: Compress a file", "6: Decompress a file", "7: Exit"]
#     for i in menu:
#         print(i)
#     mode = input("Please select a mode: ")
#     if mode == "1":
#         file_name = input("Enter file name: ")
#         encrypted_file_name = file_name + ".enc"
#         with open(file_name, "rb") as file:
#             file_data = file.read()
#         encryption = Fernet(key)
#         encrypted = encryption.encrypt(file_data)
#         with open(encrypted_file_name, "wb") as file:
#             file.write(encrypted)
#         print(f"Encrypted message is: {encrypted.decode('utf-8')}")
#         os.remove(file_name)
#         # compressfile = input("Would you like to compress the encrypted file? (y/n) ").lower()
#         # if compressfile == "y" or compressfile == "yes":
#         #     archive_name = input("Name the archive to be created:\n")
#         #     if not archive_name.endswith(".tar.gz"):
#         #         archive_name += ".tar.gz"
#         #     compress(encrypted_file_name, archive_name)
#         #     print(f"Encrypted file '{encrypted_file_name}' compressed into '{archive_name}'.")
#         #     os.remove(encrypted_file_name)

#     elif mode == "2":
#         counter = 0
#         while counter == 0:
#             encrypted_file_name = input("""
# Enter encrypted file name (with .enc extension):
# Type 'quit' to exit.\n""")
#             if encrypted_file_name.endswith(".enc"):
#                 counter = 1
#                 decrypted_file_name = encrypted_file_name[:-4]
#                 with open(encrypted_file_name, "rb") as file:
#                     file_data = file.read()
#                 decryption = Fernet(key)
#                 decrypted = decryption.decrypt(file_data)
#                 with open(decrypted_file_name, "wb") as file:
#                     file.write(decrypted)
#                 print(f"File '{encrypted_file_name}' decrypted and saved as '{decrypted_file_name}'.")
#                 # compressfile = input("Would you like to compress the decrypted file? (y/n) ").lower()
#                 # if compressfile == "y" or compressfile == "yes":
#                 #     archive_name = input("Name the archive to be created:\n")
#                 #     if not archive_name.endswith(".tar.gz"):
#                 #         archive_name += ".tar.gz"
#                 #     compress(decrypted_file_name, archive_name)
#                 #     print(f"Decrypted file '{decrypted_file_name}' compressed into '{archive_name}'.")
#                 #     os.remove(decrypted_file_name)
#                 # os.remove(encrypted_file_name)
#             elif encrypted_file_name == "quit":
#                 counter = 1
#             else:
#                 print("Invalid file format. Please provide a '.enc' file.")

#     elif mode == "3":
#         message = input("Enter message: ")
#         encryption = Fernet(key)
#         encrypted = encryption.encrypt(message.encode('utf-8'))
#         print(f"Encrypted message is: {encrypted.decode('utf-8')}")

#     elif mode == "4":
#         message = input("Enter encrypted message: ")
#         decryption = Fernet(key)
#         decrypted = decryption.decrypt(message.encode('utf-8'))
#         print(f"Decrypted message is: {decrypted.decode('utf-8')}")

#     elif mode == "5":
#         counter = 0
#         while counter == 0:
#             file_name = input("Enter file name: ")
#             archive_name = input("Name the archive to be created:\n")
#             if not archive_name.endswith(".tar.gz"):
#                 archive_name += ".tar.gz"
#                 compress(file_name, archive_name)
#                 print(f"File '{file_name}' compressed into '{archive_name}'.")
#                 os.remove(file_name)
#                 counter = 1
#             else:
#                 print("Invalid file format. Please provide a '.tar.gz' file.")

#     elif mode == "6":
#         counter = 0
#         while counter == 0:
#             file_name = input("Enter archive name (with .tar.gz extension): ")
#             if file_name.endswith(".tar.gz"):
#                 decompress(file_name)
#                 os.remove(file_name)
#                 counter = 1
#             else:
#                 print("Invalid file format. Please provide a '.tar.gz' file.")


#     elif mode == "7":
#         exit()

