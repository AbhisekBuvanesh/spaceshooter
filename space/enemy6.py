import pygame
import random
from constants import*
# tracks the enemy
class Enemy6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x = random.randint(0,SCREEN_WIDTH-HOMING_WIDTH)
        y = -100
        self.rect = pygame.Rect(x,y,HOMING_WIDTH,HOMING_HEIGHT)
        self.image = pygame.image.load("enemy6.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.damaged = pygame.image.load("enemy6damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        self.hurt = 0
        self.health = 2
    def update(self,enemies,bullets,sound,player):
        if player.rect.x < self.rect.x:
            self.rect.x -= 2
        if player.rect.x > self.rect.x:
            self.rect.x += 2
        if player.rect.y > self.rect.y:
            self.rect.y += 2
        if player.rect.y < self.rect.y:
            self.rect.y -= 2
        if self.health <= 0 or self.rect.y > SCREEN_HEIGHT:
            enemies.remove(self)


