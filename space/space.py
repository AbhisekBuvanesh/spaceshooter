import pygame
from bullet import *
from player import *
from constants import *
from enemy2 import *
from enemy3 import *
from enemy1 import *
from enemy4 import *
from enemy5 import *
from enemy6 import *
from enemy7 import *
from powerUp import *
import time
pygame.init()
def game():
    #pygame.mixer.music.load("background.wav")
    #pygame.mixer.music.play(-1)
    bulletSound = pygame.mixer.Sound("bullet.wav")
    ebulletSound = pygame.mixer.Sound("ebullet.wav")
    clock = pygame.time.Clock()
    t = time.time()
    spawn = [
        [0,102],
        [5,3],
        [8,4],
        [10,3],
        [15,2],
        [16,3],
        [17,2],
        [18,3],
        [20,3],
        [20,2],
        [23,2],
        [25,100],
        [26,3],
        [29,4],
        [30,2],
        [32,2],
        [35,3],
        [37,3],
        [38,2],
        [39,4],
        [43,3],
        [48,3],
        [49,102],
        [50,1],
        [52,2],
        [53,2],
        [54,2],
        [55,2],
        [56,2],
        [57,2],
        [58,1],
        [60,4],
        [60,3],
        [61,101],
        [65,4],
        [67,3],
        [68,3],
        [69,1],
        [73,5],
        [75,4],
        [77,2],
        [78,3],
        [82,1],
        [90,7]
        ]
    FIRE_RATE = 25
    background = pygame.image.load("background2.jpg")
    background = pygame.transform.scale(background,(SCREEN_WIDTH,SCREEN_HEIGHT))

    multiShot = False
    spawnIndex = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    playing = True
    p = Player()
    bullets = pygame.sprite.Group()
    enemyBullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    boss = None
    firing = False
    powerUp = None
    lives = 3
    heartImage = pygame.image.load("heart.png")
    heartImage = pygame.transform.scale(heartImage,(40,40))
    scoreFont = pygame.font.SysFont("Arial", 24)
    gameOverFont = pygame.font.SysFont("Helvetica",50)
    gameOver = False
    while playing:
        if gameOver == True:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_e:
                        playing = False
                    if e.key == pygame.K_r:
                        t = time.time()
                        lives = 3
                        multiShot = False
                        FIRE_RATE = 25
                        p.x = SCREEN_WIDTH/2
                        p.y = SCREEN_HEIGHT/2
                        enemies = pygame.sprite.Group()
                        boss = None
                        gameOver = False
                        powerUp = None
            screen.fill((0, 0, 0))
            gameOverText = gameOverFont.render("You lost all your live!", False, (255, 255, 255))
            screen.blit(gameOverText, (300, 200))
            restart = gameOverFont.render(" Press r to try again!", False, (255, 255, 255))
            screen.blit(restart, (300, 300))
            exit = gameOverFont.render(" Press e to exit the game!", False, (255, 255, 255))
            screen.blit(exit,(300,400))
            pygame.display.update()
            continue
        screen.blit(background,(0,0))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                playing = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    p.speedx = -PLAYER_SPEED
                if e.key == pygame.K_d:
                    p.speedx = PLAYER_SPEED
                if e.key == pygame.K_w:
                    p.speedy = -PLAYER_SPEED
                if e.key == pygame.K_s:
                    p.speedy = PLAYER_SPEED
                if e.key == pygame.K_SPACE:
                    firing = True

            if e.type == pygame.KEYUP:
                if e.key == pygame.K_SPACE:
                    firing = False
                if e.key == pygame.K_a and p.speedx == -PLAYER_SPEED:
                    p.speedx = 0
                if e.key == pygame.K_d and p.speedx == PLAYER_SPEED:
                    p.speedx = 0
                if e.key == pygame.K_w and p.speedy == -PLAYER_SPEED:
                    p.speedy = 0
                if e.key == pygame.K_s and p.speedy == PLAYER_SPEED:
                    p.speedy = 0

        while spawnIndex < len(spawn) and spawn[spawnIndex][0]< time.time() - t:
            if spawn[spawnIndex][1] == 100:
                powerUp = PowerUp(1)
            if spawn[spawnIndex][1] == 101:
                powerUp = PowerUp(2)
            if spawn[spawnIndex][1] == 102:
                powerUp = PowerUp(3)

            if spawn[spawnIndex][1] == 2:
                e = Enemy2()
                enemies.add(e)
            if spawn[spawnIndex][1] == 3:
                e = Enemy3()
                enemies.add(e)
            if spawn[spawnIndex][1] == 1:
                e = Enemy1()
                enemies.add(e)
            if spawn[spawnIndex][1] == 4:
                e = Enemy4()
                enemies.add(e)
            if spawn[spawnIndex][1] == 5:
                e = Enemy5()
                enemies.add(e)
            if spawn[spawnIndex][1] == 6:
                e = Enemy6()
                enemies.add(e)
            if spawn[spawnIndex][1] == 7:
                boss = Enemy7()

            spawnIndex+=1
        if p.hurt > 0:
            screen.blit(p.damaged, (p.rect.x, p.rect.y))
        else:
            screen.blit(p.image, (p.rect.x, p.rect.y))
        p.lastFire += 1
        if p.lastFire > p.fireRate and firing == True:
            bullet = Bullet(p,0)
            if multiShot == True:
                bullet2 = Bullet(p,-5)
                bullet3 = Bullet(p,5)
                bullets.add(bullet2)
                bullets.add(bullet3)
            bullets.add(bullet)
            p.lastFire = True
            bulletSound.play()
        for b in bullets:
            screen.blit(b.image,(b.rect.x,b.rect.y))
            b.update(bullets)
        if boss!= None:
            if boss.hurt > 0:
                screen.blit(boss.damaged, (boss.rect.x, boss.rect.y))
                boss.hurt -= 1
            else:
                screen.blit(boss.image,(boss.rect.x,boss.rect.y))
            if boss.firingLazer:
                screen.blit(boss.lazer,(boss.rect.x + boss.rect.width/2 - 15, boss.rect.y + boss.rect.height - 30))

            boss.update(enemies,enemyBullets,ebulletSound,p)
        for e in enemies:
            if e.hurt > 0:
                screen.blit(e.damaged, (e.rect.x, e.rect.y))
                e.hurt -= 1
            else:
                screen.blit(e.image,(e.rect.x,e.rect.y))
            e.update(enemies,enemyBullets,ebulletSound,p)
        for b in enemyBullets:
            screen.blit(b.image, (b.rect.x, b.rect.y))
            b.update(enemyBullets)
        if powerUp!= None:
            screen.blit(powerUp.image,(powerUp.rect.x,powerUp.rect.y))
            powerUp.update()
        p.update()
        for i in range(lives):
            screen.blit(heartImage,(10+i*45,10))
        x = str(round(time.time()-t,2))
        timeText = scoreFont.render(x,False,(255,255,255))
        screen.blit(timeText,(SCREEN_WIDTH-100,10))

        #collisions
        if pygame.sprite.spritecollide(p,enemies, True)!= []:
            if p.hurt == 0:
                lives -= 1
                p.hurt = DAMAGED_TIME
        c = pygame.sprite.groupcollide(bullets,enemies,True,False)
        if pygame.sprite.spritecollide(p,enemyBullets,True)!= [] :
            if p.hurt == 0:
                lives -= 1
                p.hurt = DAMAGED_TIME
        if boss!= None:
            if pygame.sprite.spritecollide(boss,bullets,True)!= []:
                boss.health -=1
                boss.hurt = DAMAGED_TIME
            if boss.firingLazer == True:
                playerMiddle = p.rect.x + p.rect.width / 2
                bossMiddle = boss.rect.x + boss.rect.width / 2
                if playerMiddle > bossMiddle - 10 and playerMiddle < bossMiddle + 10:
                    if p.hurt == 0:
                        lives -= 1
                        p.hurt = DAMAGED_TIME
            if boss.hit(p):
                if p.hurt == 0:
                    lives -= 1
                    p.hurt = DAMAGED_TIME
        if powerUp!= None and pygame.sprite.collide_rect(p,powerUp) == True:
            if powerUp.type == 1:
                FIRE_RATE -= 6
            if powerUp.type == 2:
                multiShot = True
            if powerUp.type == 3:
                lives += 1
            powerUp = None
        for b in c:
            for e in c[b]:
                e.health -= 1
                e.hurt = DAMAGED_TIME
        if boss!= None and boss.health <= 0 :
            boss = None
        if lives < 1:
            gameOver = True
        pygame.display.update()
        clock.tick(50)
game()



