"""
La lista clientesOnline
{socket, cliente addres, ID Cliente}
"""


#Aca quiero poner la gestion del thread del server
from threading import Thread
import select
import os
import socket
import wx
import random
import queue

from genera import generarID
class conectarServer(Thread):
	def __init__(self,tInformacion, cListaClientes, dir_ip, app):
		Thread.__init__(self)
		self.tinf = tInformacion
		self.tinf.SetValue("Inicializando servidor..")
		self.cClientes = cListaClientes
		self.TCP_IP = dir_ip
		self.TCP_PORT = 5005
		self.appapp = app
		self.clientesOnline = []
		BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
		
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server.setblocking(0)
		self.server.bind((self.TCP_IP, self.TCP_PORT))
		self.server.listen(5)

		self.cola_mensajes = {}

		
		self.inputs= [self.server]
		self.outputs = []
		self.setDaemon(True)
		self.tinf.AppendText("\nDEMONIO")
		self.lSock = [self.server] # Lista de sockets (1 para cada cliente)
		
		app.boton.SetLabel("Cerrar")

		self.start()

		

	def run(self):
		
		
		self.tinf.AppendText("\nEjecutando run como DEMONIO")

		while self.inputs:
			try:
				
				lecturas, escrituras, excepciones = select.select(self.inputs,self.outputs,self.inputs,1)
				for s in lecturas:
					if(s is self.server):
						scliente, caddres = s.accept()
						print("Nueva conexion")
						print("POR ENVIAR")
						scliente.sendall("Bien".encode())
						print("enviadaso")
						elementoLista=[]
						elementoLista.append(scliente)
						elementoLista.append(caddres)
						elementoLista.append(generarID(self.clientesOnline))
						print(elementoLista)
						self.clientesOnline.append(elementoLista)
						scliente.setblocking(0)
						self.inputs.append(scliente)
						self.cola_mensajes[scliente] = queue.Queue()
						self.appapp.list.Insert(str(elementoLista[2]),0)
						
					else:
						data = s.recv(1024)

						if data:
							print("Recibi del cliente: ", data)
							self.cola_mensajes[s].put(data)
							if(s not in self.outputs):
								self.outputs.append(s)
							
						else:
							if(s in self.outputs):
								self.outputs.remove(s)
							self.inputs.remove(s)
							print("sacando bien")
							self.sacarCliente(s)
							"""
							for i in self.clientesOnline:
								if s in i:
									citem = 0
									for citem in range(self.appapp.list.GetCount()):
										print ("citem: ",citem, " Tengo: ", int(self.appapp.list.GetString(citem)))
										print("Contra: ", i[2])
										if (int(self.appapp.list.GetString(citem)) == i[2] ):
											print("Removiendo del list")
											self.appapp.list.Delete(citem)
											print("Removido A")
											break
									print("Remover de clientes")
									self.clientesOnline.remove(i)
									print("Removido B")

							s.close()
							"""
							print("cliente Cerrado")
							print (self.clientesOnline)

							del self.cola_mensajes[s]
				
				for s in escrituras:
					try:
						next_msg = self.cola_mensajes[s].get_nowait()
					except queue.Empty:
						print("No hay mas mensajes en cola")
						self.outputs.remove(s)
					else:
						print("Escribiremos: ", next_msg)
						s.sendall(next_msg)
						print("enviado")
						if(next_msg.decode() == "El servidor te Kickea por gato"):
							s.close()
							if (s in self.outputs):
								self.outputs.remove(s)

				for s in excepciones:
					print("Tengo un E")
					self.inputs.remove(s)
					if (s in self.outputs):
						self.outputs.remove(s)
					s.close()
					del self.cola_mensajes[s]
			except:
				for i in self.clientesOnline:
					if s in i:
						print("El cliente ", i[2], " a Cerrado la conexion de forma inesperada")
						citem = 0
						for citem in range(self.appapp.list.GetCount()):
							#esto deberia arrojar una excepcion en caso de que el cliente no este en la LISTA
							if (int(self.appapp.list.GetString(citem)) == i[2] ):
								self.appapp.list.Delete(citem)
								break
						print("sacando con excepcion")
						self.sacarCliente(s)		
						#self.clientesOnline.remove(i)
						#s.close()
						#self.inputs.remove(s)

					else:
						if  self.clientesOnline.index(i) >= len(self.clientesOnline):
							print("Len: ",len(self.clientesOnline), "  Indice: ", self.clientesOnline.index(i))
							print("ERROR 99999: Fuckkk an error unreconoced")

				print("Se cayo el cliente")
			

	def sacarCliente(self, sock):
		for s in self.clientesOnline:
			if sock in s:
				citem = 0
				for citem in range(self.appapp.list.GetCount()):
					if(int(self.appapp.list.GetString(citem)) == s[2]):
						self.appapp.list.Delete(citem)
						break
			print("Saco Cliente")
			self.clientesOnline.remove(s)
			sock.close()
			if(sock in self.inputs):
				self.inputs.remove(sock)
			if(sock in self.outputs):
				self.outputs.remove(sock)
			break

		pass

	def cualEsMiIp(self):
		return self.TCP_IP
	
	def obtenerCliente(self,ID):
		print("me pide el ID: ", ID, "y tengo ", len(self.clientesOnline), " clientes")

		for i in self.clientesOnline:
			print ("tengo ",i[2]," y comparo con: ", ID)
			if(ID == i[2]):
				print("Devuelvo cliente con ID: ", i[2])
				return i
		return -1

	def enviarDato(self,dato,destino):
		print("Forzando dato")
		self.cola_mensajes[destino].put(dato.encode())
		if(destino not in self.outputs):
			self.outputs.append(destino)

