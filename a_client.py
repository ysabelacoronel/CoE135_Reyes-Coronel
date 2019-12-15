# auction client program
# will be incorporated to buyer program
# can send and receive message from server

import socket
import sys
import select
from _thread import *

def input_():
    sys.stdout.write("BID > ")
    sys.stdout.flush()

socklist = []
host = socket.gethostname()
port = 8080

bidder = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bidder.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if bidder.connect((host, port)):
    print("Joined the AUCTION...")
    print("Ctrl + c to exit")

socklist.append(bidder)
socklist.append(sys.stdin)

print("Username > ", end = '')
username = input()
bidder.send(username.encode())

stay = 0
while stay == 0:
    read, write, err = select.select(socklist, [], [])
    for sock in read:
        if sock == bidder:
            data = sock.recv(1024).decode()
            if data == "1":
                print("Won the auction. Successfully bought the item.")
                stay = 1
            elif not data:
                print("Auction ended")
                stay = 1
            else:
                print('\r' + data)
                input_()
        elif sock == sys.stdin:
            bid = sys.stdin.readline()
            if bidder.send(bid.encode()):
                input_()
        else:
            print("Foo")

bidder.close()
