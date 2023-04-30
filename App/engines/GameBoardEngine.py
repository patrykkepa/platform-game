import pygame

from App.utils.settings import *

from App.actors.ActorLive import ActorLive
from App.actors.Player import Player
from App.layout.Tiles import Tile

class GameBoardEngine:
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.potion = pygame.sprite.GroupSingle()
        self.healthBar = pygame.sprite.Group()
        self.gameOverBanner = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.time = 0

        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size + (screen_height - tile_size * len(level_map))

                if cell == 'P':
                    self.player_sprite: ActorLive() = Player((x, y))
                    self.player.add(self.player_sprite)
                if cell == '1':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_lt_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '2':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_rt_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '3':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_lb_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '4':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_rb_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '[':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_c_lt_tile.png')
                    self.tiles.add(ground_tile)
                if cell == ']':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_c_rt_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '{':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_c_lb_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '}':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_c_rb_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '5':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_e_t_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '6':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/ground_e_b_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '(':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/hang_lt_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '<':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/hang_lb_tile.png')
                    self.tiles.add(ground_tile)
                if cell == ')':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/hang_rt_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '>':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/hang_rb_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '-':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/small_l_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '_':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/small_r_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '=':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/big_l_tile.png')
                    self.tiles.add(ground_tile)
                if cell == '+':
                    ground_tile = Tile((x, y), tile_size, tile_size, './Assets/tiles/big_r_tile.png')
                    self.tiles.add(ground_tile)

        self.setup_healthBar()