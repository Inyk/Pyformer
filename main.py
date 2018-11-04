# Imports
import pygame
import player
import settings

# Create player instance
player = player.Player(100, 100)


class Game():
    """
    This class handles control flow and rendering.
    Game loop, screen updating, etc
    """
    def __init__(self):
        self.fps = 30
        self.is_running = True
        self.key = pygame.key.get_pressed()
        self.bg_img = pygame.image.load("Background.png").convert()
        self.window = pygame.display.get_surface()
        self.deltatime = 0

    def event_loop(self):
            for Event in pygame.event.get():
                if Event.type == pygame.QUIT:
                    self.is_running = False

    def render(self):
        """
        Render background and game surface
        """
        self.bg_img = pygame.transform.scale(self.bg_img, settings.SCREEN_SIZE)
        self.window.blit(self.bg_img, (0, 0))
        player.draw_player(self.window, settings.WHITE)
        pygame.display.update()

    def main(self):
        while self.is_running:
            self.event_loop()
            self.render()
            self.key_handler()


def main():
    pygame.init()
    pygame.display.set_mode(settings.SCREEN_SIZE)
    Game().main()
    pygame.quit()


main()