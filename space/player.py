import pygame
from constants import*
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.fireRate = FIRE_RATE
        self.lastFire = 0
        self.rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_WIDTH,PLAYER_HEIGHT)
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.damaged = pygame.image.load("playerdamaged.png")
        self.damaged = pygame.transform.scale(self.damaged,(self.rect.width,self.rect.height))
        self.speedx = 0
        self.speedy = 0
        self.hurt = 0
        #This is how the player is created.
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.rect.x =0
        if self.rect.y < 0:
            self.rect.y=0
        if self.rect.x+self.rect.width > SCREEN_WIDTH:
            self.rect.x = SCREEN_WIDTH - self.rect.width
        if self.rect.y + self.rect.height > SCREEN_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.rect.height
        if self.hurt > 0:
            self.hurt -= 1