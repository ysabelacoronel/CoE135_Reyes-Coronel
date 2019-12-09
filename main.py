import sqlite3
from seller import Seller
from items import Items

conn1 = sqlite3.connect('seller.db')
conn2 = sqlite3.connect('items.db')
c1 = conn1.cursor()
c2 = conn2.cursor()

list_of_items = []
list_of_sellers = []

# item checker
def Item(prod, username):
    chk = 0
    exist = find_item(prod)
    print(exist)
    if exist == []:
        chk = 1
    else:
        i = 0
        dum = len(exist)
        while i < dum:
            i +=1
            if exist[i][3] == username:
                chk = 0
                break
        else:
            chk = 1
    return chk

# username checker
def account(username):
    chk = 0
    exist = get_seller_by_name(username)
    if exist == []:
        chk = 1
    return chk

####################
# Seller functions #
####################

def insert_seller(sllr):
    with conn1:
        c1.execute("INSERT INTO Sellers VALUES (:username)", {'username': sllr.username})

def get_seller_by_name(name):
    c1.execute("SELECT * FROM Sellers WHERE username=:username", {'username': name})
    return c1.fetchall()

def remove_seller(sllr):
    with conn1:
        c1.execute("DELETE from Sellers WHERE username = :username",
                  {'username': sllr.username})

##################
# Item Functions #
##################

def insert_item(prod):
    with conn2:
        c2.execute("INSERT INTO Items VALUES (:item_name, :price, :stock, :seller)", {'item_name': prod.item_name, 'price': prod.price, 'stock': prod.stock, 'seller':prod.seller})

def find_item(prod):
    c2.execute("SELECT * FROM Items WHERE item_name=:item_name", {'item_name': prod})
    return c2.fetchall()

def update_stock(prod, new_stock, sllr):
    with conn2:
        c2.execute("""UPDATE Items SET stock = :stock
                    WHERE item_name = :item_name AND seller = :seller""",
                  {'item_name': prod, 'seller': sllr, 'stock': new_stock})

def remove_item(prod):
    with conn2:
        c2.execute("DELETE from Items WHERE item_name = :item_name",
                  {'item_name': prod})

##################
# Seller program #
##################

def seller():
    print('Hello SELLER!')
    
    # loading and creating an account
    correct2 = 0
    while correct2 == 0:
        seller = input('Options:\n1: Load existing account\n2: Create a new one\n')
        if seller == '1':
            username = input('Enter username: ')
            chk = account(username)

            if chk == 1:
                print('Username does not exist.')
            else:
                print('Hello', username)
                correct2 = 1
        elif seller == '2':
            username = input('Enter username: ')
            chk = account(username)
            if chk == 1:
                dummy_seller = Seller(username)
                insert_seller(dummy_seller)
                correct2 = 1
            else:	
                print('Username exists already.')
        else:
            print('Error: Incorrect input.')

    # OPTIONS
    
    while 1:
        option = input('A: Marketplace\nB: Auctions\nC: Items\nD: Messages\nE: Exit Program\n')
        
        if option == 'A':
			# marketplace            
            checker = 0
            market = input('Options:\n1: Post new item\n2: View all items\n3: Back\n')
            while checker == 0:
                if market == '1':
                    print('Posting new item')
                    newitem = input("Enter New Item: ")

                    pexist = Item(newitem, username)
                    if pexist == 0:
                        inp = input("Item exists already, do you want to update stock? Y or N ")
                        if inp == 'Y':
                            newstock = input("New Stock: ")
                            update_stock(newitem, newstock, username)
                            item = find_item(newitem)
                            print(item)
                    else:
                        newstock = input("Stock: ")
                        newprice = input("Price: ")
                        dummy_item = Items(newitem, newprice, newstock, username)
                        insert_item(dummy_item) 

                    checker = 1
                elif  market == '2':
                    print('Viewing all items')
                    i = 0
                    c2.execute("select * from Items")
                    results = c2.fetchall()
                    num_items = len(results)
                    while i < num_items:
                        i +=1
                        print(results[i-1][0])
                    checker = 1
                elif market == '3':
                    checker = 1
                else:
                    print('Invalid input')
                    
        elif option == 'B':
            print('Welcome to AUCTIONS')
        elif option == 'C':
            print('Welcome to ITEMS')
        elif option == 'D':
            print('Welcome to MESSAGES')
        elif option == 'E':
            exit('Goodbye')
        else:
            print('Invalid Input.')


################
# MAIN PROGRAM #
################

print('MAIN PROGRAM TEST')

c1.execute("select * from Sellers")
results = c1.fetchall()
num_sellers = len(results)

c2.execute("select * from Items")
results = c2.fetchall()
num_items = len(results)

# Buyer or Seller
correct1 = 0
while correct1 == 0:
	user = input("Buyer or Seller? ")
	if user == 'buyer':
		#buyer()
		correct1 = 1
	elif user == 'seller':
		seller()
		correct1 = 1
	else:
		print('Error: Incorrect input.')

print('end')
