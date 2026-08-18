import datetime
import sys

import pygame
from pygame import Surface, Rect, K_RETURN
from pygame.constants import K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import SCORE_POS, MENU_OPTION, C_WHITE, C_RED
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/ScoreBg.png").convert_alpha()  # Carrega a imagem do Bg do Score.
        self.rect = self.surf.get_rect(left=0, top=0)  # Cria o retangulo onde a imagem vai ser desenhada.

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load("./asset/Score.mp3")  # Carrega a musica do Score
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        text = ''
        name = ''
        score = 0

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem do Bg no retangulo.

            # Desenha textos na tela
            self.score_text(48, 'You Win!!', C_WHITE, SCORE_POS['Title'])
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            # Score em modos de game diferentes
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Your name (4 characters):'
            if game_mode == MENU_OPTION[1]:
                score = player_score[0] + player_score[1]
                text = 'Enter Team name (4 characters):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formated_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode  # Evento de tecla / escreve o nome
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load("./asset/Score.mp3")  # Carrega a musica do Score
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_RED, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', C_RED, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', C_RED,
                            SCORE_POS[list_score.index(player_score)])


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()



    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",
                                              size=text_size)  # Define fonte e tamanho do texto.
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()  # Renderiza o texto como imagem (surface).
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)  # Cria o retangulo.
        self.window.blit(source=text_surf, dest=text_rect)  # Desennha o texto na tela.


def get_formated_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f'{current_time} - {current_date}'
