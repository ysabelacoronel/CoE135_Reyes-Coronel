import socket

def seller():
	print("Seller here")
	host = socket.gethostname()
	port = 8080
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	message = s.recv(1024)
	print(message.decode("utf-8")) 

	


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
