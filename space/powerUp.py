import pygame
from constants import*
import random
class PowerUp(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        x = random.randint(0, SCREEN_WIDTH - POWERUP_WIDTH)
        y = random.randint(0,SCREEN_HEIGHT - POWERUP_HEIGHT)
        self.rect = pygame.Rect(0,0, POWERUP_WIDTH, POWERUP_HEIGHT)
        self.image = pygame.image.load("powerUp1.png")
        if type == 3:
            self.image = pygame.image.load("heart.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.speedX= POWERUP_SPEED
        self.speedY= POWERUP_SPEED
        self.type = type


    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.y+self.rect.height >= SCREEN_HEIGHT or self.rect.y <= 0:
            self.speedY = -self.speedY
        if self.rect.x+ self.rect.width >= SCREEN_WIDTH or self.rect.x <= 0:
            self.speedX = -self.speedX