import pygame


class Ship:
    """Class for ship control."""

    def __init__(self, ai_game):
        """Ship initializig and start position."""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # All nes ships start from lower
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship in current position."""
        self.screen.blit(self.image, self.rect)
