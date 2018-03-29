from threading import Thread
import select
import os
import socket
import wx
import random
import queue

#Imports propios
from funciones import esIpValida
from funciones import datoValido
from genera import generarID
from mst import conectarServer

class MiApp(wx.Frame):

	def __init__(self,parent,title):

		wx.Frame.__init__(self, parent=parent, title=title, size=(800,600))

		#Paneles (GuI) de la app
		p1 = wx.Panel(self,-1)
		#BoxSizers
		sz = wx.BoxSizer(wx.HORIZONTAL)

		a1 = wx.BoxSizer(wx.VERTICAL)
		a2 = wx.BoxSizer(wx.VERTICAL)

		b1 = wx.BoxSizer(wx.HORIZONTAL)

		c1 = wx.BoxSizer(wx.HORIZONTAL)
		c2 = wx.BoxSizer(wx.HORIZONTAL)
		c3 = wx.BoxSizer(wx.HORIZONTAL)
		c4 = wx.BoxSizer(wx.HORIZONTAL)
		c5 = wx.BoxSizer(wx.HORIZONTAL)
		sz.Add(p1,1,wx.EXPAND)

		self.SetSizer(sz)
		p1.SetSizer(b1)
		b1.Add(a1,1,wx.EXPAND)
		b1.Add(a2,1,wx.EXPAND)

		#controles
		self.conec = -1 

		lControles = []
		self.stIP = wx.StaticText(p1,-1,"Direccion IP:")
		lControles.append(self.stIP)
		
		self.stPuerto = wx.StaticText(p1,-1,"Puerto:")
		lControles.append(self.stPuerto)

		self.stBuffer = wx.StaticText(p1,-1,"Buffer:")
		lControles.append(self.stBuffer)

		self.stAlgo = wx.StaticText(p1,-1,"Algo:")
		lControles.append(self.stAlgo)

		self.tIp = wx.TextCtrl(p1,-1, "127.0.0.1")
		lControles.append(self.tIp)

		self.tPuerto = wx.TextCtrl(p1,-1, "Ingrese socket")
		lControles.append(self.tPuerto)

		self.tBuffer = wx.TextCtrl(p1, -1, "Buffer Size")
		lControles.append(self.tBuffer)

		self.boton = wx.Button(p1, -1, "Co&nectar")
		lControles.append(self.boton)

		self.bAgregar = wx.Button(p1,-1,"Agregar")
		lControles.append(self.bAgregar)

		self.bSacar = wx.Button(p1,-1,"Sacar")
		lControles.append(self.bSacar)

		self.list = wx.ListBox(p1,-1,(0,0),(300,150))
		lControles.append(self.list)

		self.tConsola = wx.TextCtrl(p1,-1, "Aca va too",(0,0),(500,500), wx.TE_MULTILINE )
		
		self.tInformacion = wx.TextCtrl(p1, -1,"Informacion de socket",(0,0),(1,1), wx.TE_MULTILINE)
		
		#posicionado de controles en sizers
		for i in range(len(lControles)):
			lControles[i].Bind(wx.EVT_KEY_UP, self.onKeyPress)
		
		c1.Add(self.stIP,1,wx.CENTER)
		c1.Add(self.tIp, 1,wx.CENTER)
		a1.Add(c1)

		c2.Add(self.stPuerto, 1, wx.CENTER)
		c2.Add(self.tPuerto, 1, wx.CENTER)
		a1.Add(c2)

		c3.Add(self.stBuffer, 1, wx.CENTER)
		c3.Add(self.tBuffer, 1, wx.CENTER)
		a1.Add(c3)
		c4.Add(self.list, 1, wx.EXPAND)
		a1.Add(c4)
		a1.Add(self.tInformacion, 1, wx.EXPAND)
		a1.Add(self.boton)
		a1.Add(c5)
		
		c5.Add(self.bAgregar)
		c5.Add(self.bSacar)
		a2.Add(self.stAlgo)
		a2.Add(self.tConsola, 1)
		self.Center(True)


		#Conexiones de Controles
		self.Bind(wx.EVT_BUTTON, self.clckOnConnect)
		self.Bind(wx.EVT_BUTTON,self.clkOnAgregar,self.bAgregar)
		self.Bind(wx.EVT_BUTTON,self.clkOnSacar,self.bSacar)
		self.tIp.Bind(wx.EVT_CHAR, self.onKeyPress)
		self.Bind(wx.EVT_CHAR, self.onKeyPress)

		#Autoconeccion
		self.conec = conectarServer(self.tInformacion,self.list,str(self.tIp.GetValue()),self)

		self.Show()

	"""
	Cuando se preciona el boton sacar... Kickea al cliente
	y lo remueve de la lista
	"""
	def clkOnSacar(self, event):
		if(self.list.GetSelection() != -1):
			print(self.list.GetString(self.list.GetSelection()))
			print(self.conec.obtenerCliente(int(self.list.GetString(self.list.GetSelection()))))
			self.conec.enviarDato("El servidor te Kickea por gato", self.conec.obtenerCliente(int(self.list.GetString(self.list.GetSelection())))[0])
		
	def clkOnAgregar(self, event):
		print("click")
		self.list.Insert("Miauu",0) 
		pass
	#Valida las teclas que ingresan 
	def onKeyPress(self, event):
		kcode = event.GetKeyCode()
		if( kcode >= 48 and kcode <= 57 or
			kcode >= 314 and kcode <= 317 or
			kcode == 8 or
			kcode == 127 or
			kcode == 46
			):
			event.Skip()
		else:
			if(kcode == wx.WXK_ESCAPE):
				self.Close()
				
	def clckOnConnect(self,event):
		if(esIpValida(self.tIp.GetValue()) == True):
			self.tConsola.AppendText("\nConectando a: " + str(self.tIp.GetValue()))
			if(self.conec == -1):
				self.conec = conectarServer(self.tInformacion,self.list,str(self.tIp.GetValue()),self)
			

		else:
			self.tConsola.SetValue("Direccion No Valida")

		self.Refresh()


if __name__ == '__main__':
	
	app = wx.App(False)
	frame = MiApp(None, "Assg Server")
	app.MainLoop()

