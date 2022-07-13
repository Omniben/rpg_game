from .character import Character, Elf, Dwarf, Human
from .wizard import Wizard
from .ladron import Ladron
from .archer import Archer
from models.exceptions import RaceException


class Menu:
	roles = [ Wizard(), Ladron(), Archer(),
]


	razas = [ Elf(), Human(), Dwarf(),
]
	
	gremios = ['Royal Never Give Up', 'Natus Vincere', 'Mad Lions',
 'Origen', 'Evil Geniuses', '100 Thieves', 'Golden Guardians',
]




	def crear_personaje(self):
		name = input('Para empezar ingresa un nombre para tu personaje: ')


		print('\nElige un rol para tu personaje:')

		for indice,rol in enumerate(self.roles, start=1):
			print(f"{indice}.→ {rol}")

		rol = int(input('\n:'))

		pj = self.roles[rol-1]
		pj.name = name


		while True:

			print('\nElige una de las siguientes razas:')

			for r in self.razas:
				print(f"{r.race}")

			raza = input('\n:')

			try:
				if raza.lower() == "elfo":
					pj.race = Elf()
				elif raza.lower() == "humano":
					pj.race = Human()
				elif raza.lower() == "enano":
					pj.race = Dwarf()
				else:
					pj.race = raza

				if not isinstance(pj.race, Elf) and not isinstance(pj.race, Human) and not isinstance(pj.race, Dwarf):
					raise RaceException()

			except RaceException:
				print(f'Raza invalida, "{pj1.race}" no es una raza existente')
				continue

			else:
				break

		print('\n¡Personaje creado!')

		return pj



	def elegir_gremio(self):
		print('Para terminar, ¿quieres unirte a un gremio? ')
		while True:
			eleccion = input('\nsi/no\n:')
			if eleccion == "si":
				print('Elige un gremio para unirte:\n')
				for indice,gremio in enumerate(self.gremios, start=1):
					print(f'{indice}.→ {gremio}')
				eleccion_gremio = int(input('\n:'))	
				return self.gremios[eleccion_gremio-1]
				break

			elif eleccion == "no":
				print('No perteneceras a ningun gremio')
				break
			else:
				print('ingrese "si" o "no" para continuar')
				continue


	@staticmethod
	def ataques_razas(sujeto, objetivo):
		if sujeto.race.__class__.__name__ == "Elf":
			print('''1.→ Fuego mistico \n2.→ Ritual arcano''')
		elif sujeto.race.__class__.__name__ == "Human":
			print('1.→ Ultimo Aliento')
		elif sujeto.race.__class__.__name__ == "Dwarf":
			print('1.→ Furia!')

		eleccion = input('\n:')
		if sujeto.race.__class__.__name__ == "Elf":
			if eleccion == "1":
				sujeto.race.mystic_fire(sujeto.mana, objetivo)
			elif eleccion == "2":
				sujeto.race.arcane_ritual(sujeto.xp, objetivo)
		elif sujeto.race.__class__.__name__ == "Human":
			if eleccion == "1":
				sujeto.race.last_breath(sujeto.hp, objetivo)
		elif sujeto.race.__class__.__name__ == "Dwarf":
			if eleccion == "1":
				sujeto.race.outrage(objetivo)
		else:
			print('Ingrese un número que corresponda a un ataque')
	


	def menu_combate(self, personaje, enemigo):
		print(f'{personaje.name} HP:{personaje.hp} mana:{personaje.mana}\n')
		print(f'Enemigo: {enemigo.name} HP:{enemigo.hp}')

		enemigo.recover_hp()

		print('\nElige una opcion\n')
		if personaje.__class__.__name__ == "Wizard":
			print('''1.→ Recuperar Maná \n2.→ Rafaga de energía \n3.→ Ataques de Raza \n4.→ Salir del entrenamiento''')

		elif personaje.__class__.__name__ == "Ladron":
			print('''1.→ Robar \n2.→ Ataques de Raza \n3.→ Salir del entrenamiento''')
	
		elif personaje.__class__.__name__ == "Archer":
			print('''1.→ Tiro especial \n2.→ Tiro de Larga Distancia \n3.→ Ataques de Raza  \n4.→ Salir del Entrenamiento''')

		menu_eleccion = input('\n:')



		if personaje.__class__.__name__ == "Wizard":
			if menu_eleccion == "1":
				personaje.recover_mana()
			elif menu_eleccion == "2":
				personaje.plasma_burst(enemigo)
			elif menu_eleccion == "3":
				self.ataques_razas(personaje, enemigo)
			elif menu_eleccion == "4":
				print('Saliendo del campo de entrenamiento')
				return False
			else:
				print('Ingrese un número que corresponda a un ataque')



		elif personaje.__class__.__name__ == "Ladron":
			if menu_eleccion == "1":
				personaje.robar(enemigo)
			elif menu_eleccion == "2":
				self.ataques_razas(personaje, enemigo)
			elif menu_elecciom == "3":
				print('Saliendo del campo de entrenamiento')
				return False
			else:
				print('Ingrese un número que corresponda a un ataque')



		elif personaje.__class__.__name__ == "Archer":
			if menu_eleccion == "1":
				personaje.special_attack(enemigo)
			elif menu_eleccion == "2":
				personaje.long_range_shot(enemigo)
			elif menu_eleccion == "3":
				self.ataques_razas(personaje, enemigo)
			elif menu_eleccion == "4":
				print('Saliendo del campo de entrenamiento')
				return False
			else:
				print('Ingrese un número que corresponda a un ataque')
		return True	
		input('...')		
		