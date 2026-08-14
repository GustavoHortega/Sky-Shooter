from code.Entity import Entity
from code.const import ENTITY_SPEED


class PlayerShot(Entity):
    def __init__ (self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name


    def move(self,):
        self.rect.x += ENTITY_SPEED[self.name]