class Character:
	hp = 100
	race = None
	guild = None

	def __init__(self, name, xp, mana, **kwargs):
		self.name = name
		self.xp = xp
		self.mana = mana


		for llave, valor in kwargs.items():
			setattr(self, llave, valor)


	def race_modifiers(self):
		if self.race:
			if self.race.__class__.__name__ == 'Elf':
				self.mana *= 2
			elif self.race.__class__.__name__ == 'Dwarf':
				self.mana -= self.mana /2
				self.hp += self.hp/2
			elif self.race.__class__.__name__ == 'Human':
				self.hp += self.hp/2
				self.mana += self.mana/2

		else:
			print('No tienes modificadores de raza')




class Elf:
	race = "Elfo"
	arcane_magic = True
	def __init__(self, arcane_magic=True):
		self.arcane_magic = arcane_magic


	def __str__(self):
		return f'Raza: {self.race}'



	def mystic_fire(self, mana, target):
		damage = 9
		if mana >= 7:
			mana -= 7
			target.hp -= damage
			print(f'Fuego mistico desatado \n{damage} de daño inflingido')
		else:
			print('Necesitas más mana')

	def arcane_ritual(self, xp, target):
		damage = 5
		if self.arcane_magic and xp >= 20:
			target.hp -= damage
			print(f'El ataque arcano se ha lanzado \n{damage} de daño inflingido')
		else:
			print('Nivel de xp insuficiente')





class Human:
	race = "Humano"
	natural_talent = True
	def __init__(self, natural_talent=True):
		self.natural_talent = natural_talent


	def __str__(self):
		return f'Raza: {self.race}'	




	def last_breath(self, hp, target):
		damage = 50
		if self.natural_talent and hp > 50:
			hp -= 50
			target.hp -= damage
			print(f'Ultimo aliento!!! \n{damage} de daño inflingido')
		else:
			print('No cumples los requisitos')



class Dwarf:
	race = "Enano"
	dwarf_rage = True
	def __init__(self, dwarf_rage=True):
		self.dwarf_rage = dwarf_rage


	def __str__(self):
		return f'Raza: {self.race}'



	def outrage(self, target):
		damage = 10
		if self.dwarf_rage:
			target.hp -= damage
			print(f'Furia desatada \n{damage} de daño inflingido')
		else:
			print('No posees la furia enana')