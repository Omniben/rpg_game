import random
from .character import Character



class Wizard(Character):
	healing = True
	intelligence = True
	role = "Mago"
	description = 'Sabio que estudia el olvidado mundo de la magia y lo arcano'

	def __init__(self, name=None, xp=20, mana=65, healing=True, **kwargs):
		super().__init__(name, xp, mana, **kwargs)
		self.healing = healing

	def __str__(self):
		return f'Clase: {self.role} \nDescripción: {self.description}'

	def recover_mana(self):
		if self.healing:
			add = random.randint(1,10)

			self.mana += add

			return print(f"+{add} de maná")
		return print("+0")

	def magic_wall(self):
		if self.intelligence and self.xp >= 20:
			return print('|')
		return print("No cumples los requisitos")


	def plasma_burst(self, target):
		damage = 9
		if self.xp > 18 and self.mana > 10:
			target.hp -= damage
			return print(f'Pum!!! \n{damage} de daño inflingido')
		return print("No cumples los requisitos")