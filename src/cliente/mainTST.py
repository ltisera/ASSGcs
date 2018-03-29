import os
import select
import socket
import wx
import queue
from threading import Thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
global s 

class conectarCliente(Thread):
	def __init__(self, app):
		Thread.__init__(self)
		self.laaplicacion = app
		self.Set_Daemon = True
		self.sacarhilo = False
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.connect((TCP_IP, TCP_PORT))
			self.s.setblocking(0)
			self.inputs =[self.s]
			self.outputs = []
			self.excepciones =[]
			self.envidato = ""
			self.start()
		except:
			print("ERROR DECON")
		
	def isConectado(self):
		return False

	def run(self):
		while self.inputs:
			if(self.sacarhilo == False):
				try:
					entradas, salidas, excepciones = select.select(self.inputs,self.outputs,[],2)
					for s in entradas:
						print("Preparando recepcion")
						dato = s.recv(2048)
						print("Recibi del sv: ", dato.decode())
						if (dato.decode() == "sali"):
							self.inputs.remove(s)
						if (dato.decode() == ""):
							print("VACIO")
							self.inputs.remove(s)
						
							

					for s in salidas:
						s.send(self.envidato.encode())
						print("Envie: ", self.envidato)
						self.outputs.remove(s)

					
				except:
					print("fuck an EXceoT")		
					a=input()
			else:
				("sacarhilo")
				break
		s.close()
		self.laaplicacion.conected = None
		print("Muerte del proceso")

	def cerrarConexion(self):
		self.sacarhilo = True

	def enviarDato(self, dato):
		print("Preparando envidato")
		self.envidato = dato
		self.outputs.append(self.s)
		
class myApp(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self,parent=parent,title=title,size=(400,200))

		self.conected = None
		p1 = wx.Panel(self, -1)
		sz = wx.BoxSizer(wx.VERTICAL)
		

		c1 = wx.BoxSizer(wx.VERTICAL)
		
		sz.Add(p1, 1, wx.EXPAND)

		self.SetSizer(sz)
		p1.SetSizer(c1)

		self.text = wx.TextCtrl(p1, -1, "JET")
		self.tIP = wx.TextCtrl(p1, -1, "127.0.0.1")
		
		self.boton = wx.Button(p1, -1, "Co&nectar")
		self.bsend = wx.Button(p1,-1, "Envidata")
		c1.Add(self.text, 1, wx.CENTER)
		c1.Add(self.boton, 0, wx.CENTER)
		c1.Add(self.bsend, 0, wx.CENTER)

		self.Bind(wx.EVT_BUTTON, self.clckOnConectar)
		self.Bind(wx.EVT_BUTTON, self.onSend, self.bsend)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Show()


	def onSend(self, event):
		if(self.conected != None):
			self.conected.enviarDato(self.text.GetValue())
			self.text.SetValue("")
		else:
			print("El cliente no esta conectado a un servidor")


	def onClose(self, event):
		if(self.conected != None):
			self.conected.cerrarConexion()
		print("Cerrado bien")
		self.Destroy()


	def clckOnConectar(self, event):
		if(self.conected == None):
			self.conected = conectarCliente(self)
		else:
			print("el cliente ya esta conectado a un server")

if __name__ == '__main__':
	s = -1
	app = wx.App(False)
	frame = myApp(None, "Assg Server")
	app.MainLoop()

