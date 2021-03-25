import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullet"""

    def __init__(self, ai_game):
        """create bullet obj at ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet at (0,0) position and assigning the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_with, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save bullet position in float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet to the top screen"""
        # renew bullet position in float format
        self.y -= self.settings.bullet_speed
        # renew rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """output bullet at the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
