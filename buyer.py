# Notes:
# - used separate text file for buyers, for easy checking
# - will use arbitrary inventory and sellers database for checking
# - display list of purchase item: DONE (I think?? HAHAHAHA)

# private messaging


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
        else:
            print("Incorrect input")
        
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
                print("Private messaging...")
                pm(buyer_username)
                stay = 0
            elif option == "5":
                print("Exiting program...")
                stay = 1

# main function
print('Welcome to the MARKETPLACE!')
correct = 0
while correct == 0:
	user = input("Buyer or Seller? ")
	if user == 'buyer' or user == 'Buyer':
		buyer()
		correct = 1
	elif user == 'seller' or user == 'Seller':
#		seller()
		correct = 1
	else:
		print('Error: Incorrect input.')