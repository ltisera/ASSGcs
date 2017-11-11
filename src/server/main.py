
import socket

print("Inicializando servidor...")

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
print("Configurando IP:" + str(TCP_IP))
print("Configurando Puerto:" + str(TCP_PORT))
print("Configurando Buffer:" + str(BUFFER_SIZE))



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("creando socket" + str(s))
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)

while 1:
	print ("Que onda")
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print ("received data:", data)
	conn.send(data)  # echo
print("Saliendo")
conn.close()