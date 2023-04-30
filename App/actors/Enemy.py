import random

import pygame
from App.actors.Actor import Actor
from App.utils.support import import_folder


class Enemy(Actor):
    def __init__(self, pos):
        super().__init__()

        # Enemy assets
        self.import_actor_assets('./Assets/enemy/', ['fly'])
        self.image = self.animations['fly'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)

        # Enemy movement
        self.speed = random.randint(3,5)
        self.gravity = 0.0

        # Enemy default status
        self.status = 'fly'


    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        self.direction.x = 1



    def update(self):
        self.animate()
        self.rect.x += self.speed