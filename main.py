# Imports
import pygame
import player
import settings
import blocks


class Game:
    """
    This class handles control flow and rendering.
    Game loop, screen updating, etc
    """
    def __init__(self):
        pygame.init()
        self.is_running = True
        self.bg_img = pygame.image.load("Background.png").convert()
        self.bg_img = pygame.transform.scale(self.bg_img, settings.SCREEN_SIZE)    
        self.window = pygame.display.set_mode(settings.SCREEN_SIZE)

    def load(self):
        """
        Function creates an instance of all objects and classes
        """
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = player.Player(self)
        self.all_sprites.add(self.player)
        for platform in blocks.PLATFORMS:
            p = blocks.Platform(*platform)
            self.all_sprites.add(p)
            self.platforms.add(p)

    def draw(self):
        """
        Draw background, game surface, and all sprites
        """
        self.window.blit(self.bg_img, (0, 0))
        self.all_sprites.draw(self.window)
        pygame.display.update()

    def update(self):
        """
        Runs every loop and update game state
        """
        self.all_sprites.update()
        collide = pygame.sprite.spritecollide(self.player, self.platforms, False)
        if self.player.vel.y > 0:
            if collide:
                self.player.pos.y = collide[0].rect.top + 1
                self.player.vel.y = 0

    def event_loop(self):
        """
        Pygame event handler
        """
        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                self.is_running = False

    def main(self):
        """
        Main function for the game. Everything passes through here
        """
        self.load()
        while self.is_running:
            settings.CLOCK.tick(settings.FPS)
            self.event_loop()
            self.update()
            self.draw()


def main():
    pygame.display.set_mode(settings.SCREEN_SIZE)
    Game().main()
    pygame.quit()


main()
