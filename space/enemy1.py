import pygame
from constants import*
import random
from enemyBullet import *
# moves downwards from the top of the screen and shoots three bullets
class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0,SCREEN_WIDTH-ENEMY1_WIDTH),-100,ENEMY2_WIDTH,ENEMY2_HEIGHT)
        self.image = pygame.image.load("enemy1.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.damaged = pygame.image.load("enemy1damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        self.speedx= 0
        self.speedY= ENEMY1_SPEED
        self.health = 3
        self.time = 0
        self.hurt = 0
    def update(self,enemies,bullets,sound,player):
        self.rect.x += self.speedx
        self.rect.y += self.speedY
        if self.speedY == 0 and self.time % 80 == 0:
            b1 = EnemyBullet(self.rect.x+self.rect.width/2 - ENEMY_BULLET_WIDTH/2, self.rect.y + self.rect.height , 0,ENEMY_BULLET_SPEED)
            b2 = EnemyBullet(self.rect.x + self.rect.width / 2 - ENEMY_BULLET_WIDTH /2, self.rect.y + self.rect.height, -5,ENEMY_BULLET_SPEED)
            b3 = EnemyBullet(self.rect.x + self.rect.width / 2 - ENEMY_BULLET_WIDTH /2, self.rect.y + self.rect.height, 5,ENEMY_BULLET_SPEED)
            bullets.add(b1)
            bullets.add(b2)
            bullets.add(b3)
            sound.play()
        if self.rect.y+ENEMY2_HEIGHT > 150:
            self.speedY = 0
        if self.time > 600 and self.speedY == 0:
            self.image = pygame.transform.rotate(self.image, 180)
            self.speedY = -ENEMY1_SPEED
        if self.rect.y < -100:
            enemies.remove(self)
        if self.health <= 0:
            enemies.remove(self)
        self.time +=1