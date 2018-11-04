# Imports
import pygame
import player
import settings
import sys

# Create player instance
player = player.Player(100, 100)

class Game:
    """
    This class handles control flow and rendering.
    Game loop, screen updating, etc
    """
    def __init__(self):
        self.fps(30)
        self.is_running = True
        self.key = pygame.key.get_pressed()
        self.background_image = pygame.image.load("Bacground.png").convert()
        self.window = pygame.display.set_mode(settings.SCREEN_SIZE)

    def event_loop(self):
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    self.is_running = False

    def render(self):
        """
        Render background and game surface
        """
        self.window
        self.background_image = pygame.transform.scale( self.background_image,
                                                        settings.SCREEN_SIZE)
        self.window.blit(self.background_image, (0, 0))
        self.widndow.blit(self.background_image, (0, 0))
        pygame.display.update()

    def key_handler(self):
        while self.is_running:
            if self.key[pygame.K_LEFT]:
                player.move_left()
            if self.key[pygame.K_RIGHT]:
                player.move_right()

    def main(self):
        while self.is_running:
            self.event_loop()
            self.render()
            self.key_handler()


def main():
    pygame.init()
    Game.main()
    pygame.quit()
