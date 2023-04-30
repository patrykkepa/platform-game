import sys
import pygame
import random

# Parent classes
from App.actors.Actor import Actor
from App.actors.ActorLive import ActorLive
from App.engines.EndGameEngine import EndGameEngine
from App.engines.GameBoardEngine import GameBoardEngine
from App.layout.LayoutElement import LayoutElement

# Engines
from App.engines.CollisionsEngine import CollisionsEngine
from App.engines.EnemiesEngine import EnemiesEngine
from App.engines.HealthBarEngine import HealthBarEngine
from App.engines.PlayerEngine import PlayerEngine
from App.engines.PotionsEngine import PotionsEngine

from App.layout.Tiles import Tile
from App.actors.Player import Player
from App.actors.Potion import Potion
from App.actors.Enemy import Enemy
from App.layout.HealthBar import HealthBar
from App.layout.GaveOverBanner import GameOverBanner
from App.utils.settings import *



class Game(GameBoardEngine,
            CollisionsEngine, 
            PlayerEngine, 
            PotionsEngine, 
            EnemiesEngine, 
            HealthBarEngine, 
            EndGameEngine):

    def __init__(self, level_map, surface, difficulty_level):
        # game setup
        self.display_surface = surface
        self.difficulty_level = difficulty_level
        self.display_welcome = False
        self.setup_level(level_map)
        self.current_x = 0
        self.score = 0
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.current_time = pygame.time.get_ticks()


    def run(self):
        # tiles
        self.tiles.update()
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.check_Player()
        self.player.draw(self.display_surface)

        # healthBar
        self.healthBar.draw(self.display_surface)

        # potion
        self.check_Potion()
        self.potion.draw(self.display_surface)

        # enemies
        self.check_enemies()
        self.setup_enemies()
        self.enemies.update()
        self.enemies.draw(self.display_surface)

        # end game
        self.kill_game_actors()
        self.end_screen()

        self.end_game()

