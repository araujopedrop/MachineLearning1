from random import randint
from math import exp
def hardlim(sum):
	#numMetodo = 1
	if sum >= 0:
		return 1
	else:
		return 0


def hardlims(sum):
	if sum >= 0:
		return 1
	else:
		return -1


def logsig(sum):
	#numMetodo = 2
	print sum
	print exp(-sum)
	val = 1/(1 + exp(-sum))
	return val





def crearPerceptron(cantEntradas):
	lista = []
	for entrada in range(cantEntradas+1):
		if (randint(1,50) > 25):
			lista.append(randint(1,20)/20.0) 
		else:
			lista.append(-1 * randint(1,20)/20.0) 
	print "Perceptron inicializado", lista
	return lista 


def calcularNeta(per,pat,numMetodo):
	sumatoria = 0
	cantPesos = len(per)
	neta = 0
	for index in range(cantPesos):
		if index == 0:
			sumatoria = sumatoria + per[0]*1
		else:
			sumatoria = sumatoria + per[index]*pat[index-1]
	if (numMetodo == 1):
		neta = hardlim(sumatoria)
	else:
		neta = logsig(sumatoria)
	return neta




def ajustarPesos(per,err,patron,alfa):
	cantEntradas = len(per)
	print cantEntradas
	print range(cantEntradas)
	print patron

	for index in range(cantEntradas):
		if (index == 0):
			per[0] = per[0] + alfa*err*1
		else:
			#print "Peso[%d] = Peso[%d] + alfa*err*patron[%d]" % (index,index,index-1)
			per[index] = per[index] + alfa*err*patron[index-1]
	return per




def entrenarPerceptron(per,pat,a):
	cantPatrones = len(pat)
	error = 1
	errorTotal = 1
	sumatoria = 0
	neta = 0
	cantIteraciones = 0
	numPatron = 0
	flag = 1
	while (flag != 0):
		if cantIteraciones < 1000:
			cantIteraciones = cantIteraciones + 1
			errorTotal = 0
			numPatron = 0
			flag = 0

			for patron in pat:
				numPatron = numPatron + 1
				sumatoria = (per[0]*1 + per[1]*patron[0] + per[2]*patron[1])
				neta = hardlim(sumatoria)
				error = patron[2] - neta
				if error != 0:
					flag = 1
				per = ajustarPesos(per,error,patron,a)
				print "Iteracion: %d, Patron: %d, Pesos = [%f,%f,%f], Sumatoria: %f, Error: %d" % (cantIteraciones,numPatron,per[0],per[1],per[2],sumatoria,error) 
			print
		else:
			print "Ups, muchas iteraciones" 
			break
	return per



def excitarPerceptron(input,per):
	neta = per[0]*1 + per[1]*input[0] + per[2]*input[1]
	output = hardlim(neta)

	return output


















def ajustarPesosRed(diccionarioRedPerceptrones,error,patron,alfa):
	#w(t+1) = w(t) + alfa*error*x
	for capa in diccionarioRedPerceptrones:
		listaPerceptrones = diccionarioRedPerceptrones[capa]
		for index in range(len(listaPerceptrones)):
			perceptron = listaPerceptrones[index]
			perceptron = ajustarPesos(perceptron,error,patron,alfa)
	return diccionarioRedPerceptrones


def inicializarListaInput(pat,lista,cantPer):
	#pat: patron a copiar
	#    [x1,x2,x3,...,xn,salida]
	#lista: lista que contendra los patrones copiados "cantPer" veces SIN la salida
	#cantPer = Cantidad de perceptrones de la ultima capa
	patSinSalida = pat[:(len(pat) - 1)] #me devuelve la lista sin la salida
	for cant in range(cantPer):
		lista.append(patSinSalida)
	return lista


def calcularListaNeta(capa,listaIn):
	#Genera la lista de salidas de una capa, a partir de sus entradas
	#capa     = lista con los perceptrones de esa capa    
	#listaIn  = Lista de listas. Habra un sublista por cada perceptron. Cada sublista tendra el patron de entrada para ese perceptron
	#           [[x1,x2,...],[x3,x4,...],[x5,x6,...,],...]
	#listaOut = Lista con los valores de salida de cada perceptron
	#           [O1,O2,O3,...]
	listaOut = []
	if (len(capa) == 1):
		numMetodo = 1
	else:
		numMetodo = 2
	for index in range(len(capa)):
		listaOut.append(calcularNeta(capa[index],listaIn[index],numMetodo))
	return listaOut


def generarListaInput(listaOut):
	#Genera la listaInput para la siguiente capa, a partir de la listaOut de la capa actual
	#listaOut = Lista con los valores de salida de cada perceptron de una determinada capa
	#		  = [O1,O2,O3,...]
	#listaIn  = Lista de listas. Habra un sublista por cada perceptron. Cada sublista tendra el patron de entrada para ese perceptron
	#           [[x1,x2,...],[x3,x4,...],[x5,x6,...,],...]
	lon = len(listaOut)
	listaIn  = []
	for entrada in range(lon - 1):
		listaIn.append(listaOut)
	return listaIn 



