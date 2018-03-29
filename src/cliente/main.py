import os
import socket

IDCliente = 1
os.system("cls")


print("Hola, soy el cliente:", IDCliente)



TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "solo puedo enviar 20 y que pasa si enviamos una banda mas".encode()

print("Inicidando el cliente")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.setblocking(0)
dato = "".encode()
print("ACA 1")
print("listo y preparado")
#dato = s.recv(BUFFER_SIZE)
print(dato.decode())
	
while(dato.decode()!="sali"):
	MESSAGE = input("Enviar ->")
	if(MESSAGE != ""):
		print("enviando: " + str(MESSAGE))	
		s.send(MESSAGE.encode())
		dato = s.recv(BUFFER_SIZE)
		print("Recibi: ", dato.decode())
	else:
		print ("Imposible enviar mensaje vacio")

#s.send("sali".encode())
#dato = s.recv(BUFFER_SIZE)
s.close()
print ("received dato:" + str(dato.decode()))