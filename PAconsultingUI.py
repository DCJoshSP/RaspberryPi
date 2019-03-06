import pygame
import random
import math
import sys

pygame.init()
size = (800,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("UI")
done= False
clock = pygame.time.Clock()
stage = 1

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE =(50,50,255)
YELLOW = (255,255,0)
GREEN = (150,200,0)
LIGHTBLUE = (50,175,236)
RED = (255,50,50)
SKINCOLOUR = (235,160,130)
COLOUR = (150,200,0)
backGround = pygame.image.load("PaconsultingBG.png")
bicycleSpriteLeft = pygame.image.load("bicycleSpriteLeft.png")
bicycleSpriteRight = pygame.image.load("bicycleSpriteRight.png")
bicycleCurrent = bicycleSpriteRight
bicycleVelocity = random.randint(1,5)
bicycleSide = 0
bicycleX = -100
bicycleY = 404
myFont =  pygame.font.SysFont("Impact",20)
enterNewUserName = False
enterNewUserEmail = False
newUserName = ""
newUserEmail = ""
l = []
    
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if stage == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #checks the mouse to see if the user has clicked on a button
                mx, my = pygame.mouse.get_pos()
                if mx > 150 and mx < 300 and my >200 and my < 300:
                    stage = 2
                    print(stage)
                elif mx > 500 and mx < 650 and my>200 and my<300:
                    stage = 3
                    print(stage)
        elif stage == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 275 and mx < 550 and my > 240 and my <265:
                    enterNewUserName = True
                elif mx > 235 and mx < 550 and my > 270 and my < 295:
                    enterNewUserEmail = True
                if enterNewUserName == True:
                    if mx > 550 and mx < 600 and my > 250 and my < 265:
                        enterNewUserName = False
                        userName = newUserName #(userName) is where the user would input their new username, so change this to whatever you use in the main code!
                        newUserName = ""
                        l = []
                        print(userName)
                    elif mx > 610 and mx < 650 and my > 250 and my < 265:
                        enterNewUserName = False
                        newUserName = ""
                        l = []
                elif enterNewUserEmail == True:
                    if mx > 550 and mx < 600 and my > 270 and my < 285:
                        enterNewUserEmail = False
                        userEmail = newUserEmail #same above, but for the new user's email address this time.
                        newUserEmail = ""
                        l = []
                        print(userEmail)
                    elif mx > 610 and mx < 650 and my > 270 and my < 285:
                        enterNewUserEmail = False
                        newUserName = ""
                        l = []
            if enterNewUserName == True or enterNewUserEmail == True:  
                if event.type == pygame.KEYDOWN:
                    letterInput = pygame.key.name(event.key)
                    if enterNewUserName == True:
                        l.append(letterInput)
                        newUserName = ''.join(l)
                    if enterNewUserEmail == True:
                        l.append(letterInput)
                        newUserEmail = ''.join(l)
    screen.blit(backGround,(0,0))
    #calculates the bicycle's posistion and changes it
    if bicycleX > 801 or bicycleX < -101:
        bicycleSide = random.randint(0,1)
        bicycleVelocity = random.randint(1,5)
        if bicycleSide == 1:
            bicycleCurrent = bicycleSpriteLeft
            bicycleX = 800
        elif bicycleSide == 0:
            bicycleCurrent = bicycleSpriteRight
            bicycleX = -100
    else:
        if bicycleSide == 0:
            bicycleX = bicycleX + bicycleVelocity
        elif bicycleSide == 1:
            bicycleX = bicycleX - bicycleVelocity
    screen.blit(bicycleCurrent, (bicycleX,bicycleY))
    if stage == 1:
        pygame.draw.rect(screen, YELLOW , (150,200,150,100))
        pygame.draw.rect(screen, YELLOW , (500,200,150,100))
        screen.blit(myFont.render("CREATE NEW",1,BLUE),(175,235))
        screen.blit(myFont.render("LOG IN",1,BLUE),(550,235))
    elif stage == 2:
        screen.blit(myFont.render("Creating new acount:",1,BLUE),(100,200))
        pygame.draw.rect(screen, YELLOW, (275,260,275,5))
        screen.blit(myFont.render("Enter Username:",1,BLUE),(140,240))
        pygame.draw.rect(screen, YELLOW, (235,290,315,5))
        screen.blit(myFont.render("Enter Email:",1,BLUE),(140,270))
        if enterNewUserName == True:
            screen.blit(myFont.render("DONE",1,BLUE),(560,240))
            screen.blit(myFont.render("CANCEL",1,BLUE),(610,240))
            screen.blit(myFont.render(newUserName,1,BLUE),(275,235))
        elif enterNewUserEmail == True:
            screen.blit(myFont.render("DONE",1,BLUE),(560,270))
            screen.blit(myFont.render("CANCEL",1,BLUE),(610,270))
            screen.blit(myFont.render(newUserEmail,1,BLUE),(235,265))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
