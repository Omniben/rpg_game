from .character import Character 
from .atributos import Sigilo, Agil


class Ladron(Character, Sigilo, Agil):
	role = 'Ladron'
	description = 'Agiles bandidos que usan su destreza en combate, optimos para la exploracion y saqueos de mazmorras'

	def __init__(self, name=None, xp=20, mana=30, **kwargs):
		super().__init__(name, xp, mana, **kwargs)


	def __str__(self):
		return f'Clase: {self.role} \nDescripción: {self.description}'


	def robar(self, target):
		damage = 3
		if self.sigilo:
			target.hp -= damage
			print(f'{damage} de daño inflingido')
			return bool(random.randint(0, 1))
		return False