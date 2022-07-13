from models.character import Character, Elf, Human, Dwarf
from models.wizard import Wizard
from models.ladron import Ladron
from models.archer import Archer
from models.enemies import PracticeTarget
from models.menu import Menu
import random
import os
import sys




def limpiar_pantalla():
    my_os=sys.platform
    if my_os == "win32":
        os.system("cls")
    elif my_os == "linux" or my_os == "darwin": # darwin para mac
        os.system("clear")





maniqui_practica = PracticeTarget()



print('Bienvenido a Monstruos y Mazmorras')
print("\n\n")
print("Para empezar crea tu personaje")
print("\n\n")



pj1 = Menu().crear_personaje()

pj1.race_modifiers()

pj1.guild = Menu().elegir_gremio()



print('''\nAntes de combatir, vamos al campo de entrenamiento

Aquí podras probar tus ataques con un maniquí de entrenamiento''')


input(''''Presiona cualquier tecla para continuar... 
''')
limpiar_pantalla()

menu = True

while menu:

	menu = Menu().menu_combate(pj1, maniqui_practica)


	limpiar_pantalla()