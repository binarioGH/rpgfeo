#-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from random import choice
from platform import platform
def listarobjetos(lista):
	print("Objeto      |      Cantidad       |      Tipo")
	for item in lista:
		print("----------------------------------------")
		print("{}      |      {}      |      {}".format(item,lista[item][0],lista[item][1][0]))
class Personaje():
	def __init__(self, nombre, genero):
		self.pause = False
		self.xp = 0
		self.xppoints = 0
		if str(platform())[0] == "W":
		 	self.clear = "cls"
		else:
			self.clear = "clear"
		self.nombre = nombre
		self.genero = genero
		if self.genero == "h":
			self.letra = ("o", "ó")
		else:
			self.letra = ("a", "á")
		self.comentarios()
		self.status = {"Salud":10,"Hambre": 10, "Fuerza": 3, "Resistencia": 30,"Dinero": 20, "Temperatura corporal":34,"Nivel":1}
		self.inventario = {"Poción de resistencia":[1,("Poción (debil)", "Resistencia", True),5],"Cordero":[3,("Comida", "Hambre",True),5]}
		self.equipables = {}
		self.equipo = {"Cabeza":False,"Pecho":False,"Manos":False,"Arma":False}
		hambruna = Thread(target=self.hunger)
		hambruna.daemon = True
		hambruna.start()
		temp = Thread(target=self.temperatura)
		temp.daemon = True
		temp.start()
		niveles = Thread(target=self.lvlup)
		niveles.daemon = True
		niveles.start()
	def lvlup(self):
		xptop = 10
		while True:
			if self.xp >= xptop:
				if self.xp % 10 == 0:
					self.xppoints += 10
				else:
					self.xppoints += 1
				self.status["Nivel"]+= 1
				xptop = xptop * 2 
				print("**Tienes nuevos puntos de experiencia")

	def consumirxp(self, mejora):
		elements = ("Fuerza", "Salud", "Resistencia")
		if mejora in elements:
			if self.xppoints <= 0:
				print("**No tienes suficientes puntos de experiencia.")
			else:
				print("**Se ha mejorado el atributo {}.".format(mejora))
				self.status[mejora] += 1
				self.xppoints -= 1
		else:
			print("**No se puede mejorar el atributo '{}'.".format(mejora))
	def comentarios(self):	
		self.no_encontrar = ("\n{}(pensamiento): Quizá me falla la memoría, pero estaba segur{} de que dejé eso aquí".format(self.nombre, self.letra[1]),"\n{}(Pensamiento): Juraría que tenía un poco aún".format(self.nombre),"\n{}(Pensamiento): Diablos, ya no tengo más".format(self.nombre),"{}(pensamiento): ¿Donde quedó eso que estoy buscando?".format(self.nombre))
		self.acabar=("\n{}(pensamiento): Creo que ese era el ultimo...".format(self.nombre),"\n{}(pensamineto): Y ahí va la ultima que quedaba...".format(self.nombre),"\n{}(pensamiento): Creo que con eso no quedan más.".format(self.nombre))
	def temperatura(self):
		while True:
			if self.status["Temperatura corporal"] > 38 or self.status["Temperatura corporal"] < 30:
				sleep(self.status["Resistencia"])
				self.status["Salud"] -= 1
	def hunger(self):
		while True:
			sleep(self.status["Resistencia"])
			if self.status["Hambre"] <= 0:
				self.status["Salud"] -= 1
				if self.status["Salud"] == 5:
					print("{}(pensamiento): Estoy en un muy mal estado".format(self.nombre))
			else:
				self.status["Hambre"] -= 1
				if self.status["Hambre"] == 5:
					print("{}(pensamiento): Empiezo a sentir hambruna".format(self.nombre))
	def verInventario(self):
		listarobjetos(self.inventario)
	def verStatus(self):
		for necesidad in self.status:
			print("{}: {}".format(necesidad, self.status[necesidad]))
	def consumir(self, item):
		if item in self.inventario and self.inventario[item][1][2]:
			self.status[self.inventario[item][1][1]] += self.inventario[item][2]
			self.inventario[item][0] -= 1
			if self.inventario[item][0] <= 0:
			    del self.inventario[item]
			    print(choice(self.acabar))		
		else:
			if item not in self.inventario:
				print(choice(self.no_encontrar))
			else:
				print("**{} no es un objeto consumible.".format(item))
	def equipar(self, item):
		if item in self.inventario and not self.inventario[item][1][2]:
			if self.equipo[self.inventario[item][1][3]]:
				if self.inventario[item][1][3] == "Manos":
					soespacio = ("s","n")
				else:
					soespacio = ("","")
				print("**Tu{} {} está{} en uso.".format(soespacio[0],self.inventario[item][1][3],soespacio[1]))
			else:
				self.equipo[self.inventario[item][1][3]] = True
				self.equipables[item] = self.inventario[item]
				del self.inventario[item]
				self.status[self.equipables[item][1][1]] += self.equipables[item][2]			
		else:
			if item not in self.inventario:
				print(choice(self.no_encontrar))
			else:
				print("**{} no es un objeto equipable".format(item))
	def desequipar(self, item):
		if item in self.equipables:
			self.inventario[item] = self.equipables[item]
			del self.equipables[item]
			self.equipo[self.inventario[item][1][3]] = False
			self.status[self.inventario[item][1][1]] -= self.inventario[item][2]
		else:
			print("**No tienes equipado ese objeto.")