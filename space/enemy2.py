import pygame
from constants import*
import random
# moves upward from the bottom
class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0,SCREEN_WIDTH-ENEMY2_WIDTH),SCREEN_HEIGHT+100,ENEMY2_WIDTH,ENEMY2_HEIGHT)
        self.image = pygame.image.load("enemy2.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.speedx= 0
        self.speedy= -ENEMY2_SPEED
        self.health = 1
        self.hurt = 0
        self.damaged = pygame.image.load("enemy2damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
    def update(self,enemies,bullets,sound,player):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.y+ENEMY2_HEIGHT < 0:
            enemies.remove(self)
        if self.health <= 0:
            enemies.remove(self)
