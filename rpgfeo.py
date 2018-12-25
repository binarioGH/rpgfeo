 #-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from platform import python_version as pv
from platform import platform
from random import choice, randint
from lib.character import Personaje
from lib.combat import *
from lib.entorno import Mundo
from os import system
from getpass import getpass
def lluvia():
	m.eventsthread = False
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
	m.eventsthread = True
def robo():
	mc.pause = True
	m.eventsthread = False
	narrador =("**Una persona se aproxima, tiene uniforme de la orden de los cuervos.","**Una sombra está rondando, aparenta malas intenciones.","**Un bandido mira a {} fijamente mientras se acerca.".format(mc.nombre))
	print(choice(narrador))
	print("\n*****Batalla*****")
	ladron_vida = randint(2*mc.status["Nivel"], 3*mc.status["Nivel"])
	ladron_ataque = randint(mc.status["Nivel"],4*mc.status["Nivel"])
	print("\n{}".format(choice(narrador)))
	getpass("Presiona doble enter para continuar...		")
	kmbt = combat(mc.clear, mc.nombre, mc.status["Salud"],mc.status["Fuerza"],"???",ladron_vida,ladron_ataque)
	if kmbt == 1:
		print("**{} derrotó al ladrón y escapó.".format(mc.nombre))
		xp = (ladron_vida + ladron_ataque) / 2
		print("**{} adquirio {} puntos de xp.".format(mc.nombre, xp))
		mc.xp += xp
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
	m.eventsthread = True

def eventos():
	events = (lluvia, robo)
	while m.eventsthread:
		sleep(randint(60, 120))
		choice(events)() #Escoger un evento de manera 'aleatoria'
				
if __name__ == '__main__':
	m = Mundo()
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
				elif cmd[:7] == "mejorar":
					mc.consumirxp(cmd[8:])
				elif cmd[:7] == "equipar":
					mc.equipar(cmd[8:])
				elif cmd[:10] == "desequipar":
					mc.desequipar(cmd[11:])
				elif cmd == "mirar" or cmd == "mirar el entorno" or cmd == "mirar alrrededor":
					m.lookaround()
				elif cmd == "moverse" or cmd == "caminar":
					m.lugarnuevo = True
				elif cmd[:7] == "recoger":
					if cmd[8:] in m.around and not m.tienda:
						m.around[cmd[8:]][0] = m.around[cmd[8:]][0] - 1
						print(m.around[cmd[8:]][0])
						if cmd[8:] not in mc.inventario:
							mc.inventario[cmd[8:]] = []
							for value in m.around[cmd[8:]]:
								mc.inventario[cmd[8:]].append(value)
							mc.inventario[cmd[8:]][0] = 1	
						else:
							mc.inventario[cmd[8:]][0] += 1

						if m.around[cmd[8:]][0] == 0:
							del m.around[cmd[8:]]
					else:
						if not m.tienda:
							print("**No puedes recoger objetos de una tienda.")
						else:
							print("**No se encuentra dicho objeto en el entorno.")
				elif cmd[:7] == "comprar":
					if cmd[8:] in m.around and m.tienda:
						if mc.status["Dinero"] >= m.around[cmd[8:]][2] * m.around[cmd[8:]][2]:
							mc.status["Dinero"] -= m.around[cmd[8:]][2] * m.around[cmd[8:]][2]
							if cmd[8:] in mc.inventario:
								mc.inventario[cmd[8:]][0] += 1
							else:
								mc.inventario[cmd[8:]] = []
								for value in m.around[cmd[8:]]:
									mc.inventario[cmd[8:]].append(value)
								mc.inventario[cmd[8:]][0] = 1
							m.around[cmd[8:]][0] -= 1
							if m.around[cmd[8:]][0] <= 0:
								del m.around[cmd[8:]]
						else:
							print("**No tienes suficiente dinero.")
					else:
						if not m.tienda:
							print("**No estás en una tienda")
						else:
							print("**Dicho objeto no se encuentra en la tienda.")

				elif cmd == mc.clear:
					system(mc.clear)
				elif cmd == "ADMIN: -*-lluvia":
					rain = Thread(target=lluvia)
					rain.daemon = True
					rain.start()
				elif cmd == "ADMIN: -*-robo":
					crime = Thread(target=robo)
					crime.daemon = True
					crime.start()
				elif cmd == "ADMIN: -*-xp":
					mc.xp = 1000
				elif cmd == "ADMIN: -*-dinero":
					mc.status["Dinero"] += 10000
			except IndexError:
				pass
			except Exception as e:
				print("ERROR: {}".format(e))
	print("Game Over...")