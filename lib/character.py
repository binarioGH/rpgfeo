#-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from platform import platform
class Personaje():
	def __init__(self, nombre, genero):
		self.pause = False
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
		self.status = {"Salud":10,"Hambre": 10, "Fuerza": 3, "Resistencia": 30, "Arma equipada": 0, "Armadura":0,"Dinero": 20, "Temperatura corporal":34}
		self.inventario = {"Poción de resistencia":[1,("Resistencia (debil)", "resistenciatencia"),5],"Cordero":[3,("Comida", "Hambre"),5]}
		self.objetivos = {}
		hambruna = Thread(target=self.hunger)
		hambruna.daemon = True
		hambruna.start()
		temp = Thread(target=self.temperatura)
		temp.daemon = True
		temp.start( )
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
		print("Objeto      |      Cantidad       |      Tipo")
		for item in self.inventario:
			print("----------------------------------------")
			print("{}      |      {}      |      {}".format(item,self.inventario[item][0],self.inventario[item][1][0]))
	def verStatus(self):
		for necesidad in self.status:
			print("{}: {}".format(necesidad, self.status[necesidad]))
	def consumir(self, item):
		if item in self.inventario:
			self.status[self.inventario[item][1][1]] += self.inventario[item][2]
			self.inventario[item][0] -= 1
			if self.inventario[item][0] <= 0:
			    del self.inventario[item]
			    print(choice(self.acabar))		
		else:
			print(choice(self.no_encontrar))