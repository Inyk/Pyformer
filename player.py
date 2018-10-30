import pygame

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.speed = 5

    def draw_player(self, surface, color):
        self.image = pygame.draw.rect(surface, color, ( self.x, self.y, self.width, self.height ) )
    def move_left(self):
        self.x -= self.speed
    def move_right(self):
        self.x += self.speed