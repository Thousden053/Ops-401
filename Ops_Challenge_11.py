#!/usr/bin/python3

#Tyler Housden


import sys
from scapy.all import sr1, IP, TCP

host = "192.168.1.1" # define the IP address of the host to scan
port_range = range(1, 1025) # define the range of ports to scan

for dst_port in port_range:
    src_port = 1025
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

    if response is None:
        print(f"Port {dst_port} is filtered or host is not responding")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port, flags="R"), timeout=1, verbose=0)
        print(f"Port {dst_port} is open")
    elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
        print(f"Port {dst_port} is closed")
    else:
        print(f"Port {dst_port} has an unknown response")
