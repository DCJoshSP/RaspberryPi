import pygame
import random
import math
import sys

pygame.init()
size = (800,400)
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

#background picture and sprites
backGround = pygame.image.load("PaconsultingBG.png")
bicycleSpriteLeft = pygame.image.load("bicycleSpriteLeft.png")
bicycleSpriteRight = pygame.image.load("bicycleSpriteRight.png")
bicycleCurrent = bicycleSpriteRight
bicycleVelocity = random.randint(1,5)
bicycleSide = 0
bicycleX = -100
bicycleY = 304
myFont =  pygame.font.SysFont("Impact",20)
myBigFont =  pygame.font.SysFont("Impact",50)

#variables for creating new account
enterNewUserName = False
enterNewUserEmail = False
newUserNameInput= False
newUserEmailInput = False
newUserName = "bob"
newUserEmail = "bob@gmail.com"

#variables for the login page
loginName = ""
userNames = ['A','B','C','D','E','F','G','H'] #this would be an array of all the urernames
userNameDisplayNo = 0
userName = ""

#variables for updating account info
updateUserName = False
updateUserEmail = False

#empty string used to display letters input
l = []
    
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if stage == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #checks the mouse to see if the user has clicked on a button
                mx, my = pygame.mouse.get_pos()
                if mx > 150 and mx < 300 and my >150 and my < 250:
                    stage = 2
                    print(stage)
                elif mx > 500 and mx < 650 and my>150 and my<250:
                    stage = 3
                    print(stage)
        elif stage == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 1
                if mx > 275 and mx < 550 and my > 190 and my <215:
                    enterNewUserName = True
                elif mx > 235 and mx < 550 and my > 220 and my < 245:
                    enterNewUserEmail = True
                if enterNewUserName == True:
                    if mx > 550 and mx < 600 and my > 190 and my < 215:
                        enterNewUserName = False
                        userName = newUserName #(userName) is where the user would input their new username, so change this to whatever you use in the main code!
                        newUserName = ""
                        l = []
                        print(userName)
                        newUserNameInput = True
                    elif mx > 610 and mx < 650 and my > 190 and my < 215:
                        enterNewUserName = False
                        newUserName = ""
                        l = []
                elif enterNewUserEmail == True:
                    if mx > 550 and mx < 600 and my > 220 and my < 235:
                        enterNewUserEmail = False
                        userEmail = newUserEmail #same above, but for the new user's email address this time.
                        newUserEmail = ""
                        l = []
                        print(userEmail)
                        newUserEmailInput = True
                    elif mx > 610 and mx < 650 and my > 200 and my < 235:
                        enterNewUserEmail = False
                        newUserName = ""
                        l = []
                elif newUserNameInput == True and newUserEmailInput == True:
                    if mx > 290 and mx < 435 and my > 270 and my < 310: 
                        stage = 8
            elif enterNewUserName == True or enterNewUserEmail == True:  
                if event.type == pygame.KEYDOWN:
                    letterInput = pygame.key.name(event.key)
                    if enterNewUserName == True:
                        l.append(letterInput)
                        newUserName = ''.join(l)
                    if enterNewUserEmail == True:
                        l.append(letterInput)
                        newUserEmail = ''.join(l)
        elif stage == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx > 190 and mx < 245 and my >310 and my < 345:
                        stage = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if userNameDisplayNo == 0:
                            userNameDisplayNo == len(userNames)-1
                        else:
                            userNameDisplayNo = userNameDisplayNo - 1
                    elif event.key == pygame.K_RIGHT:
                        if userNameDisplayNo == (len(userNames)-1):
                            userNameDisplayNo = 0
                        else:
                            userNameDisplayNo = userNameDisplayNo + 1
                    elif event.key == pygame.K_RETURN:
                        userName = userNames[userNameDisplayNo]
                        print(userName)
                        stage = 4
        elif stage == 4:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 3
                elif mx > 300 and mx < 450 and my > 150 and my < 200:
                    stage  = 5
                elif mx > 300 and mx < 450 and my > 220 and my < 270:
                    stage = 6
                elif mx > 300 and mx < 450 and my > 290 and my < 340:
                    stage = 7
        elif stage == 5:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 4
                elif mx > 150 and mx < 300 and my > 150 and my < 250:
                    stage = 9
                elif mx > 500 and mx < 650 and my > 150 and my < 250:
                    stage = 10
        elif stage == 6:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 4
                elif mx > 500 and mx < 550 and my > 150 and my < 175:
                    updateUserName = True
                elif mx > 500 and mx < 550 and my > 180 and my < 205:
                    updateUserEmail = True
            elif event.type == pygame.KEYDOWN:
                elif enterNewUserName == True or enterNewUserEmail == True:  
                letterInput = pygame.key.name(event.key)
                if enterNewUserName == True:
                    l.append(letterInput)
                    newUserName = ''.join(l)
                if enterNewUserEmail == True:
                    l.append(letterInput)
                    newUserEmail = ''.join(l)
        elif stage == 7:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 4
        elif stage == 8:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mx > 315 and mx < 485 and my > 280 and my < 330:
                        stage = 1
        elif stage == 9:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 6
        elif stage == 10:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mx > 190 and mx < 245 and my >310 and my < 345:
                    stage = 6
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
        pygame.draw.rect(screen, YELLOW , (150,150,150,100))
        pygame.draw.rect(screen, YELLOW , (500,150,150,100))
        screen.blit(myFont.render("CREATE NEW",1,BLUE),(175,185))
        screen.blit(myFont.render("LOG IN",1,BLUE),(550,185))
        userName = ""
    elif stage == 2:
        screen.blit(myFont.render("Creating new acount:",1,BLUE),(100,150))
        pygame.draw.rect(screen, YELLOW, (275,210,275,5))
        screen.blit(myFont.render("Enter Username:",1,BLUE),(140,190))
        pygame.draw.rect(screen, YELLOW, (235,240,315,5))
        screen.blit(myFont.render("Enter Email:",1,BLUE),(140,220))
        pygame.draw.rect(screen, YELLOW, (290,270,145,50))
        screen.blit(myFont.render("Create account",1,BLUE),(300,280))
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
        if enterNewUserName == True:
            screen.blit(myFont.render("DONE",1,BLUE),(560,190))
            screen.blit(myFont.render("CANCEL",1,BLUE),(610,190))
            screen.blit(myFont.render(newUserName,1,BLUE),(275,185))
        elif enterNewUserEmail == True:
            screen.blit(myFont.render("DONE",1,BLUE),(560,220))
            screen.blit(myFont.render("CANCEL",1,BLUE),(610,220))
            screen.blit(myFont.render(newUserEmail,1,BLUE),(235,215))
        if newUserNameInput == True:
            screen.blit(myFont.render(userName,1,BLUE),(275,185))
        if newUserEmailInput == True:
            screen.blit(myFont.render(userEmail,1,BLUE),(235,215))
    elif stage == 3:
        screen.blit(myFont.render("Use arrows to cycle through accounts, then press ENTER to select yours.",1,BLUE),(120,180))
        screen.blit(myBigFont.render("<",1,BLUE),(275,220))
        screen.blit(myBigFont.render(">",1,BLUE),(475,220))
        screen.blit(myFont.render(userNames[userNameDisplayNo],1,BLUE),(350,235))
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    elif stage == 4:
        screen.blit(myFont.render("Account : " + userName,1,BLUE),(120,145))
        pygame.draw.rect(screen, YELLOW, (300,150,150,50))
        screen.blit(myFont.render("View clothes",1,BLUE),(323,162))
        pygame.draw.rect(screen, YELLOW, (300,220,150,50))
        screen.blit(myFont.render("Edit account",1,BLUE),(325,232))
        pygame.draw.rect(screen, YELLOW, (300,290,150,50))
        screen.blit(myFont.render("Recomendation",1,BLUE),(312,302))
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    elif stage == 5:
        pygame.draw.rect(screen, YELLOW , (150,150,150,100))
        pygame.draw.rect(screen, YELLOW , (500,150,150,100))
        screen.blit(myFont.render("VIEW CLOTHES",1,BLUE),(170,185))
        screen.blit(myFont.render("EDIT CLOTHES",1,BLUE),(525,185))
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    elif stage == 6:
        screen.blit(myFont.render("Username : ",1,LIGHTBLUE),(210,150))
        screen.blit(myFont.render("Email : ",1,LIGHTBLUE),(210,180))
        screen.blit(myFont.render(newUserName,1,LIGHTBLUE),(310,150))
        screen.blit(myFont.render(newUserEmail,1,LIGHTBLUE),(265,180))
        screen.blit(myFont.render("EDIT",1,BLUE),(500,150))
        screen.blit(myFont.render("EDIT",1,BLUE),(500,180))
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    elif stage == 7:
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    elif stage == 8:
        screen.blit(myBigFont.render("Account created!",1,BLUE),(200,100))
        screen.blit(myFont.render("You can now Log in through the main menu!",1,BLUE),(205,175))
        screen.blit(myFont.render("Account name : " + userName,1,BLUE),(150,210))
        screen.blit(myFont.render("Email : " + userEmail,1,BLUE),(223,240))
        pygame.draw.rect(screen, YELLOW, (315,280,170,50))
        screen.blit(myFont.render("Back to main menu",1,BLUE),(323,290))
    elif stage == 9:
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    elif stage == 10:
        pygame.draw.rect(screen, YELLOW, (190,310,55,35))
        screen.blit(myFont.render("BACK",1,BLUE),(195,315))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
