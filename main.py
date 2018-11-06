# Imports
import pygame
import player
import settings

class Game():
    """
    This class handles control flow and rendering.
    Game loop, screen updating, etc
    """
    def __init__(self):
        self.is_running = True
        self.key = pygame.key.get_pressed()
        self.bg_img = pygame.image.load("Background.png").convert()
        self.window = pygame.display.get_surface()

    def event_loop(self):
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                self.is_running = False
        player.key_handler()

    def render(self):
        """
        Render background and game surface
        """
        self.bg_img = pygame.transform.scale(self.bg_img, settings.SCREEN_SIZE)
        self.window.blit(self.bg_img, (0, 0))
        player.draw_player(self.window)
        pygame.display.update()

    def main(self):
        while self.is_running:
            settings.CLOCK.tick(settings.FPS)
            self.event_loop()
            self.render()
            player.update()
# Create player instance
player = player.Player()


def main():
    pygame.init()
    pygame.display.set_mode(settings.SCREEN_SIZE)
    Game().main()
    pygame.quit()


main()
