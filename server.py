import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(10)
print("Waiting for connections...")

while 1:
	client_sock, addr = s.accept()
	print('Got connection from ', addr)
	client_sock.send(("Welcome to the MARKETPLACE!"))
