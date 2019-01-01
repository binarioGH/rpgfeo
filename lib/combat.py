#-*-coding: utf-8-*-
from random import randint, choice
from os import system
from getpass import getpass
from platform import python_version as pv
class Enemy():
	def __init__(self, seed):
		cabezas =("o","8","#","6","%")
		pechos = ("#","1","|","8","I")
		armas = ("7","/",")","")
		nombres = ("Bandido","Ladrón","???","Sospechoso")
		self.avatar = "\n\n 		 {}\n		/{}\\{}\n 		/ \\".format(choice(cabezas),choice(pechos),choice(armas))
		self.nombre = choice(nombres)
		self.v = randint(2*seed, seed*3)
		self.f = randint(seed, seed*4)
		self.status = {"Salud":self.v, "Fuerza":self.f}
def combat(clear,pnombre,status,bstatus, bnombre, inv, avatar, bavatar, spells):
	olive = bstatus["Salud"]
	cando = []	
	if str(pv())[0] == "3":
		raw_input = input
	while status["Salud"] > 0 and bstatus["Salud"] > 0:
		system(clear)
		cmd = raw_input('''
			[{}]  [{}]        [{}]  [{}]
                                       
                {}                {}

            [A] Atacar.
            [B] Bloquear ataque.
            [I] Inventario.
            [M] Magia.
			>>>'''.format(pnombre, status["Salud"], bnombre, bstatus["Salud"], avatar, bavatar))
		cmd = cmd.lower()
		if cmd == "a":
			bstatus["Salud"] -= randint(int(status["Fuerza"] / 2), status["Fuerza"] * 2)
		elif cmd == "b":
			status["Salud"] += bstatus["Fuerza"] /2
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
		elif cmd == "m":
			if cando == []:
				for spell in spells:
					if spells[spell][2] == "Daño":
						cando.append(spell)
					else:
						continue
			for do in cando:
				print("{} : {}".format(do, spells[do][1]))
			do = ""
			while not do in cando:
				do = raw_input(">>")
			spells[do][0](bstatus)


		if bstatus["Salud"] <= 0:
			ganar(status, olive)
			continue
		bchoice = randint(1,2)
		if bchoice == 1:
			status["Salud"] -= bstatus["Fuerza"]
		elif bchoice == 2:
			bstatus["Salud"] += status["Fuerza"] / 2
	system(clear)
	if status["Salud"] > bstatus["Salud"]:
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