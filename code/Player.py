from re import match

import pygame

from code.Entity import Entity
from code.const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name

    def update(self, ):
        pass

    def move(self, ):
        move_speed = ENTITY_SPEED[self.name]
        name = self.name
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[name]] and self.rect.y > 0:
            self.rect.centery -= move_speed
        if pressed_keys[PLAYER_KEY_DOWN[name]] and self.rect.y < WIN_HEIGHT - self.rect.height:
            self.rect.centery += move_speed
        if pressed_keys[PLAYER_KEY_LEFT[name]] and self.rect.x > 0:
            self.rect.centerx -= move_speed
        if pressed_keys[PLAYER_KEY_RIGHT[name]] and self.rect.x < WIN_WIDTH - self.rect.width:
            self.rect.centerx += move_speed
