from code.Entity import Entity
from code.Const import ENTITY_SPEED


class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.name = name

    def move(self):
        self.rect.x -= ENTITY_SPEED[self.name]
