# initial main options. choosing if buyer or seller
# problem: 
# 1. Wont take other form of user input. will only accept form indicated in ifelse statement. 
# 2. Not sure if enough error checking. Already checked if input is 'buyer', 'seller', or none. 
# 3. Neverending loop of getting user input if choice is none of the listed choices. 
# 4. Added option to load a user 


# username checker
def account(username):
	f = open("accounts.txt", "r")
	f1 = f.read().splitlines()
	chk = 0
	for x in f1:
		if username == x:
			chk = 1
	f.close()
	return chk
		

# Seller program 
def seller():
	print('Hello SELLER!')

	# loading and creating an account
	correct = 0
	while correct == 0:
		seller = input('Options:\n1: Load existing account\n2: Create a new one\n')
		if seller == '1':
			username = input('Enter username: ')
			print(username)
			chk = account(username)
			if chk == 1:
				print('Hello', username)
				correct = 1
			else:
				print('Username does not exist.')
		elif seller == '2':
			username = input('Enter username: ')
			chk = account(username)
			if chk == 1:
				print('Username exists already.')
			else:	
				print('Hello', username)
				f = open("accounts.txt", "a+")
				f.write(username)	
				correct = 1		
		else:
			print('Error: Incorrect input.')

	option = input('A: Marketplace\nB: Auctions\nC: Items\nD: Messages\nE: Exit Program\n')
			


def buyer():
	print('Hello BUYER!')
		
	

print('Welcome to the MARKETPLACE!')
correct = 0;
while correct == 0:
	user = input("Buyer or Seller? ")
	if user == 'buyer':
		buyer()
		correct = 1
	elif user == 'seller':
		seller()
		correct = 1
	else:
		print('Error: Incorrect input.')

print('end')
