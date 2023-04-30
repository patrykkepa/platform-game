from App.utils.settings import *

from App.layout.LayoutElement import LayoutElement
from App.layout.HealthBar import HealthBar

class HealthBarEngine:
    def setup_healthBar(self):
        self.initial_life = self.player_sprite.initial_life
        self.current_life = self.player_sprite.current_life
        self.healthBar.update()
        for index in range(self.current_life):
            healthBar_sprite: LayoutElement = HealthBar((heart_width * index, 1))
            self.healthBar.add(healthBar_sprite)

    def update_healthBar(self, action):
        match action:
            case 'subtract':
                if self.current_life > 0:
                    self.healthBar.sprites()[self.current_life-1].kill()
                    self.current_life -= 1
            case 'add':
                healthBar_sprite = HealthBar((heart_width * self.current_life, 1))
                self.healthBar.add(healthBar_sprite)
                self.current_life += 1
            case _:
                pass