# auction program before incorporating in the main eller program
# can handle mutilple client connection
# detects invalid bid
# can monitor number of clients connected
# can determine highest bidder


import socket
import sys
from _thread import *
import time

item = "ball"
price = 10
current_bid = price
host = socket.gethostname()
port = 8080
connlist= []

seller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
seller.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
seller.bind((host, port))

seller.listen(10)
print("Waiting for BIDDERS...")

def timer():
    sec = 300

    while sec > 0:
        m, s = divmod(sec, 60)
        timeleft = str(m).zfill(2) + ":" + str(s).zfill(2)
        print('\r' + timeleft)
        time.sleep(1)
        sec -= 1

def buyer_num(username, conn):
    num = len(connlist)

    return num

def bidder_thread(conn, addr, username):    
    global current_bid
    global highest_bid
    start_new_thread(buyer_num, (username, conn))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            print("Bidder " + username + " left the auction")
            connlist.remove(conn)
            num = buyer_num(username, conn)
            if num == 1:
                if int(current_bid) > int(price):
                    print("Item sold to " + highest_bid)

            break
        
        if int(data) > int(current_bid):
            current_bid = data
            highest_bid = username
            print("Bidder: " + highest_bid)
            data = username + " bids " + data
            for c in connlist:
                c.sendall(data.encode())
        elif int(data) < int(current_bid):
            data = "Invalid bid by " + username
            for c in connlist:
                c.sendall(data.encode())
        else:
            pass

        data = "Current bid is " + str(current_bid)
        for c in connlist:
            c.sendall(data.encode())

    conn.close()

while True:
    conn, addr = seller.accept()
    connlist.append(conn)
    print("Client with address " + str(addr) + " connected to the AUCTION")
    resp = "Welcome to the AUCTION of item: " + item + " with starting bid of " + str(price)
    conn.sendto(resp.encode(), addr)
    username = conn.recv(1024).decode()
    start_new_thread(bidder_thread, (conn, addr, username))
    num = buyer_num(username, conn)
    print("Number of buyers: ", num)

seller.close()
