import pygame

from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import ENTITY_SPEED, ENTITY_SHOOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.left, self.rect.centery))
