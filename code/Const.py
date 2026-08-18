import pygame

# C
C_RED = (215, 38, 56)
C_WHITE = (255, 255, 255)
C_GREEN = (70, 160, 0)
C_ORANGE = (206, 101, 0)
# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Player1': 3,
    'Player1Shot': 8,
    'Player2': 3,
    'Player2Shot': 8,
    'Enemy1': 2,
    'Enemy1Shot': 4,
    'Enemy2': 1,
    'Enemy2Shot': 4,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
}

ENTITY_SHOOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 80,
    'Enemy2': 80,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 2,
    'Level1Bg2': 1,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 2,
    'Level2Bg2': 1,
    'Level2Bg3': 3,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 20,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 100,
    'Enemy2Shot': 0,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_RCTRL,
    'Player2': pygame.K_LCTRL
}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SPAWN_TIME = 1000

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'EnterName': (WIN_WIDTH / 2, 85),
    'Label': (WIN_WIDTH / 2, 90),
    'Name': (WIN_WIDTH / 2, 110),
    0: (WIN_WIDTH / 2, 110),
    1: (WIN_WIDTH / 2, 135),
    2: (WIN_WIDTH / 2, 155),
    3: (WIN_WIDTH / 2, 175),
    4: (WIN_WIDTH / 2, 195),
    5: (WIN_WIDTH / 2, 215),
    6: (WIN_WIDTH / 2, 235),
    7: (WIN_WIDTH / 2, 255),
    8: (WIN_WIDTH / 2, 275),
    9: (WIN_WIDTH / 2, 295),
}

# T
TIMEOUT_STEP = 100  # ms
TIMEOUT_LEVEL = 1000  # ms
