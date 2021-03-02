import sys
import pygame
from settings import Settings
from ship import Ship


class Invasion:
    """"Class for control resource and game behavior."""

    def __init__(self):
        """Initializing the game and create game resource."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invasion")
        self.ship = Ship(self)

        # Screen color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main game cycle."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Handless key pressed and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Updating image on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # display the last drawn screen
        pygame.display.flip()


if __name__ == '__main__':
    # Create example and starting the game
    ai = Invasion()
    ai.run_game()
