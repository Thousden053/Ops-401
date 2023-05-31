#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt


import os
import platform
import hashlib
import time

def get_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        while chunk := file.read(8192):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def search_files(file_name, directory):
    total_files_searched = 0
    total_hits = 0

    # Get the operating system name
    operating_system = platform.system()

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Perform case-insensitive search
            if file_name.lower() in file.lower():
                timestamp = time.ctime(os.path.getmtime(file_path))
                file_size = os.path.getsize(file_path)
                md5_hash = get_md5(file_path)

                print(f"\nTimestamp: {timestamp}")
                print(f"File Name: {file}")
                print(f"File Size: {file_size} bytes")
                print(f"File Path: {file_path}")
                print(f"MD5 Hash: {md5_hash}")
                total_hits += 1

            total_files_searched += 1

    print(f"\nTotal files searched: {total_files_searched}")
    print(f"Total hits found: {total_hits}")

def main():
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    search_files(file_name, directory)

if __name__ == "__main__":
    main()
