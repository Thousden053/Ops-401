#!/usr/bin/python3

#Tyler Housden

#utilized chatgpt


import sys
import argparse
import socket
from scapy.all import sr1, IP, TCP

def ping(host):
    try:
        socket.inet_aton(host)
    except socket.error:
        print(f"Invalid IP address: {host}")
        return False

    response = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)

    if response is None:
        print(f"Host {host} is not responding to pings")
        return False

    print(f"Host {host} is up")
    return True

def scan_ports(host):
    port_range = range(1, 1025)

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP Port Scanner with Ping")
    parser.add_argument("host", help="IP address of the host to scan")
    args = parser.parse_args()

    if ping(args.host):
        scan_ports(args.host)
