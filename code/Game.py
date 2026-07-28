import pygame

from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load("./asset/Menu.wav")  # Carrega a musica do menu
        pygame.mixer_music.play(-1) # Toca a música do menu

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

        #     # Checa eventos
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit() # Fecha Janela
        #             exit() # Encerra o Pygame
