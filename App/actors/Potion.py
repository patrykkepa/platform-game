import pygame
from App.actors.Actor import Actor
from App.utils.support import import_folder


class Potion(Actor):
    def __init__(self, pos):
        super().__init__()

        # Potion assets
        self.import_actor_assets('./Assets/potion/', ['potion'])
        self.image = self.animations['potion'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # Potion movement
        self.gravity = 0.3

        # Potion default status
        self.status = 'potion'




