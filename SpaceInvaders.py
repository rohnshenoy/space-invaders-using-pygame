import pygame
import math
import random

#initializing pygame
pygame.init()

#setting up the game window 
screen = pygame.display.set_mode((800,600))

#setting the icon and title of the window
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#setting background 
background = pygame.image.load("background.png")


#setting player image
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


#setting enemy image
# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#setting bullet image
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "redy"


# for displaying score 
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',32)#freesansbold.ttf is name of the font and .ttf is the extension of font ttf - TrueType font 

textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
  over_text = over_font.render("GAME OVER", True, (255, 255, 255))
  screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x,y):
  screen.blit(playerImg,(x,y))

def enemy(x,y,i):
  screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
  global bullet_state
  bullet_state = "fire"
  screen.blit(bulletImg,(x+16,y+10))
  #here x+16 , y+10 because the bullet should appear like its firing from the nose of the spaceship.
  #if only x,y then it appears like bullet is firing from left side of the spaceship.


def isCollision(enemyX,enemyY,bulletX,bulletY):
  #formula for distance btw 2 points is d=√((x2 – x1)² + (y2 – y1)²).
  distance = math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
  if distance < 27 :
    return True
  else:
    return False




#Game loop
running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
      if  event.type == pygame.QUIT:
          running = False


    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        playerX_change = -3
      if event.key == pygame.K_RIGHT:
        playerX_change = 3
      if event.key == pygame.K_UP:
        bulletX = playerX
        fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
      if event.key ==pygame.K_LEFT or event.key == pygame.K_RIGHT:
        playerX_change = 0

      

    playerX += playerX_change

    if playerX <= 0 :
      playerX = 0
    if playerX >= 736 :
      playerX = 736 


    for i in range(num_of_enemies):

      # Game Over
      if enemyY[i] > 440:
          for j in range(num_of_enemies):
              enemyY[j] = 2000
          game_over_text()
          break
        
      enemyX[i] += enemyX_change[i]
      if enemyX[i] <= 0 :
        enemyX_change[i] = 2
        enemyY[i] += enemyY_change[i]
      elif enemyX[i] >= 736 :
        enemyX_change[i] = -2
        enemyY[i] += enemyY_change[i]

      #for collision 
      collison = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
      if collison:
        bulletY = 480 
        bullet_state = "ready"
        score_value += 1
        enemyX[i] = random.randint(0,736)
        enemyY[i] = random.randint(50,150)
      enemy(enemyX[i],enemyY[i],i)

    #bullet movement 
    if bulletY <= 0 :
      bulletY = 480
      bullet_state = "ready"


    if bullet_state in "fire":
      fire_bullet(bulletX,bulletY)
      bulletY -= bulletY_change


    



    player(playerX,playerY)
    show_score(textX, textY)
    




    pygame.display.update()