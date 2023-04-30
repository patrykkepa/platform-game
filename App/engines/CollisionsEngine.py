

class CollisionsEngine:
    
    def horizontal_movement_collision(self):
      # player collision with tiles
      player = self.player.sprite
      if player:
          player.rect.x += player.direction.x * player.speed

          # player collision with tiles
          for sprite in self.tiles.sprites():
              if sprite.rect.colliderect(player.rect):
                  if player.direction.x < 0:
                      player.rect.left = sprite.rect.right
                      player.on_left = True
                      self.current_x = player.rect.left
                  elif player.direction.x > 0:
                      player.rect.right = sprite.rect.left
                      player.on_right = True
                      self.current_x = player.rect.right

          if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
              player.on_left = False
          if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
              player.on_right = False

          # player collision with potion
          for sprite in self.potion.sprites():
              if sprite.rect.colliderect(player.rect):
                  if player.direction.x < 0:
                      self.update_healthBar('add')
                      sprite.kill()
                  elif player.direction.x > 0:
                      self.update_healthBar('add')
                      sprite.kill()

          # player collision with enemies
          for sprite in self.enemies.sprites():
              if sprite.rect.colliderect(player.rect):
                  if player.direction.x < 0:
                      self.update_healthBar('subtract')
                      self.reset_enemy(sprite)
                      self.check_Potion()
                  elif player.direction.x > 0:
                      self.update_healthBar('subtract')
                      self.reset_enemy(sprite)
                      self.check_Potion()

          # enemies clossion with player
          enemies = self.enemies.sprites()
          for enemy in enemies:
              for sprite in self.player.sprites():
                  if sprite.rect.colliderect(enemy.rect):
                      if enemy.direction.x < 0:
                          self.update_healthBar('subtract')
                          self.reset_enemy(enemy)
                          self.check_Potion()
                      elif enemy.direction.x > 0:
                          self.update_healthBar('subtract')
                          self.reset_enemy(enemy)
                          self.check_Potion()


    def vertical_movement_collision(self):
      player = self.player.sprite
      if player:
          player.apply_gravity()

          # player collision with tiles
          for sprite in self.tiles.sprites():
              if sprite.rect.colliderect(player.rect):
                  if player.direction.y > 0:
                      player.rect.bottom = sprite.rect.top
                      player.direction.y = 0
                      player.on_ground = True
                  elif player.direction.y < 0:
                      player.rect.top = sprite.rect.bottom
                      player.direction.y = 0
                      player.on_ceiling = True

          if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
              player.on_ground = False
          if player.on_ceiling and player.direction.y > 0:
              player.on_ceiling = False

          # potion collision with tiles
          if(self.potion.sprite):
              potion = self.potion.sprite
              potion.apply_gravity()

              for sprite in self.tiles.sprites():
                  if sprite.rect.colliderect(potion.rect):
                      if potion.direction.y > 0:
                          potion.rect.bottom = sprite.rect.top
                          potion.direction.y = 0
                          potion.on_ground = True
                      elif potion.direction.y < 0:
                          potion.rect.top = sprite.rect.bottom
                          potion.direction.y = 0
                          potion.on_ceiling = True

              if potion.on_ground and potion.direction.y < 0 or potion.direction.y > 1:
                  potion.on_ground = False
              if potion.on_ceiling and potion.direction.y > 0:
                  potion.on_ceiling = False

              # player collision with potion
              for sprite in self.potion.sprites():
                  if sprite.rect.colliderect(player.rect):
                      if player.direction.y > 0:
                          self.update_healthBar('add')
                          sprite.kill()
                      elif player.direction.y < 0:
                          self.update_healthBar('add')
                          sprite.kill()

              # player collision with enemies
              for sprite in self.enemies.sprites():
                  if sprite.rect.colliderect(player.rect):
                      if player.direction.y > 0:
                          # self.update_healthBar('subtract')
                          self.score += 1
                          self.reset_enemy(sprite)
                          # self.check_Potion()
                      elif player.direction.y < 0:
                          self.update_healthBar('subtract')
                          self.reset_enemy(sprite)
                          self.check_Potion()

              # enemy collision with player
              enemies = self.enemies.sprites()
              for enemy in enemies:
                  for sprite in self.enemies.sprites():
                      if sprite.rect.colliderect(enemy.rect):
                          if enemy.direction.y > 0:
                              self.update_healthBar('subtract')
                              self.reset_enemy(enemy)
                              self.check_Potion()
                          elif enemy.direction.y < 0:
                              self.update_healthBar('subtract')
                              self.reset_enemy(enemy)
                              self.check_Potion()