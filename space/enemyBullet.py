import pygame
from constants import*
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,x,y,speedX,speedY):
        super().__init__()
        self.rect = pygame.Rect(x,y,ENEMY_BULLET_WIDTH,ENEMY_BULLET_HEIGHT)
        self.image = pygame.image.load("enemybullet.png")
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.speedX = speedX
        self.speedY = speedY
        #This is how the player is created.
    def update(self,bullets):

        self.rect.y += self.speedY
        self.rect.x += self.speedX
        if self.rect.x < -100 or self.rect.x > SCREEN_WIDTH +100 or self.rect.y < -100 or self.rect.y > SCREEN_HEIGHT +100:
            bullets.remove(self)

