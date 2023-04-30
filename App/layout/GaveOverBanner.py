import pygame.sprite

from App.layout.LayoutElement import LayoutElement


class GameOverBanner(LayoutElement):
    def __init__(self, pos):
        super().__init__(pos)

    def setup(self, pos):
        self.image = pygame.image.load('Assets/gameover/gameover.png')
        self.rect = self.image.get_rect(topleft=pos)



