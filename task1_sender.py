import socket
import sys

argc = len(sys.argv)

if argc != 3:
    print("Usage: python3 task1_sender.py <IP address> <port number>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])

# Construct ICMP socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP) # AF_INET = IPv4, SOCK_RAW = raw socket, IPPROTO_ICMP = ICMP

s.connect((ip, port)) # Bind to port 0, which means any available port

while True:
    message = input("Enter message to send the reicever: ")

    # Encrypt with AES-GCM
    # TODO

    # Send the message
    
    print(f"Sending the following message to {ip}:{port}\n{message}")

    s.send(message.encode())