def generarID(lista):

	repetir = True
	candidato = 0

	print(len(lista))
	if(len(lista)==0):
		return 0
	print("Espacio")
	for i in lista:
		print (i[2])
	while(repetir):
		for i in lista:
			if (candidato == i[2]):
				candidato += 1
				repetir = True
			else:
				repetir = False
	return candidato





