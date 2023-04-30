import random

from App.utils.settings import *

from App.actors.Actor import Actor
from App.actors.Enemy import Enemy

class EnemiesEngine:
    def setup_enemies(self):
        self.time += 60
        if len(self.enemies.sprites()) < self.difficulty_level and self.time == 2400:
            self.time = 0
            random_spot = random.randint(50, screen_height - 50)
            enemy_sprite: Actor = Enemy((0, random_spot))
            self.enemies.add(enemy_sprite)

    def check_enemies(self):
        for sprite in self.enemies.sprites():
            if sprite.rect.left > screen_width:
                self.reset_enemy(sprite)

    def reset_enemy(self, sprite):
        random_spot = random.randint(50, screen_height - 50)
        sprite.rect.right = 0
        sprite.rect.top = random_spot