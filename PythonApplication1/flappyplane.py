
import pygame
import random

pygame.init()

gamescreen = pygame.display.set_mode((800,480))
startscreen = pygame.display.set_mode((800,480))
pygame.display.set_caption('Hafsas Flappy Plane')
gameoverscreen = pygame.display.set_mode((800,480))

running = True
startrunning= True

fontt = pygame.font.Font("font.ttf" , 40)
font1 = pygame.font.Font("font.ttf" , 16)
gameover = pygame.font.Font("font.ttf" , 40)
restart = pygame.font.Font("font.ttf" , 16)

fontt = fontt.render("Hafsa's Flappy Plane", True ,(196, 154,132))
font1 = font1.render("Press Spacebar to continue..", True ,(196, 154,132))
gameover = gameover.render(" GAME OVER  :( ", True ,(196, 154,132))
restart = restart.render("Press Spacebar to retry :) ", True ,(196, 154,132))

background = pygame.image.load("background.png")
ground = pygame.image.load ("ground.png")
plane= pygame.image.load("red0.png")
obstacle1= pygame.image.load ("1.png")
obstacle2 = pygame.image.load ("0.png")

O1x = 692
O1y = 280   #241 normal
O2x = 480
O2y = -80   
planeX= 100
planeY=200
speed1 = 7
speed2 = 6

#def chooseObstacle (obstacle, yvalue):
#     if chosenobstacle== obstacle1:
#         yvalue == 241
#     elif chosenobstacle == obstacle2:
#         yvalue == 0

#     return yvalue
#randomspeed1 =random.choice (speed1)
#randomspeed2 =random.choice (speed2)

index = [0, 1 , 2 , 3]

y1value = [320, 290 , 300 , 350]
y2value = [-100, -40 , -80 , -90]
randomindex1 = random.choice(index)
randomindex2 = random.choice(index)
randomy1= y1value[randomindex1]
randomy2= y2value[randomindex2]

#obstacles= [obstacle1,obstacle2] 
#chosenobstacle = random.choice(obstacles)

def movepahar(O1x):
    #O1x=O1x-randomy1
    O1x=O1x-speed1
    return O1x

def moveuprwalapahar(O2x):
    #O2x = O2x-randomy2
    O2x = O2x-speed2
    return O2x

def moveplaneneechy (planeY):
    planeY = planeY+3
    return planeY

def moveplaneupr (planeY):
     planeY = planeY-100
     return planeY

def checkzameen():
    if (planeY > 420):
        return False
    else:
        return True
#def checkneechywaalyphaarkinok():
#    if (randomy1-239== planeY or randomy1 == planeY):
#        return False
#    else:
#        return True
    #if ( randomy1 == planeY):
    #    return False
    #else:
    #    return True
#def checkuprwaalyphaarkinok():
#    if (randomy2+239== planeY or randomy2 ==planeY):
#        return False
#    else:
#        return True
    #if (randomy2 ==planeY):
    #    return False
    #else:
    #    return True

    #start Screen 
while (startrunning == True):

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
         startrunning = False
      
      if event.type== pygame.KEYDOWN:
         if event.key==pygame.K_SPACE:
             startrunning= False
  
  

  pygame.display.flip()
  gamescreen.blit(background , (0,0))
  gamescreen.blit(ground, (0,409))
  gamescreen.blit(plane, (350,200))
  startscreen.blit(fontt , (150, 100))
  startscreen.blit(font1 , (250, 320))

#MAIN GAME LOOP
#def mainloop(running):
while (running==True):

     planeY = moveplaneneechy(planeY)
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                planeY =moveplaneupr(planeY)
        else:   
             planeY = moveplaneneechy(planeY)
  
         #collision checks
     if (checkzameen() == False):
         running= False 
     #if (checkneechywaalyphaarkinok() == False):
     #    running= False 
     #if (checkuprwaalyphaarkinok() == False):
     #    running= False 

     O1x = movepahar(O1x) 
     if (O1x <= -105):
         O1x = 790
         #chosenobstacle = random.choice(chooseObstacle(obstacles, O1y))
         randomy1= random.choice (y1value)
         O1x = movepahar(O1x)

     O2x = moveuprwalapahar(O2x)
     if (O2x <= -105):
        O2x = 790
        randomy2= random.choice (y2value)
        #chosenobstacle = random.choice(chooseObstacle(obstacles, O2y))
        O2x = moveuprwalapahar(O2x)

     pygame.display.flip()
     gamescreen.blit(background , (0,0))
    #screen.blit(chosenobstacle, (O1x,O1y))
    #screen.blit(chosenobstacle , (O2x,O2y))
     gamescreen.blit(obstacle1, (O1x,randomy1))
     gamescreen.blit(obstacle2 , (O2x,randomy2))
     gamescreen.blit(ground, (0,409))
     gamescreen.blit(plane, (planeX,planeY))

gameoverrunning=True
#Gameover Screen
while (gameoverrunning == True):
    
    pygame.display.flip()
    gameoverscreen.blit(background , (0,0))
    gameoverscreen.blit(ground, (0,409))
    gameoverscreen.blit(gameover , (170, 200))
    gameoverscreen.blit(restart , (250, 320))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
         gameoverrunning = False
      if event.type == pygame.KEYDOWN:
         if event.key==pygame.K_SPACE:
             running = True
             