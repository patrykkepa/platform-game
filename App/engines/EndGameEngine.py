import pygame
import sys

from App.utils.settings import *

from App.layout.LayoutElement import LayoutElement
from App.layout.GaveOverBanner import GameOverBanner

class EndGameEngine:
    def kill_game_actors(self):
        player = self.player.sprite
        if player and self.current_life <= 0:
            self.player.sprite.kill()
        potion = self.potion.sprite
        if potion and self.current_life <= 0:
            self.potion.sprite.kill()
        
        if player and self.current_life <= 0:
            self.end_time = pygame.time.get_ticks()

    def end_screen(self):
        if self.current_life <= 0:
            gameOverBanner_sprite: LayoutElement = GameOverBanner((screen_width / 2 - gameOverBanner_width / 2, screen_height / 2 - gameOverBanner_height / 2))
            self.gameOverBanner.add(gameOverBanner_sprite)
            self.gameOverBanner.draw(self.display_surface)

            # button setup
            self.color = (255, 255, 255)
            self.color_light = (170, 170, 170)
            self.color_dark = (100, 100, 100)
            self.smallfont = pygame.font.SysFont('Raleway', 35, bold=True)
            self.text = self.smallfont.render('RESET', True, self.color)
            self.scoreText = self.smallfont.render(f'Your score: {str(self.score)}, Time: {str(abs(round(self.current_time - self.end_time, 1))/1000)}', True, self.color_dark)
            self.offset_y = gameOverBanner_height/2 + 50

            # score
            self.display_surface.blit(self.scoreText, (screen_width / 2 - 280 / 2, button_height / 2 + 7 + self.offset_y))

            # button
            for i in range(4):
                pygame.draw.rect(self.display_surface, self.color_dark, (
                screen_width / 2 - button_width / 2 - i, screen_height / 2 - button_height / 2 + self.offset_y - i,
                button_width, button_height), 1)
            self.display_surface.blit(self.text, (
            screen_width / 2 - 80 / 2, screen_height / 2 - button_height / 2 + 7 + self.offset_y))

            mouse = pygame.mouse.get_pos()
            if screen_width / 2 - button_width / 2 <= mouse[
                0] <= screen_width / 2 - button_width / 2 + button_width and screen_height / 2 - button_height / 2 + self.offset_y <= \
                    mouse[1] <= screen_height / 2 - button_height / 2 + self.offset_y + button_height:
                for i in range(4):
                    pygame.draw.rect(self.display_surface, self.color_light, (
                        screen_width / 2 - button_width / 2 - i, screen_height / 2 - button_height / 2 + self.offset_y - i,
                        button_width, button_height), 1)

            # button input
            mouse = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    if screen_width / 2 - button_width / 2 <= mouse[
                        0] <= screen_width / 2 - button_width / 2 + button_width and screen_height / 2 - button_height / 2 + self.offset_y <= \
                            mouse[1] <= screen_height / 2 - button_height / 2 + self.offset_y + button_height:
                        self.display_welcome = True

    def end_game(self):
        if self.display_welcome == True:
            return self.display_welcome