def esIpValida(dirIP):
	#chequeo 4 puntos
	cp = 0
	for i in range(len(dirIP)):
		if(dirIP[i] == '.'):
			cp = cp + 1 
	if (cp != 3):
		print ("No hay 3 Puntos en: ",dirIP)
		return False
	else:
		numero = ''
		for i in range(len(dirIP)):
			if(dirIP[i] != '.'):
				numero = numero + dirIP[i]
			else:
				if(int(numero) < 0 or int(numero) > 255):
					print("Fuera de RANGO")
					numero = ""
					return False
				else:
					numero =""
		if(int(numero) < 0 or int(numero) > 255):
			print("Fuera de RANGO")
			numero = ""
			return False
		else:
			numero =""
		print("Direccion ip valida: ", dirIP)
		return True

def datoValido(dato):
	for i in range(len(dato)):
		print("fin")