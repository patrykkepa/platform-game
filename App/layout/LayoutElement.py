import pygame.sprite

from abc import ABC, abstractmethod

class LayoutElement(pygame.sprite.Sprite, ABC):
    def __init__(self, pos, *args):
      super().__init__()
      self.setup(pos, *args)
    
    @abstractmethod
    def setup(self, pos, *args):
        """self.image = pygame.image.load('')"""
        """self.rect = self.image.get_rect(topleft=pos)"""