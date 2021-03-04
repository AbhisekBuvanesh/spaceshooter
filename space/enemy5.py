import pygame
from constants import*
import random
from enemyBullet import *
# Enemy that moves downwards and shoots 4 bullets
class Enemy5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - ENEMY5_WIDTH), -100, ENEMY5_WIDTH, ENEMY5_HEIGHT)
        self.image = pygame.image.load("enemy5.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.damaged = pygame.image.load("enemy5damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        self.speedX= 0
        self.speedY= ENEMY5_SPEED
        self.health = 5
        self.time = 0
        self.hurt = 0
    def update(self,enemies,bullets,sound,playe):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.health <= 0 or self.rect.y > SCREEN_HEIGHT:
            enemies.remove(self)
        self.time += 1
        if self.time% 50 == 0:
            b1 = EnemyBullet(self.rect.x+self.rect.width/2 - ENEMY_BULLET_WIDTH/2, self.rect.y + self.rect.height/2 -ENEMY_BULLET_HEIGHT/2 , 5,ENEMY_BULLET_SPEED)
            b2 = EnemyBullet(self.rect.x+self.rect.width/2 - ENEMY_BULLET_WIDTH/2, self.rect.y + self.rect.height/2 -ENEMY_BULLET_HEIGHT/2 , -5,ENEMY_BULLET_SPEED)
            b3 = EnemyBullet(self.rect.x+self.rect.width/2 - ENEMY_BULLET_WIDTH/2, self.rect.y + self.rect.height/2 -ENEMY_BULLET_HEIGHT/2 , ENEMY_BULLET_SPEED,2)
            b4 = EnemyBullet(self.rect.x+self.rect.width/2 - ENEMY_BULLET_WIDTH/2, self.rect.y + self.rect.height/2 -ENEMY_BULLET_HEIGHT/2 , -ENEMY_BULLET_SPEED,-2)
            b5 = EnemyBullet(self.rect.x+self.rect.width/2 - ENEMY_BULLET_WIDTH/2, self.rect.y + self.rect.height/2 -ENEMY_BULLET_HEIGHT/2 , 0,-ENEMY_BULLET_SPEED)

            bullets.add(b1)
            bullets.add(b2)
            bullets.add(b3)
            bullets.add(b4)
            bullets.add(b5)
            sound.play()