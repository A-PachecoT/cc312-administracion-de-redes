#!/usr/bin/env python

import socket,sys

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6789

socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_server.bind((SERVER_IP,SERVER_PORT))

print("[*] Servidor UDP escuchando en %s:%d" % (SERVER_IP,SERVER_PORT))

while True:
	data,address = socket_server.recvfrom(4096)
	socket_server.sendto("Soy el servidor aceptando conexiones...".encode(),address)
	data = data.strip()
	print("Mensaje %s recibido desde %s: ",data, address)

	try:
		response = "Hola %s" % sys.platform
	except Exception as e:
		response = "%s" % sys.exc_info()[0]
	
	print("Respuesta",response)
	
	socket_server.sendto(bytes(response,encoding='utf8'),address)
		
socket_server.close()
		
