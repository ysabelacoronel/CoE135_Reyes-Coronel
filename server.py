import socket
import sys
import traceback
from threading import Thread

def main():
	server()

def server():
	host = socket.gethostbyname(socket.gethostname())
	port = 8080
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	try:
		s.bind(host, port)
	except:
		print("Bind failed")
		sys.exit()

	s.listen(10)
	print("Waiting for connections...")

	while 1:
		conn, addr = s.accept()
		ip, port = str(addr[0]), str(addr[1])
		print(ip + ":" + port + "connected to MARKETPLACE")

	try:
		Thread(target = client_thread, args = (conn, ip, port)).start()
	except:
		print("Error in creating thread")
		traceback.print_exc()
	s.close()

def clientThread(conn, ip, port, buff_size = 5120):
	active = True
	while active:
		client_input = receive_input(conn, buff_size)
		if "q" in client_input:
			print(ip + ":" port + "exiting")
			conn.close()
			print(ip + ":" port + "left the MARKETPLACE")
			active = False
		else:
			

