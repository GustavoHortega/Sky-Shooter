import pygame

from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

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

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
