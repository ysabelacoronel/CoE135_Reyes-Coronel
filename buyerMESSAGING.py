# Notes:
# - used separate text file for buyers, for easy checking
# - will use arbitrary inventory and sellers database for checking
# - serves as the server program for the private messaging
# - with interrupt handler in the pm and main program


import socket

# private messaging
def pm(username):
    host = socket.gethostname()
    port = 8080

    # socket creation and binding
    buyer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buyer.bind((host, port))

    # will accept only one connection
    buyer.listen(1)
    print("Waiting for seller...")

    conn, addr = buyer.accept()
    print("Got a connection from " + str(addr))

    try:
        seller_name = conn.recv(1024).decode()
        resp = "Hello " + seller_name + "!"
        conn.send(resp.encode())

        conn.send(username.encode())

        resp = conn.recv(1024).decode()
        print(resp)

        stay = 0
        while stay == 0:
            print("Response: ", end = '')
            resp = input()
            if resp == "q":
                print("Bye!")
                conn.send(resp.encode())
                stay = 1
            elif resp == None:
                print("Bye!")
                stay = 1
            else:
                conn.send(resp.encode())

            data = conn.recv(1024).decode()    
            if data == "q":
                print("Seller left the chat")
                stay = 1
            # elif data == None:
            #     print("Seller left the chat")
            #     stay = 1
            # elif socket.error:
            #     print("Seller left the chat")
            #     stay = 1
            else:
                print("Seller:" + data)

        conn.close()
    except KeyboardInterrupt:
        print("Bye!")
        resp = "q"
        conn.send(resp.encode())
        conn.close()
        quit()

# username checker
def account(username):
	f = open("buyers_database.txt", "r")
	f1 = f.read().splitlines()
	chk = 0
	for x in f1:
		if username == x:
			chk = 1
	f.close()
	return chk

# buyer main function
def buyer():
    print("Hello BUYER!")

    # loading and creating an account
    correct = 0
    while correct == 0:
        buyer = input("Options: \n1: Load existing acccount\n2: Create a new one\n")
        
        if buyer == "1":
            buyer_username = input("Username: ")
            b_chk = account(buyer_username)

            # username check
            if b_chk == 1:
                print("Hello " + buyer_username + "!\n")
                correct = 1
            else:
                print("Username does not exist")
                correct = 0
        elif buyer == "2":
            buyer_username = input("Username: ")
            print(buyer_username)
            b_chk = account(buyer_username)

            # username availability check
            if b_chk != 1:
                print("Hello " + buyer_username + "!")
                f = open("buyers_database.txt","a+")
                f.write(buyer_username)
                f.close()
                correct = 1
            else:
                print("Username already exists")
                correct = 1
        else:
            print("Incorrect input")
            correct = 0
        
    stay = 0
    while stay == 0:
        # main options in buyer funtion
        print("Options: \n1: Marketplace\n2: Auction\n3: Purchases\n4: Private Messaging\n5: Exit program\n")
        option = input()
        # check option input from user
        if option == "1":
            print("Option: \n1: View all items\n2: View all sellers\n3: Back")
            m_opt = input()
                
            # check marketplace option
            if m_opt == "1":
                f = open("inventory.txt", "r")
                item = f.readline()
                print(item)
                stay = 0
        elif option == "2":
            print("Auctions available:")
            stay = 0
        elif option == "3":
            print("Purchased items:\n")
            f_name = buyer_username + '.txt'
            print(f_name)
            f = open(f_name, "r")
                
            # printing all contents of file
            line = f.readline()
            print(line)
            f.close()
            print('\n')
            stay = 0
        elif option == "4":
            print("PRIVATE MESSAGING")
            pm(buyer_username)
            stay = 0
        elif option == "5":
            print("Exiting program...")
            stay = 1

# main function
print('Welcome to the MARKETPLACE!')
correct = 0
while correct == 0:
    try:
        user = input("Buyer or Seller? ")
        if user == 'buyer' or user == 'Buyer':
            buyer()
            correct = 1
        elif user == 'seller' or user == 'Seller':
    #		seller()
            correct = 1
        else:
            print('Error: Incorrect input.')
    except KeyboardInterrupt:
        print("Bye!")
        quit()
