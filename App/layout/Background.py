import pygame
from App.utils.settings import *

class Background:
    def __init__(self, surface):
        self.display_surface = surface
        self.setup_background(self.display_surface)


    def setup_background(self, display_surface):
        self.bg_surface_sea = pygame.image.load('Assets/background/sea.png')
        self.bg_surface_deep_sea = pygame.image.load('Assets/background/deep_sea.png')
        self.bg_surface_deep_sea = pygame.transform.scale(self.bg_surface_deep_sea, (deep_sea_size_x, 160))
        self.bg_surface_clouds = pygame.image.load('Assets/background/clouds.png')
        self.bg_surface_sky = pygame.image.load('Assets/background/sky.png')
        self.bg_surface_sky = pygame.transform.scale(self.bg_surface_sky, (400, 500))

    def run(self):
        for i in range(0, screen_width):
            self.display_surface.blit(self.bg_surface_sky, (i * 400, 0))
        for i in range(0, screen_width):
            self.display_surface.blit(self.bg_surface_clouds, (i * 816, screen_height - clouds_size_y - sea_size_y - deep_sea_size_y*1.25))
            self.display_surface.blit(self.bg_surface_deep_sea, (i * 190, screen_height - deep_sea_size_y*2))
            self.display_surface.blit(self.bg_surface_sea, (i * 190, screen_height - sea_size_y-deep_sea_size_y*1.25))
