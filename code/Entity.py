from abc import ABC, abstractmethod
import pygame

from code.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[name]
        self.damage = ENTITY_DAMAGE[name]
        self.last_dmg = 'None'
        self.score = ENTITY_SCORE[name]

    @abstractmethod
    def move(self, ):
        pass
