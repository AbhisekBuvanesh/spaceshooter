import pygame
from constants import*
import random
from enemyBullet import *
# This is the enemy that moves from the right corner down to the middle and back to the left corner
class Enemy4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(-80,-80,SNAKE_WIDTH,SNAKE_HEIGHT)
        self.image = pygame.image.load("enemy4.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.image = pygame.transform.rotate(self.image, 180)
        self.damaged = pygame.image.load("enemy4damaged.png")
        self.damaged = pygame.transform.scale(self.damaged, (self.rect.width, self.rect.height))
        self.damaged = pygame.transform.rotate(self.damaged, 180)
        self.speedX= SNAKE_SPEED
        self.speedY= SNAKE_SPEED / 2
        self.health = 2
        self.time = 0
        self.hurt = 0
    def update(self,enemies,bullets,sound,player):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.x >= SCREEN_WIDTH / 2 and self.speedY > 0:
            self.speedY = -SNAKE_SPEED / 2
        if self.rect.x > SCREEN_WIDTH:
            enemies.remove(self)
        if self.health <= 0:
            enemies.remove(self)
        if self.time % 30 == 0 :
            b = EnemyBullet(self.rect.x + self.rect.width / 2 - ENEMY_BULLET_WIDTH / 2, self.rect.y + self.rect.height, 0, ENEMY_BULLET_SPEED)
            sound.play()
            bullets.add(b)
        self.time+=1

