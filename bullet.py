import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullet control"""

    def __init__(self, ai_game):
        """create bullet obj at the current ship position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet at (0, 0) position and use correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_with, self.settings.bullet_with)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Bullet position at float.
        self.y = float(self.rect.y)


"""PARAM = "261 СТРАНИЦА"""
