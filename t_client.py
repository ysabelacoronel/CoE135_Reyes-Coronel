# test client for private messaging

import socket

host = socket.gethostname()
port = 8080

# socket creation and binding
seller = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
seller.connect((host, port))

seller_name = "Poopoo"
seller.send(seller_name.encode())

try:
    resp = seller.recv(1024)
    resp = resp.decode()
    print("Buyer: " + resp)

    buyer_name = seller.recv(1024).decode()
    resp = "Hello " + buyer_name + "!"
    seller.send(resp.encode())

    stay = 0
    while stay == 0:
        seller.setblocking(0)
        data = seller.recv(1024).decode()
        if data == "q":
            print("Buyer left the chat")
            quit()
        # elif socket.error:
        #     print("foo")s
        #     print("Buyer left the chat")
        #     stay = 1
        # elif data == None:
        #     print("Buyer left the chat")
        #     stay = 1
        # elif len(data) == 0:
        #     resp = input("Response: " , end = '')
        #     seller.send(resp.encode())
        else:
            print("Buyer: " + data)

        print("Response: ", end = '')
        resp = input()
        if resp == "q":
            print("Bye!")
            seller.send(resp.encode())
            stay = 1
        else:
            seller.send(resp.encode())

    seller.close()
except KeyboardInterrupt:
    print("Bye bitch")
    resp = "q"
    seller.send(resp.encode())
    quit()
    seller.close()
