
import pygame_menu
from pygame_menu.examples import create_example_window

from typing import Tuple, Any

surface = create_example_window('MENU - GRUPO AGL', (600, 400))

def start_the_game() -> None:

    global user_name

menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_ORANGE, 
    title='VAMOS CORRER ?',
    width=400
)

user_name = menu.add.text_input('Nome: ', default='       ', maxchar=10)
user_name = menu.add.text_input('Idade: ', default='', maxchar=2)
menu.add.selector('País: ', [('Brasil', 1), ('Argentina', 2), ('Chile', 3), ('Uruguai', 4), ('Paraguai', 5), ('Outro', 6)]) 
menu.add.button('Jogar', start_the_game)
menu.add.button('Sair', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)