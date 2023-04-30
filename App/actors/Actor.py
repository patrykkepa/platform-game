import pygame.sprite
from App.utils.support import import_folder

class Actor(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        # Actor assets
        self.frame_index = 0
        self.animation_speed = 0.15

        # Actor movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.jump_speed = -16

        # Actor default status
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
    
    def import_actor_assets(self, path, animations_arr) -> None:
      character_path = path
      self.animations = {}
      for animation in animations_arr:
          self.animations[animation] = []

      for animation in self.animations.keys():
          full_path = character_path + animation
          self.animations[animation] = import_folder(full_path)
      
    
    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y