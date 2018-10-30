# Imports
import pygame
import sys
import player

from settings import *

# Create player instance
player = player.Player(100, 100)

def draw_surface(surface, background):
    surface.blit(background, (0, 0))

def main():
    # Initialize pygame
    pygame.init()
    
    # Window and background
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("Background.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pyformer")

    # Loop variable
    IS_RUNNING = True

    # Main game loop
    while IS_RUNNING:
        clock.tick(30)
        key = pygame.key.get_pressed()

        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:
                IS_RUNNING = False
        if key[pygame.K_LEFT]:
            player.move_left()
        if key[pygame.K_RIGHT]:
            player.move_right()

        draw_surface(DISPLAYSURF, background)
        player.draw_player(DISPLAYSURF, WHITE)
        pygame.display.update()
main()