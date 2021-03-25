import pygame


class Ship:
    """Class for ship control."""

    def __init__(self, ai_game):
        """Ship initializig and start position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # All new ships start from lower
        self.rect.midbottom = self.screen_rect.midbottom
        # Save ship coords
        self.x = float(self.rect.x)
        # flag for moving
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update x position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update rect
        self.rect.x = self.x

    def blitme(self):
        """Draw ship in current position."""
        self.screen.blit(self.image, self.rect)
