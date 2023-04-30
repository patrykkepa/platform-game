import sys
import pygame
from App.utils.settings import *

# My classes
from App.layout.Background import Background
from App.Welcome import Welcome
from App.Game import Game

class App:
    def __init__(self):
      # General pygame setup
      pygame.init()
      self.clock = pygame.time.Clock()

      # Title and icon
      pygame.display.set_caption("Elden jumper")
      icon = pygame.image.load("Assets/icon.png")
      pygame.display.set_icon(icon)

      # Create the screen
      self.screen = pygame.display.set_mode((screen_width, screen_height))

      # Initial game setup
      self.background = Background(self.screen)
      self.is_welcome_open = True
      self.difficulty_level = None
    

    def display_welcome(self):
      # Ustaw widok powitalny i wyświetlaj go dpokóki gracz nie wybierze poziomu trudności
      self.welcome = Welcome(self.screen)
                
      while self.no_difficulty_level():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.background.run()
        self.welcome.run()

        self.difficulty_level = self.welcome.get_difficulty_level()
        pygame.display.update()
        self.clock.tick(60)

      self.is_welcome_open = False


    def display_game(self):
      # Ustaw grę i wyświetlaj grę dopóki gracz nie przegra rozgrywki
      self.game = Game(level_map, self.screen, self.difficulty_level)

      while not self.is_welcome_open:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

        self.background.run()
        self.game.run()

        self.is_welcome_open = self.game.end_game()
        pygame.display.update()
        self.clock.tick(60)

      self.difficulty_level = None


    def no_difficulty_level(self):
      if self.difficulty_level == None or self.difficulty_level == 0:
        return True
      return False
    
    
    def game_loop(self):
      # W nieskończonej pętli: albo wyświetlaj widok powitalny albo widok gry
      while True:
        match self.is_welcome_open:
          case True:
              self.display_welcome()
          case False:
            self.display_game()
    


    
    def run(self):
       self.game_loop()

          

    
    



