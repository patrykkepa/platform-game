import pygame
from App.layout.LayoutElement import LayoutElement

class Tile(LayoutElement):
    def __init__(self, pos, size_x, size_y, tile_name):
        super().__init__(pos, size_x, size_y, tile_name)
        
    def setup(self, pos, size_x, size_y, tile_name):
        self.image = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
        tile = pygame.image.load(tile_name).convert_alpha()
        self.image.blit(tile, (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

