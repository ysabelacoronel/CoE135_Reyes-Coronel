import sqlite3
from seller import Seller
from items import Items
from sold import Sold
from buyer import Buyer

conn1 = sqlite3.connect('seller.db')
conn2 = sqlite3.connect('items.db')
conn3 = sqlite3.connect('sold.db')
conn4 = sqlite3.connect('buyer.db')

c1 = conn1.cursor()
c2 = conn2.cursor()
c3 = conn3.cursor()
c4 = conn4.cursor()


# item checker
def Item(prod, username):
    chk = 0
    exist = find_item(prod)
    if exist == []:
        chk = 1
    else:
        i = 0
        dum = len(exist)
        while i < dum:
            i +=1
            if exist[i-1][3] == username:
                chk = 0
                break
        else:
            chk = 1
    return chk

# username checker
def saccount(username):
    chk = 0
    exist = get_seller_by_name(username)
    if exist == []:
        chk = 1
    return chk

# username checker
def baccount(username):
    chk = 0
    exist = get_buyer_by_name(username)
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

####################
# Buyer functions #
####################

def insert_buyer(buyr):
    with conn4:
        c4.execute("INSERT INTO Buyers VALUES (:username)", {'username': buyr.username})

def get_buyer_by_name(name):
    c4.execute("SELECT * FROM Buyers WHERE username=:username", {'username': name})
    return c4.fetchall()

#def remove_buyer(buyr):

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

#######################
# Sold Item Functions #
#######################

def sold_item(prod, php, qty, sllr, byer):
    with conn3:
        c3.execute("INSERT INTO SoldItems VALUES (:item_name, :price, :quantity, :seller, :buyer)", {'item_name': prod, 'price': php, 'quantity': qty, 'seller':sllr, 'buyer':byer})

def find_solditem(prod,sllr):
    c3.execute("SELECT * FROM SoldItems WHERE item_name=:item_name AND seller=:seller", {'item_name': prod, 'seller': sllr})
    return c3.fetchall()

def update_quantity(prod, newq, sllr):
    with conn3:
        c3.execute("""UPDATE SoldItems SET quantity = :quantity
                    WHERE item_name = :item_name AND seller = :seller""",
                  {'item_name': prod, 'seller': sllr, 'quantity': newq})

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
            chk = saccount(username)

            if chk == 1:
                print('Username does not exist.')
            else:
                print('Hello', username, '!\n')
                correct2 = 1
        elif seller == '2':
            username = input('Enter username: ')
            chk = saccount(username)
            if chk == 1:
                dummy_seller = Seller(username)
                insert_seller(dummy_seller)
                print('Hello', username, '!\n')
                correct2 = 1
            else:	
                print('Username exists already.')
        else:
            print('Error: Incorrect input.')

    # OPTIONS
    
    while 1:
        option = input('A: Marketplace\nB: Auctions\nC: View Sold Items\nD: Messages\nE: Exit Program\n')
        
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
                    c2.execute("SELECT * FROM Items WHERE seller= :seller", {'seller':username})
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
            print('Welcome to SOLD ITEMS')        
            c3.execute("SELECT * FROM SoldItems WHERE seller= :seller", {'seller':username})
            results = c3.fetchall()
            num_items = len(results)
            print("Item Name - Quantity")
            i = 0
            while i < num_items:
                i +=1
                print("{} - {}".format(results[i-1][0], results[i-1][2]))

        elif option == 'D':
            print('Welcome to MESSAGES')
        elif option == 'E':
            exit('Goodbye')
        else:
            print('Invalid Input.')

#################
# Buyer Program #
#################

def buyer():
    
    # loading and creating an account
    correct2 = 0
    while correct2 == 0:
        buyer = input('Options:\n1: Load existing account\n2: Create a new one\n')
        if buyer == '1':
            username = input('Enter username: ')
            chk = baccount(username)

            if chk == 1:
                print('Username does not exist.')
            else:
                print('Hello', username, '!\n')
                correct2 = 1
        elif buyer == '2':
            username = input('Enter username: ')
            chk = baccount(username)
            if chk == 1:
                dummy_buyer = Buyer(username)
                insert_buyer(dummy_buyer)
                print('Hello', username, '!\n')
                correct2 = 1
            else:	
                print('Username exists already.')
        else:
            print('Error: Incorrect input.')

    # OPTIONS
    
    while 1:
        option = input('A: Marketplace\nB: Auctions\nC: View all Purchases\nD: Messages\nE: Exit Program\n')
        
        if option == 'A':
			# marketplace            
            checker = 0
            market = input('Options:\n1: View all items\n2: View all sellers\n3: Back\n')
            while checker == 0:
                if market == '1':
                    print('Viewing all items')
                    i = 0
                    c2.execute("SELECT * FROM Items")
                    results = c2.fetchall()
                    num_items = len(results)
                    print("Item name\t-----\tPrice - Stock")
                    while i < num_items:
                        i +=1
                        print("{}. {}\t-----\t{} - {}".format(i, results[i-1][0],results[i-1][1], results[i-1][2]))
                    buy = int(input("Enter number of item: "))
                    print("before")
                    
                    # updating stock
                    newstock = results[buy-1][2] - 1
                    update_stock(results[buy-1][0], newstock, results[buy-1][3])
                    
                    # adding to database of sold items
                    check = find_solditem(results[buy-1][0], results[buy-1][3])
                    if check == []:
                        sold_item(results[buy-1][0], results[buy-1][1], 1, results[buy-1][3], username)
                    else:
                        newq = check[0][2] + 1
                        update_quantity(results[buy-1][0], newq, results[buy-1][3])

                    c2.execute("SELECT * FROM Items WHERE item_name=:item_name AND seller=:seller", {'item_name': results[buy-1][0], 'seller': results[buy-1][3]})     
                    results = c2.fetchall()               
                    print(results)
                    checker = 1    

                elif  market == '2':
                    print('Viewing all sellers')
                    i = 0
                    c1.execute("SELECT * FROM Sellers")
                    results = c1.fetchall()
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
            print('Welcome to Purchases')
            c3.execute("SELECT * FROM SoldItems WHERE buyer:=buyer", {'buyer': username})
            results = c3.fetchall()
            num_items = len(results)
            print("Item Name - Quantity")
            i = 0
            while i < num_items:
                i +=1
                print("{} - {}".format(results[i-1][0], results[i-1][2]))

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
		buyer()
		correct1 = 1
	elif user == 'seller':
		seller()
		correct1 = 1
	else:
		print('Error: Incorrect input.')

print('end')
