#-*-coding: utf-8-*-
from random import randint
#-*-coding: utf-8-*-
class Mundo():
	def __init__(self):
		self.eventsthread = True
		self.arround = {}
		self.lugarnuevo = True
		self.objetos = {
		"Poción de resistencia":[1,("Poción (debil)", "Resistencia",True),5],
		"Cordero":[1,("Comida", "Hambre",True),5],
		"Poción de regeneración":[1,("Poción (debil)","Salud",True), 3],
		"Moneda":[1,("Dinero", "Dinero",True),1],
		"Espada":[1,("Arma","Fuerza",False,"Arma"), 20],
		"Lanza":[1,("Arma","Fuerza",False,"Arma"), 15],
		"Martillo":[1,("Arma","Fuerza",False,"Arma"), 30],
		"Casco":[1,("Armadura","Salud",False,"Cabeza"),10],
		"Peto":[1,("Armadura","Salud",False,"Pecho"),30],
		"Guantes de combate":[1,("Armadura","Salud",False,"Manos"),5],
		"Guantes termicos":[1,("Ropa","Temperatura corporal",False,"Manos"),5],
		"Sueter":[1,("Ropa","Temperatura corporal",False,"Pecho"),10],
		"Gorro termico":[1,("Ropa","Temperatura corporal",False,"Cabeza"),5]
		}
	def lookarround(self):
		if self.lugarnuevo:
			for item in self.objetos:
				if randint(0,1) == 1:
					self.arround[item] = self.objetos[item]
					self.arround[item][0] = randint(1,5)
		listarobjetos(self.arround)
def listarobjetos(lista):
	print("Objeto      |      Cantidad       |      Tipo")
	for item in lista:
		print("----------------------------------------")
		print("{}      |      {}      |      {}".format(item,lista[item][0],lista[item][1][0]))
