#-*-coding: utf-8-*-
from random import randint
class Mundo():
	def __init__(self):
		self.eventsthread = True
		self.around = {}
		self.lugarnuevo = True
		self.tienda = False
		self.objetos_naturales = {
		"Manzana":[1,("Comida", "Hambre",True),5],
		"Moneda":[1,("Dinero", "Dinero",True),1],
		"Rama afilada":[1,("Arma","Fuerza",False,"Arma"),5],
		"Roca":[1,("Arma","Fuerza",False,"Arma"),1],
		"Zarmajola roja":[1,("Planta","Salud",True),4],
		"Larmalona":[1,("Planta", "Fuerza",True),2],
		"Amaescarla":[1,("Planta","Salud",True),-4],
		"Lormanilas":[1,("Planta","Fuerza",True),-6]
		}
		self.objetos_tienda = {
		"Poción de resistencia":[1,("Poción (debil)", "Resistencia",True),5],
		"Poción de regeneración":[1,("Poción (debil)","Salud",True), 3],
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
	def lookaround(self):
		if self.lugarnuevo:
			if randint(1,10) == 5:
				print("**Entras a una tienda.")
				self.tienda = True
				objlist = self.objetos_tienda
			else:
				self.tienda = False
				objlist = self.objetos_naturales
			for item in objlist:
				if randint(0,1) == 1:
					self.around[item] = objlist[item]
					self.around[item][0] = randint(1,5)
		if self.tienda:
			listarobjetos(self.around, True)
		else:
			listarobjetos(self.around)
		self.lugarnuevo = False
def listarobjetos(lista, tienda=False):
	if tienda:
		extra="      |     Precio"

	else:
		extra=""

	print("Objeto      |      Cantidad       |      Tipo{}".format(extra))
	for item in lista:
		if tienda:
			precio=lista[item][2]*lista[item][2]
			extra2="      |     "
		else:
			precio=""
			extra2=""
		print("----------------------------------------")
		print("{}      |      {}      |      {}{}{}".format(item,lista[item][0],lista[item][1][0],extra2,precio))
