import pygame
import random 
import math
from pygame import mixer
pygame.init()

#create a screen
screen = pygame.display.set_mode((800,500))

background = pygame.image.load('bg3.jpg')
# BACKGROUND SOUND
mixer.music.load('background.wav')
mixer.music.play(-1)
#title and Icon
pygame.display.set_caption('space invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


#player
playerimg = pygame.image.load('UFO.png')
playerX = 200
playerY = 430
pos = 0


# enemy
enemyimg = []
enemyX = []
enemyY = []
posenX = []
posenY = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien1.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    posenX.append(1)
    posenY.append(40)



# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 430
bulletposX = 0
bulletposY = 3
bullet_state = "ready"

# score 
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

over = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render('Score:' + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over():
    over_font = over.render('GAME OVER',True,(255,255,255))
    screen.blit(over_font,(200,250))
    
def player(x,y):
    screen.blit(playerimg ,(x,y))

    
    
def enemy(x,y,i):
    
    screen.blit(enemyimg[i],(x,y))
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg ,(x + 16, y + 10))
    
def iscollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY - bulletY,2))
    if distance < 27:
        return True
    else:
        return False
    

#gamelooop
run = True
while run:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                pos = -2
            if event.key == pygame.K_RIGHT:
                pos = 2
            
            if event.key == pygame.K_SPACE and bullet_state is "ready":
                bulletX = playerX
                bullet_sound = mixer.Sound('Laser.wav')
                bullet_sound.play()
                fire_bullet(playerX,bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pos = 0
                
    # player            
    playerX += pos
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800-64:
        playerX = 800-64
    #enemy
    for i in range(num_of_enemies):
        if enemyY[i] > 370:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += posenX[i]
        if enemyX[i] <= 0:
            posenX[i] = 1
            enemyY[i] += posenY[i]
        elif enemyX[i] >= 800-64:
            posenX[i] = -1
            enemyY[i] += posenY[i]
        collision = iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 430
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i] , i)

        
#     bullet
    if bulletY <= 0:
        bulletY = 430
        bullet_state = "ready"
    
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletposY
        
    #collision
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
pygame.quit()