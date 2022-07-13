from .character import Character



class Archer(Character):
	agility = True
	role = 'Arquero'
	descripton = 'Aventurero que ayuda a su equipo desde la lejania, son una parte tactica de cualquier grupo con sus ataques a larga distancia'

	def __init__(self, name=None, xp=20, mana=40, special_arrows=True, fire_range=40, **kwargs):
		super().__init__(name, xp, mana, **kwargs)
		self.special_arrows = special_arrows
		self.fire_range = fire_range

	def __str__(self):
		return f'Clase: {self.role} \nDescripción: {self.descripton}'


	def dodge(self):
		if self.agility and self.xp > 11:
			return print("Esquivas!")
		return print("No cumples los requisitos")	

	def special_attack(self, target):
		damage = 7
		if self.special_arrows:
			target.hp -= damage
			return print(f"Flecha especial!! \n{damage} de daño inflingido")
		return print("No cumples los requisitos")

	def long_range_shot(self, target):
		damage = 5 + (self.fire_range // 10)
		if self.special_arrows and self.fire_range > 40:
			target.hp -= damage
			return print(f"Tiro de máxima distancia \n{damage} de daño inflingido")
		return print("No cumples los requisitos")