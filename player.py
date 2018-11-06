import pygame
import settings

vector = pygame.math.Vector2

class Player():
    def __init__(self):
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((50,50))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = vector(tuple(x / 2 for x in settings.SCREEN_SIZE))
        self.is_left = False
        self.is_right = False
        self.is_jumping = False
        self.pos = vector(self.rect.center)
        self.vel = vector(0, 0)
        self.speed = vector(0, 0)
        self.accel = 0.5
        self.friction = -0.12

    def key_handler(self):
        self.speed = vector(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()
        if keys[pygame.K_SPACE]:
            self.jump()
    
    def update(self):
        self.speed += self.vel * self.friction
        self.vel += self.speed
        self.pos += self.vel + 0.5 * self.speed
        self.rect.center = self.pos
        
    def draw_player(self, window):
        window.blit(self.image, self.pos)

    def move_left(self):
        if self.pos.x > 0
            self.speed.x = -self.accel

    def move_right(self):
        if self.pos.x < (settings.WIDTH - self.width):
            self.speed.x = self.accel

    def jump(self):
        self.y = -1
