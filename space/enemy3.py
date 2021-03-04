import pygame
import random
from constants import*
from enemyBullet import *
# moves down along the sides and shoots bullets left or right
class Enemy3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.r = random.randint(0,1)
        x= SCREEN_WIDTH+100
        if self.r == 0:
            x = -100
        self.rect = pygame.Rect(x,0,ENEMY3_WIDTH,ENEMY3_HEIGHT)
        self.image = pygame.image.load("enemy3.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.hurt = 0
        self.damaged = pygame.image.load("enemy3damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        if self.r == 0:
            self.image=pygame.transform.rotate(self.image,-90)
            self.damaged = pygame.transform.rotate(self.damaged, -90)
        else:
            self.image=pygame.transform.rotate(self.image,90)
            self.damaged = pygame.transform.rotate(self.damaged, 90)
        self.speedY= ENEMY3_SPEED
        self.speedX= ENEMY3_SPEED
        if self.r == 1:
            self.speedX = -self.speedX
        self.health = ENEMY3_HEALTH
        self.time = 0
    def update(self,enemies,bullets,sound,player):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.speedX > 0 and self.rect.x + self.rect.width >= 100:
            self.speedX = 0
        if self.speedX < 0 and self.rect.x < SCREEN_WIDTH - 100 :
            self.speedX = 0
        if self.health <= 0 or self.rect.y > SCREEN_HEIGHT:
            enemies.remove(self)
        self.time += 1
        if self.time% 50 == 0:
            if self.r == 0:
                b = EnemyBullet(self.rect.x + self.rect.width,self.rect.y+ self.rect.height/2- BULLET_HEIGHT/2,ENEMY_BULLET_SPEED,0)
            else:
                b = EnemyBullet(self.rect.x, self.rect.y + self.rect.height / 2 - BULLET_HEIGHT/2, -ENEMY_BULLET_SPEED, 0)
            sound.play()
            bullets.add(b)

