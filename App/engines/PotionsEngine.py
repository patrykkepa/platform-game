import random

from App.utils.settings import *

from App.actors.Actor import Actor
from App.actors.Potion import Potion

class PotionsEngine:
    def setup_Potion(self):
      if self.current_life < self.initial_life:
          random_spot = random.randint(20, screen_width - 20)
          potion_sprite: Actor = Potion((random_spot, -50))
          self.potion.add(potion_sprite)

    def check_Potion(self):
      potion = self.potion.sprite or None
      if potion == None:
          self.setup_Potion()
      if potion != None and potion.rect.top > screen_height:
          self.setup_Potion()