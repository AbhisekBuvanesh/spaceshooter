import pygame
from constants import*
import random
from enemy6 import *
from enemyBullet import *
# Enemy that moves downwards and shoots 4 bullets and a lazer
class Enemy7(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(SCREEN_WIDTH/2 - ENEMY7_WIDTH/2,-250, ENEMY7_WIDTH, ENEMY7_HEIGHT)
        self.image = pygame.image.load("booss.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.image = pygame.transform.rotate(self.image,180)
        self.damaged = pygame.image.load("boossdamaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        self.damaged = pygame.transform.rotate(self.damaged, 180)
        self.lazer= pygame.image.load("laser.png")
        self.lazer = pygame.transform.rotate(self.lazer,180)
        self.lazer = pygame.transform.scale(self.lazer,(30,SCREEN_HEIGHT-300))
        self.firingLazer = False
        self.speedX= 0
        self.speedY= ENEMY7_SPEED
        self.health = 40
        self.time = 0
        self.hurt = 0
        self.firing = 0
        self.fireTime = 0
        self.lazerTime = 0
        self.homingTime = 0
    def update(self,enemies,bullets,sound,player):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.y > 50 and self.speedY!= 0:
            self.firingLazer = True
            self.speedY = 0
            self.speedX = ENEMY7_SPEED
            self.firing = 1
        if self.rect.x < 0:
            self.speedX = -self.speedX
        if self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.speedX = -self.speedX
        if self.firing == 1 and self.fireTime <= 0:
            b1 = EnemyBullet(self.rect.x + 50, self.rect.y + self.rect.height / 2, -5, 10)
            b2 = EnemyBullet(self.rect.x + 80, self.rect.y + self.rect.height / 2, -3, 10)
            b3 = EnemyBullet(self.rect.x + self.rect.width - 50, self.rect.y + self.rect.height / 2, 5, 10)
            b4 = EnemyBullet(self.rect.x + self.rect.width - 80, self.rect.y + self.rect.height / 2, 3, 10)
            bullets.add(b1)
            bullets.add(b2)
            bullets.add(b3)
            bullets.add(b4)
            self.fireTime = 40
        if self.lazerTime < 0:
            self.firingLazer = not self.firingLazer
            self.lazerTime = 80
        if self.homingTime < 0:
            e = Enemy6()
            e.rect.x = self.rect.x + self.rect.width/2 - e.rect.width / 2
            e.rect.y = self.rect.y + self.rect.height/2 - e.rect.height / 2
            enemies.add(e)
            self.homingTime = 300
        self.fireTime -= 1
        self.lazerTime -= 1
        self.homingTime -= 1

        self.time += 1
    def hit(self,player):
        if pygame.sprite.collide_rect(self,player):
            return True
