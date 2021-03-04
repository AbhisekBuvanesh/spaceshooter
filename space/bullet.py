import pygame
from constants import*
class Bullet(pygame.sprite.Sprite):
    def __init__(self,player,speedX):
        super().__init__()
        self.speedX = speedX
        self.rect = pygame.Rect(player.rect.x+player.rect.width/2-BULLET_WIDTH/2,player.rect.y-BULLET_HEIGHT,BULLET_WIDTH,BULLET_HEIGHT)
        self.image = pygame.image.load("bullet.png")
        self.damaged = pygame.image.load("enemy6damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.speed= -BULLET_SPEED
        self.health = 1
        self.damaged = False
        #This is how the player is created.
    def update(self,bullets):
        self.rect.x += self.speedX
        self.rect.y += self.speed
        if self.rect.y + self.rect.height < 0:
            bullets.remove(self)
