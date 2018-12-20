 #-*-coding: utf-8-*-
from threading import Thread
from time import sleep
from platform import python_version as pv
from random import randint, choice
from lib.character import *
def lluvia():
	empieza_lluvia = ("\n{}(pensamiento): Está empezando a llover.".format(mc.nombre),"\n{}(pensaiento):Las frias gotas de la lluvia me traen malos recuerdos.".format(mc.nombre),"\n{}(pensamiento):Quizá está lluvia sea un problema despues".format(mc.nombre))
	acaba_lluvia=("\n{}(pensamiento): La lluvia acabó".format(mc.nombre),"\n{}(pensamiento):Parese que no habrá lluvia por un rato".format(mc.nombre),"\n{}(pensamiento): La lluvia se fue, espero que tambien se vaya el frio".format(mc.nombre))
	print(choice(empieza_lluvia))
	tiempo_de_lluvia = randint(60, 300)
	count = 0
	while count != tiempo_de_lluvia:
		sleep(1)
		if randint(0,10) == 5:
			mc.status["Temperatura corporal"] -= 1
	print(choice(acaba_lluvia))
def robo():
	narrador =("**Una persona se aproxima, tiene uniforme de la orden de los cuervos.","**Una sombra está rondando, aparenta malas intenciones.","**Un bandido mira a {} fijamente mientras se acerca.".format(mc.nombre))
	print(choice(narrador))
	print("\n*****Batalla*****")
	ladron_vida = randint(2, 3)
	ladron_ataque = randint(1,4)
	inv = []
	for item in mc.inventario:
		inv.append(item)
	objeto_robado = choice(inv)
	cantidad_robada = randint(1,mc.inventario[objeto_robado][0])
	if mc.status["Fuerza"] > ladron_vida:
		print("\n**{} ataca al sospechoso y lo derrota.".format(mc.nombre))
	else:
		print("\n**Los ataques de {} no son lo suficientemente fuertes para el bandido.".format(mc.nombre))
		do = randint(1,3)
		if do == 1:
			print("\n**El bandido toma {}  de la mochila de {}.".format(objeto_robado, mc.nombre))
			if cantidad_robada == mc.inventario[objeto_robado][0]:
				del mc.inventario[objeto_robado]
			else:
				mc.inventario[objeto_robado][0] -= cantidad_robada
		elif do == 2:
			print("El bandido le hace daño a {} y hulle.".format(mc.nombre))
			mc.status["Salud"] -= ladron_ataque
		elif do == 3:
			print("{} logra escapar a salvo.".format(mc.nombre))
def eventos():
	events = (lluvia, robo)
	while True:
		sleep(randint(60, 120))
		choice(events)() #Escoger una función random de la lista events (está en lib.events)

if __name__ == '__main__':
	if str(pv())[0] == "3":
		raw_input = input
	n = str(raw_input("Ingresa el nombre de tu personaje: "))
	g = ""
	while g != "h" and g != "m":
		g = str(raw_input("Ingresa el genero de tu personaje [h / m]: "))
	mc = Personaje(n, g)
	cmd = ""
	events = Thread(target=eventos)
	events.daemon = True
	events.start()
	while cmd != "gameover" and mc.status["Salud"] > 0:
		try:
			cmd = raw_input("({})--|>>>>".format(mc.nombre))
			if cmd == "inventario":
				mc.verInventario()
			elif cmd == "status":
				mc.verStatus()
			elif cmd[:4] == "usar":
				mc.consumir(cmd[5:])
			elif cmd == "ADMIN: -*-lluvia":
				#Comando para testear
				lluvia()
			elif cmd == "ADMIN: -*-robo":
				robo()
		except IndexError:
			pass
		except Exception as e:
			print("ERROR: {}".format(e))
	print("Game Over...")