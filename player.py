import pygame

class Player():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
    def draw_player(self, surface, color):
        self.image = pygame.draw.rect(surface, color, (200, 300, self.x, self.y))