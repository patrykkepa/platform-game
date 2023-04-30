from App.utils.settings import *

class PlayerEngine:
    def check_Player(self):
        player = self.player.sprite
        if player and player.rect.top > screen_height:
            player.rect.top = screen_height - tile_size*4
            player.rect.right = 200
            self.update_healthBar('subtract')
            self.check_Potion()