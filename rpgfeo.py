 #-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from platform import python_version as pv
from platform import platform
from random import choice, randint
from lib.character import *
from lib.combat import *
from os import system
def lluvia():
	empieza_lluvia = ("\n{}(pensamiento): Está empezando a llover.".format(mc.nombre),"\n{}(pensaiento):Las frias gotas de la lluvia me traen malos recuerdos.".format(mc.nombre),"\n{}(pensamiento):Quizá está lluvia sea un problema despues".format(mc.nombre))
	acaba_lluvia=("\n{}(pensamiento): La lluvia acabó".format(mc.nombre),"\n{}(pensamiento):Parese que no habrá lluvia por un rato".format(mc.nombre),"\n{}(pensamiento): La lluvia se fue, espero que tambien se vaya el frio".format(mc.nombre))
	print(choice(empieza_lluvia))
	tiempo_de_lluvia = randint(60, 300)
	count = 0
	while count != tiempo_de_lluvia:
		sleep(1)
		if randint(0,10) == 5:
			mc.status['Temperatura corporal'] -= 1
		count += 1
	print(choice(acaba_lluvia))
def robo():
	narrador =("**Una persona se aproxima, tiene uniforme de la orden de los cuervos.","**Una sombra está rondando, aparenta malas intenciones.","**Un bandido mira a {} fijamente mientras se acerca.".format(mc.nombre))
	print(choice(narrador))
	print("\n*****Batalla*****")
	ladron_vida = randint(2, 3)
	ladron_ataque = randint(1,4)
	mc.pause = True
	kmbt = combat(mc.clear, mc.nombre, mc.status["Salud"],mc.status["Fuerza"],"???",ladron_vida,ladron_ataque)
	if kmbt == 1:
		print("**{} derrotó al ladrón y escapó.".format(mc.nombre))
	else:
		if randint(0,1) == 1:
			print("**{} es herido durante el combate, pero logra escapar.".format(mc.nombre))
		else:
			inv = []
			for item in mc.inventario:
				inv.append(item)
			objeto_robado = choice(inv)
			cantidad_robada = randint(1,inventario[objeto_robado][0])
			print("**El ladrón robó {} del inventario de {} y hulló".format(objeto_robado, mc.nombre))
			if cantidad_robada >= mc.inventario[objeto_robado][0]:
				del mc.inventario[objeto_robado]
			else:
				mc.inventario[objeto_robado][0] -= cantidad_robadat
	mc.pause = False

def eventos():
	events = (lluvia, robo)
	while True:
		sleep(randint(60, 120))
		choice(events)() #Escoger un evento de manera 'aleatoria'
		


		
if __name__ == '__main__':
	if str(pv())[0] == "3":
		#Esto es para tener compatibilidad entre python 3 y 2
		raw_input = input
	n = str(raw_input("Ingresa el nombre de tu personaje: "))
	g = ""
	while g != "h" and g != "m": 
		#Esto es para que no se pueda escoger otra opción que no sea "h" o "m"
		g = str(raw_input("Ingresa el genero de tu personaje [h / m]: "))
	mc = Personaje(n, g)
	cmd = ""
	#Empezar el hilo de eventos (abajo)
	events = Thread(target=eventos)
	events.daemon = True
	events.start()
	#Empezar el hilo de eventos(arriba)
	while cmd != "gameover" and mc.status["Salud"] > 0:
		if mc.pause:
			pass
		else:
			try:
				cmd = raw_input("({})--|>>>>".format(mc.nombre))
				if cmd == "inventario":
					mc.verInventario()
				elif cmd == "status":
					mc.verStatus()
				elif cmd[:4] == "usar":
					mc.consumir(cmd[5:])
				elif cmd == "ADMIN: -*-lluvia":
					rain = Thread(target=lluvia)
					rain.daemon = True
					rain.start()
				elif cmd == "ADMIN: -*-robo":
					crime = Thread(target=robo)
					crime.daemon = True
					crime.start()
				elif cmd == mc.clear:
					system(mc.clear)
			except IndexError:
				pass
			except Exception as e:
				print("ERROR: {}".format(e))
	print("Game Over...")