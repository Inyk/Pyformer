"""
Imports and initialize
"""
import pygame
import sys

"""
Global constants
"""
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 480
IS_RUNNING = True

"""
Colors
"""
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("Background.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pyformer")

class Player():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
    def draw_player(self):
        self.image = pygame.draw.rect(DISPLAYSURF, WHITE, (200, 300, self.x, self.y))
player = Player(100, 100)
while IS_RUNNING:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            IS_RUNNING = False

    DISPLAYSURF.blit(background, (0,0))
    player.draw_player()
    pygame.display.update()