def crearRedPerceptron(capas,cantEntradas):
	#cantEntradas = es el numero de entradas de la ultima capa solamente
	#               La cantidad de entradas de las restantes capas va a ser igual a la cantidad de perceptrones de la capa anterior
	#capas        = numero de capas de la red. Tmb, numero de perceptrones en la ultima capa
	numeroCapa = capas
	cantPerceptrones = 0
	diccPerceptrones = {}
	perceptron = []
	listaPerceptrones = []
	cont = 0
	numeroPer = 1
	for elem in range(capas):    
		cantPerceptrones = cantPerceptrones + (elem + 1)    #obtengo la cantidad de perceptrones totales

	print "Capa: %d" % (numeroCapa)
	while(numeroPer <= cantPerceptrones):					
		if cont < numeroCapa:
			if (numeroCapa == capas):                         #Si estoy en la ultima capa
				perceptron = crearPerceptron(cantEntradas)    #Creo perceptrones con "cantEntradas + 1" entradas. +1 por la de bias
			else:
				perceptron = crearPerceptron(numeroCapa + 1)  #Creo perceptrones con "numeroCapa + 2" entradas. +2 del bias y xq entradas = cantAnteriorPerceptrones + 1 
			listaPerceptrones.append(perceptron)
			cont = cont + 1
			numeroPer = numeroPer + 1
		else:
			print "Capa: %d" % (numeroCapa-1)
			diccPerceptrones[numeroCapa] = listaPerceptrones  #Lleno el diccionario con la clave y su lista respectiva
			cont = 0
			numeroCapa = numeroCapa - 1
			listaPerceptrones = []
	print
	diccPerceptrones[numeroCapa] = listaPerceptrones          #Lleno el diccionario con la clave y su lista respectiva de la primera capa

	print diccPerceptrones
	return diccPerceptrones




def entrenarRedPerceptron(diccPer,pat,a):
	cantIteraciones = 0
	capas = max(diccPer.keys())
	flag = 1
	error = 0
	listaCapa = []
	listaneta = []
	listaInput = []
	pataux = pat
	lenPatron =  len(pat[0])
	salida = 0
	while (flag != 0):                      #Si el flag se pone en 1, quiere decir que la red ya aprendio
		if cantIteraciones < 22000:             #Pongo un limite en las iteraciones para que no loopee infinitamente
			cantIteraciones = cantIteraciones + 1
			flag = 0
			print
			print "Iteracion: %d" % (cantIteraciones)
			print
			for patron in pataux:      							                      #Por cada patron
				print "  Patron:",patron
				print
				salida = patron[lenPatron-1]
				for capa in diccPer:                                                  #Por cada capa
					if(capa == 1):											          #Si es la capa mas grande
						listaInput = inicializarListaInput(patron,listaInput,capas)   #inicializo la listaInput por cada patron. Lo hago una vez por cada uno
					else:						                                      #Si es otra capa
						listaInput = generarListaInput(listaneta)          		      #genero la lista de input con la lista neta
						print
						print
					listaCapa  = diccPer[capas-capa+1]                                #tomo la capa (de la mas grande a la mas chica)
					print "    Capa", capas-capa+1
					print "   ",listaCapa
					print
					print "    Entradas"
					print "   ",listaInput
					print
					listaneta  = calcularListaNeta(listaCapa,listaInput)              #genero la lista neta
					print "    Salida"
					print "   ",listaneta
					listaInput = []
				error = salida - listaneta[0] 
				print
				print "    Error:",error
				print
				if (error != 0):
					flag = 1

				diccPer = ajustarPesosRed(diccPer,error,patron,a)
				print "    Nuevos pesos:", diccPer
				listaneta = []
				print



		else:
			print "Ups, muchas iteraciones" 
			break
	if (flag == 0):
		print "Entrenamiento finalizado con Exito"
	else:
		print "Entrenamiento incompleto o fallido"

	return diccPer



def excitarRed(diccPer,patron):
	listaInput = []
	listaneta = []
	listaCapa = []
	capas = max(diccPer.keys())
	for capa in diccPer:                                                  #Por cada capa
		if(capa == 1):											          #Si es la capa mas grande
			listaInput = inicializarListaInput(patron,listaInput,capas)   #inicializo la listaInput por cada patron. Lo hago una vez por cada uno
		else:						                                      #Si es otra capa
			listaInput = generarListaInput(listaneta)          		      #genero la lista de input con la lista neta
		listaCapa  = diccPer[capas-capa+1]                                #tomo la capa (de la mas grande a la mas chica)
		listaneta  = calcularListaNeta(listaCapa,listaInput)              #genero la lista neta
		listaInput = []
	return listaneta















numeroCapas = 2
numeroEntradas = 2
alfa = 0.6
patronAND = [[1,1,1],[1,0,0],[0,1,0],[0,0,0]]
patronOR  = [[0,0,0],[0,1,1],[1,0,1],[1,1,1]]
patronXOR = [[1,1,0],[1,0,1],[0,1,1],[0,0,0]]
patron2   = [[2,1,1],[0,-1,1],[-2,1,-1],[0,2,-1]]
patronCuadrados = [[1,1,1],[2,4,1],[3,9,1],[4,16,1],[5,25,1],[6,36,1],[7,49,1],[8,64,1],[9,81,1],[10,100,1],[4,2,0],[9,3,0],[16,4,0],[36,6,0],[49,7,0],[64,8,0]]


#Lista1 = crearPerceptron(numeroEntradas)
#Lista1 = entrenarPerceptron(Lista1,patronAND,alfa)
red = crearRedPerceptron(numeroCapas,numeroEntradas)
red = entrenarRedPerceptron(red,patronXOR,alfa)
#print calcularNeta(Lista1,[1,1])

print excitarRed(red,[12,121,1])
print excitarRed(red,[12,120,0])
print excitarRed(red,[12,181,1])