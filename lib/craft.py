#-*-coding: utf-8-*-

class CraftingTable():
	def __init__(self):
		self.craftable = {
		"Espada de madera":(1,("Arma", "Fuerza",False,"Arma","->>"),7,{"Rama afilada":2}),
        "Lanza rustica":(1,("Arma","Fuerza",False,"Arma","---_"),8,{"Rama afilada":1,"Roca":1}),
        "Espada envenenada":(1,("Arma","Fuerza",False,"Arma","-:|>>>"),30,{"Espada":1,"Amaescarla":3}),
        "Ensalada":(1,("Comida","Hambre",True),20,{"Manzana":3,"Larmalona":2,"Zarmajola roja":1})
		}
	def craft(self, inv, wannacraft):
		c = 0
		if not wannacraft in self.craftable:
			print("**Ese objeto no existe.")
			return 0
		for req in self.craftable[wannacraft][3]:
			if req in inv:
				if inv[req][0] >= self.craftable[wannacraft][3][req]:
					c += 1
				else:
					break
			else:
				break
		if c < len(self.craftable[wannacraft][3]):
			print("**No puedes crear {} porque te faltan objetos.".format(wannacraft))
			return 0
		else:
			for ingredient in self.craftable[wannacraft][3]:
				if inv[ingredient][0] == 1:
					del inv[ingredient]
				else:
					inv[ingredient][0] -= 1
			if wannacraft in inv:
				inv[wannacraft][0] += 1
			else:
				values = []
				for value in self.craftable[wannacraft][:3]:
					values.append(value)
				inv[wannacraft] = values
	def listarobjetos(self):
		print("Objeto      |       Ingredientes")
		for item in self.craftable:
			print("{}      |      {}".format(item, self.craftable[item][3]))