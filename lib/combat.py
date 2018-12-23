#-*-coding: utf-8-*-
from random import randint
from os import system
from platform import python_version as pv
def combat(clear,pnombre,plive, pattack,bnombre, blive, battack):
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
	while plive > 0 and blive > 0:
		system(clear)
		cmd = raw_input('''
			[{}]  [{}]        [{}]  [{}]
                                       
                {}                {}

            [A] Atacar.
            [B] Bloquear ataque.
			>>>'''.format(pnombre, plive, bnombre, blive, avatares[0], avatares[randint(1,3)]).strip())
		cmd = cmd.lower()
		if cmd == "a":
			blive -= pattack
		elif cmd == "b":
			plive += battack /2
		bchoice = randint(1,2)
		if bchoice == 1:
			plive -= battack
		elif bchoice == 2:
			blive += pattack / 2
	system(clear)
	if plive > blive:
		return 1
	else:
		return 0