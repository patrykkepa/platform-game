import sys
import pygame
from App.utils.settings import *

class Welcome:
    def __init__(self, surface):
        self.display_surface = surface
        # self.setup_background(self.display_surface)

        # white color
        self.color = (255, 255, 255)
        # light shade of the button
        self.color_light = (170, 170, 170)
        # dark shade of the button
        self.color_dark = (100, 100, 100)

        self.smallfont = pygame.font.SysFont('Raleway', 35, bold=True)

        self.text_easy = self.smallfont.render('EASY', True, self.color)
        self.text_hard = self.smallfont.render('HARD', True, self.color)

        # buttons offset
        self.easy_offset = 0
        self.hard_offset = button_height+20

        # logo
        self.logo = pygame.image.load('Assets/icon.png').convert_alpha()
        self.logo.set_alpha(150)
        self.logo = pygame.transform.scale(self.logo, (logo_width, logo_height))

        self.difficulty_level = 0


    def render_button(self, theme, hover_theme, text, text_x, offset_y):
        for i in range(4):
            pygame.draw.rect(self.display_surface, theme, (screen_width/2 - button_width/2 - i, screen_height/2 - button_height/2 + offset_y - i, button_width, button_height), 1)
        self.display_surface.blit(text,(screen_width / 2 - text_x / 2, screen_height / 2 - button_height / 2 + 7 + offset_y))

        mouse = pygame.mouse.get_pos()
        if screen_width/2 - button_width/2 <= mouse[0] <= screen_width/2 - button_width/2 + button_width and screen_height/2 - button_height/2 + offset_y <= mouse[1] <= screen_height/2 - button_height/2 + offset_y + button_height:
            for i in range(4):
                pygame.draw.rect(self.display_surface, hover_theme, (
                screen_width / 2 - button_width / 2 - i, screen_height / 2 - button_height / 2 + offset_y - i,
                button_width, button_height), 1)

    def get_input(self):
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # checks if a mouse is clicked
            if ev.type == pygame.MOUSEBUTTONDOWN:

                if screen_width/2 - button_width/2 <= mouse[0] <= screen_width/2 - button_width/2 + button_width and screen_height/2 - button_height/2 + self.easy_offset <= mouse[1] <= screen_height/2 - button_height/2 + self.easy_offset + button_height:
                    self.difficulty_level = 5
                if screen_width/2 - button_width/2 <= mouse[0] <= screen_width/2 - button_width/2 + button_width and screen_height/2 - button_height/2 + self.hard_offset <= mouse[1] <= screen_height/2 - button_height/2 + self.hard_offset + button_height:
                    self.difficulty_level = 10

    def get_difficulty_level(self):
        if self.difficulty_level != 0:
            return self.difficulty_level

    def run(self):
        self.display_surface.blit(self.logo, (screen_width/2 - logo_width/2, screen_height/2 - logo_height*1.5))
        self.render_button(self.color_dark, self.color_light,  self.text_easy, 70, self.easy_offset)
        self.render_button(self.color_dark, self.color_light, self.text_hard, 70, self.hard_offset)
        self.get_input()
        self.get_difficulty_level()


