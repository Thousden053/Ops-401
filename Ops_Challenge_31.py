#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt


import os
import platform

def search_files(file_name, directory):
    total_files_searched = 0
    total_hits = 0

    # Get the operating system name
    operating_system = platform.system()

    for root, _, files in os.walk(directory):
        for file in files:
            # Perform case-insensitive search
            if file_name.lower() in file.lower():
                file_path = os.path.join(root, file)
                print(f"Found: {file_path}")
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
