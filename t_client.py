# test client for private messaging

import socket
import select
import sys

def input_():
    sys.stdout.write("SELLER: ")
    sys.stdout.flush()

socklist = []
host = socket.gethostname()
port = 8080

# socket creation and binding
seller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
seller.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
seller.connect((host, port))

try:
    socklist.append(seller)
    socklist.append(sys.stdin)

    seller_name = "Poopoo"
    seller.send(seller_name.encode())

    resp = seller.recv(1024)
    resp = resp.decode()
    print("BUYER: " + resp)

    buyer_name = seller.recv(1024).decode()
    resp = "Hello " + buyer_name + "!"
    seller.send(resp.encode())

    stay = 0
    while stay == 0:
        read, write, err = select.select(socklist, [], [])
        for sock in read:
            if sock == seller:
                data = sock.recv(1024).decode()
                if not data:
                    print("\nBuyer left the chat")
                    print("Bye!")
                    quit()
                    stay = 1
                else:
                    print('\r' + data)
                    input_()
            elif sock == sys.stdin:
                resp = sys.stdin.readline()
                resp = "\rSELLER: " + resp
                if seller.send(resp.encode()):
                    input_()
                    stay = 0
            else:
                pass


except KeyboardInterrupt:
    print("Bye")
    resp = "q"
    seller.send(resp.encode())
    stay = 1
    quit()
    seller.close()
