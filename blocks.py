# This file is called blocks instead of platform because platform.Platform started confusing me
# Yes I'm reminding myself why I named a file the way I did

import pygame
import settings


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(settings.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height


PLATFORMS = [(0, settings.HEIGHT - 40, settings.WIDTH, 40),
             (settings.WIDTH / 2 - 50, settings.HEIGHT * 3/4, 100, 20)
             ]
