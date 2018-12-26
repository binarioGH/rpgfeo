#-*-coding: utf-8-*-
from random import randint
from os import system
from getpass import getpass
from platform import python_version as pv
def combat(clear,pnombre,status,bnombre, blive, battack, inv):
	oblive = blive
	avatares = (
		'''
            0
	   /|\\
	   / \\''',    
	   '''
            #
	   /|\\
	   / \\
	   ''',
	   '''
            8
	   /|\\
	   / \\''',
	   '''
            6
	   /|\\
	   / \\ ''')
	if str(pv())[0] == "3":
		raw_input = input
	while status["Salud"] > 0 and blive > 0:
		system(clear)
		cmd = raw_input('''
			[{}]  [{}]        [{}]  [{}]
                                       
                {}                {}

            [A] Atacar.
            [B] Bloquear ataque.
            [I] Inventario.
			>>>'''.format(pnombre, status["Salud"], bnombre, blive, avatares[0], avatares[randint(1,3)]).strip())
		cmd = cmd.lower()
		if cmd == "a":
			blive -= randint(int(status["Fuerza"] / 2), status["Fuerza"] * 2)
		elif cmd == "b":
			status["Salud"] += battack /2
		elif cmd == "i":
			print("Objeto      |      Cantidad      |      Tipo")
			for obj in inv:
				print("---------------------------------------------")
				print("{}      |      {}       |      {}".format(obj, inv[obj][0], inv[obj][1][0]))
			select = ""
			while not select in inv:
				select = raw_input("Ingresa el objeto que usaras: ")
			if inv[select][1][2]:
				buff = inv[select][1][1]
				if buff == "Fuerza" or buff == "Salud":
					status[buff] += inv[select][2]
				else:
					print("**Este objeto no se puede usar en combate.")
			else:
				print("**Este objeto no es consumible.")
			getpass("Aprieta enter para continuar.")
		if blive <= 0:
			ganar(status, oblive)
			continue
		bchoice = randint(1,2)
		if bchoice == 1:
			status["Salud"] -= battack
		elif bchoice == 2:
			blive += status["Fuerza"] / 2
	system(clear)
	if status["Salud"] > blive:
		return 1
	else:
		return 0
def ganar(status, seed):
	if str(pv())[0] == "3":
		raw_input = input
	print("Haz derrotado al ladrón, decide que hacer con el.")
	print('''
		[M]atar
		[R]obar
		[P]erdonar''')
	do = ""
	while do != "m" and do != "r" and do != "p":
		do = raw_input(">>>")
		do = do.lower()
	if do == "m":
		status["Karma"] -= randint(2,7) * status["Nivel"]
	elif do == "r":
		status["Karma"] -= status["Nivel"]
		status["Dinero"] += randint(seed, seed * 2) 
	elif do == "p":
		status["Karma"] += randint(2,7) * status["Nivel"]