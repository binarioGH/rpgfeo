#-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from random import choice, randint
from platform import platform
class Magic():
	def __init__(self, status):
		self.s = status
		self.bottom = 5
		self.top = 10
		self.spells = {"Marchitar":(self.marchitar, "Daña a tu enemigo.", "Daño"),"Luz" :(self.luz,"Aumenta el valor de un elemento de tu status.", "Fortuna"),"Alquimia":(self.alquimia, "Transforma un objeto en oro.","Fortuna")}
		self.keepdoingthespell = True
	def marchitar(self, enemy):
		spend = randint(self.bottom,self.top)
		if self.s["Maná"] >= spend:
			self.s["Maná"] -= spend
			enemy["Salud"] -= spend
		else: 
			self.s["Salud"] -= spend / 2
	def luz(self):
		spend = randint(int(self.s["Maná"] / 6), int(self.s["Maná"] /4	))
		while self.s["Maná"] >= spend and self.keepdoingthespell:
			spnd = randint(self.bottom, self.top)
			sleep(spnd)
			self.s["Salud"] += spnd
			self.s["Maná"] -= spnd /2
	def alquimia(self):
		self.s["Dinero"] += randint(self.bottom, self.top)
		self.s["Maná"] -= 40
		self.s["Salud"] -= 3

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
		self.status = {"Salud":10,"Hambre": 10, "Fuerza": 3, "Resistencia": 30,"Dinero": 20, "Temperatura corporal":34,"Nivel":1,"Karma":0, "Maná":0}
		self.m = Magic(self.status)
		self.inventario = {"Poción de resistencia":[1,("Poción (debil)", "Resistencia", True),5],"Cordero":[3,("Comida", "Hambre",True),5]}
		self.equipables = {}
		self.equipo = {"Cabeza":[False,"0","0"],"Pecho":[False,"|","|"],"Manos":[False,None,None],"Arma":[False,"",""]}
		self.avatar ='''\n 		 {}\n 		/{}\\{}\n 		/ \\'''.format(self.equipo["Cabeza"][1],self.equipo["Pecho"][1],self.equipo["Arma"][1])
		needs = Thread(target=self.necesidades)
		needs.daemon = True
		needs.start()
	def necesidades(self):
		karmatop = 10
		karmabottom = -10
		bufo = 1
		xptop = 10
		secs = 0
		while True:
			sleep(1)
			secs += 1
			if secs >= self.status["Resistencia"]:
				secs = 0
				self.status["Hambre"] -= 1
				if self.status["Temperatura corporal"] > 38 or self.status["Temperatura corporal"] < 30:
					self.status["Salud"] -= 1
				if self.status["Hambre"] <= 0:
					self.status["Salud"] -= 1
				elif self.status["Hambre"] >= 30:
					self.status["Fuerza"] -= 1
				if self.status["Hambre"] == 5:
					print("{}(pensamiento): Empiezo a sentir hambruna".format(self.nombre))
			if self.xp >= xptop:
				if self.xp % 10 == 0:
					self.xppoints += 10
				else:
					self.xppoints += 1
				self.status["Nivel"]+= 1
				xptop = xptop * 2 
				print("**Tienes nuevos puntos de experiencia")
			if self.status["Karma"] >=  karmatop:
				self.status["Salud"] += bufo
				bufo += bufo
				karmatop += karmatop
				print("**Tu salud ha mejorado por tu karma.")
			elif self.status["Karma"] <= karmabottom:
				self.status["Fuerza"] += bufo
				bufo += bufo
				karmabottom += karmabottom
				print("**Tu fuerza ha mejorado por tu karma.")
	def consumirxp(self, mejora):
		elements = ("Fuerza", "Salud", "Resistencia","Maná")
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
			if self.equipo[self.inventario[item][1][3]][0]:
				if self.inventario[item][1][3] == "Manos":
					soespacio = ("s","n")
				else:
					soespacio = ("","")
				print("**Tu{} {} está{} en uso.".format(soespacio[0],self.inventario[item][1][3],soespacio[1]))
			else:
				self.equipo[self.inventario[item][1][3]][0] = True
				self.equipo[self.inventario[item][1][3]][1] = self.inventario[item][1][4]
				self.avatar ='''\n 		 {}\n 		/{}\\{}\n 		/ \\'''.format(self.equipo["Cabeza"][1],self.equipo["Pecho"][1],self.equipo["Arma"][1])
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
			self.equipo[self.inventario[item][1][3]][0] = False
			self.equipo[self.inventario[item][1][3][0]] = self.equipo[self.inventario[1][3][0]][2]
			self.status[self.inventario[item][1][1]] -= self.inventario[item][2]
			self.avatar ='''\n 		 {}\n 		/{}\\{}\n 		/ \\'''.format(self.equipo["Cabeza"][1],self.equipo["Pecho"][1],self.equipo["Arma"][1])
		else:
			print("**No tienes equipado ese objeto.")
