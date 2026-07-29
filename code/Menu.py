import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect

from code.const import WIN_WIDTH, COLOR_RED, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png")  # Carrega a imagem do Bg do menu.
        self.rect = self.surf.get_rect(left=0, top=0)  # Cria o retangulo onde a imagem vai ser desenhada.

    def run(self, ):
        pygame.mixer_music.load("./asset/Menu.wav")  # Carrega a musica do menu
        pygame.mixer_music.play(-1) # Toca a música do menu

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem do Bg no retangulo.
            self.menu_text(70, "Sky", COLOR_RED, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, "Shooter", COLOR_RED, ((WIN_WIDTH / 2), 110))

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(25, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Checa todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha Janela
                    exit()  # Encerra o Pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)  # Define fonte e tamanho do texto.
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderiza o texto como imagem (surface).
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Cria o retangulo.
        self.window.blit(source=text_surf, dest=text_rect)  # Desennha o texto na tela.
