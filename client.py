# Python program to implement client side of chat room.
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:

	read_sockets = select.select([server], [], [], 1)[0]
	import msvcrt
	if msvcrt.kbhit(): read_sockets.append(sys.stdin)

	#print ("antes del for")
	for socks in read_sockets:
		#print ("for: " + str(socks))
		if socks == server:
			message = socks.recv(2048)
			print ("<recibido>")
			print (message.decode('utf-8'))
		else:
			#orint("##menu princpal##")
			message = sys.stdin.readline()
			texto_a_enviar = message
			server.sendall(texto_a_enviar.encode('utf-8'))
			#server.sendall('true'.encode('utf-8'))
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()
server.close()
