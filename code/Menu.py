import pygame
from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect

from code.Const import WIN_WIDTH, C_RED, MENU_OPTION, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png").convert_alpha()  # Carrega a imagem do Bg do menu.
        self.rect = self.surf.get_rect(left=0, top=0)  # Cria o retangulo onde a imagem vai ser desenhada.

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load("./asset/Menu.wav")  # Carrega a musica do menu
        pygame.mixer_music.play(-1) # Toca a música do menu

        while True:
            # DESENHA IMAGENS
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem do Bg no retangulo.
            self.menu_text(70, "Sky", C_RED, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, "Shooter", C_RED, ((WIN_WIDTH / 2), 110))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_RED, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()


            # CHECA TODOS OS EVENTOS
            for event in pygame.event.get():

                # Evento QUIT
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha Janela
                    exit()  # Encerra o Pygame

                #Evento Pressionar Teclas
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option +=1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION)-1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)  # Define fonte e tamanho do texto.
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()  # Renderiza o texto como imagem (surface).
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Cria o retangulo.
        self.window.blit(source=text_surf, dest=text_rect)  # Desennha o texto na tela.
