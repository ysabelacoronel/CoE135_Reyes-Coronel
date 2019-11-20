def seller():
	print("Seller here")

def buyer():
	print("Buyer here")

# main program
print ('Welcome to MARKETPLACE')
print ('What will you be?')

input_ = raw_input("seller or buyer? \n")
print(input_)

if input_== 'seller':
	print("I'm a seller")
	seller()
elif input_ == 'buyer':
	print("I'm a buyer")
	buyer()
else:
	print("I'm no one. Bye")
