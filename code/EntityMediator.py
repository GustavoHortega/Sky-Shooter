from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.PlayerShot import PlayerShot
from code.const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # Metodo privado / Verifica quando sai da tela
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, PlayerShot):
            if ent.rect.right >= WIN_WIDTH:
                ent.health = 0

        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]): # Verifica colisao
        for i in range(len(entity_list)):
            entity_test = entity_list[i]
            EntityMediator.__verify_collision_window(entity_test)

    @staticmethod
    def verify_health(entity_list: list[Entity]): # Verifica vida da entidade e destroi
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
