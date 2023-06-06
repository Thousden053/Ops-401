#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt

import subprocess

def banner_grabbing_with_netcat(target, port):
    try:
        result = subprocess.check_output(['nc', '-v', target, str(port)], stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to perform banner grabbing with netcat: {e.output.decode()}")

def banner_grabbing_with_telnet(target, port):
    try:
        result = subprocess.check_output(['telnet', target, str(port)], stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to perform banner grabbing with telnet: {e.output.decode()}")

def banner_grabbing_with_nmap(target):
    try:
        result = subprocess.check_output(['nmap', '-p-', '-sV', target], stderr=subprocess.STDOUT, timeout=10)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(f"Failed to perform banner grabbing with Nmap: {e.output.decode()}")

# Prompt for URL or IP address
target_address = input("Enter a URL or IP address: ")

# Prompt for port number
port_number = int(input("Enter a port number: "))

# Perform banner grabbing with netcat
print("Performing banner grabbing with netcat...")
banner_grabbing_with_netcat(target_address, port_number)

# Perform banner grabbing with telnet
print("Performing banner grabbing with telnet...")
banner_grabbing_with_telnet(target_address, port_number)

# Perform banner grabbing with Nmap
print("Performing banner grabbing with Nmap...")
banner_grabbing_with_nmap(target_address)
