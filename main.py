# Imports
import pygame
import sys
import player

# Initialize pygame
pygame.init()

# Global constants
SCREEN_WIDTH = 620
SCREEN_HEIGHT = 480
IS_RUNNING = True

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window and background
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("Background.png").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pyformer")

player = player.Player(100, 100)

# Main game loop
while IS_RUNNING:
    for Event in pygame.event.get():
        if Event.type == pygame.QUIT:
            IS_RUNNING = False

    DISPLAYSURF.blit(background, (0,0))
    player.draw_player(DISPLAYSURF, WHITE)
    pygame.display.update()