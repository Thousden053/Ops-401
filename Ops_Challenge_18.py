#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt

import zipfile

def test_password(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except:
        return False

def brute_force(zip_file_path, wordlist_file_path):
    with zipfile.ZipFile(zip_file_path) as zip_file:
        with open(wordlist_file_path, 'r') as wordlist_file:
            for line in wordlist_file.readlines():
                password = line.strip('\n')
                success = test_password(zip_file, password)
                if success:
                    print(f'Password found: {password}')
                    return
    print('Password not found in the wordlist.')

# Replace these paths with the paths to your zip file and wordlist
zip_file_path = 'path/to/your/zip/file.zip'
wordlist_file_path = 'path/to/rockyou.txt'

brute_force(zip_file_path, wordlist_file_path)
