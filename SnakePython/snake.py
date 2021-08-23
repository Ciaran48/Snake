import pygame
import time
import random

pygame.init()

#colours in RGB
red=(255,0,0)
orange=(255,128,0)
green=(0,153,0)
blue=(0,128,125)
purple=(127,0,255)
black=(0,0,0)
white=(255,255,255)
grey=(160,160,160)
lightgreen=(173, 247, 0)
#saves time declaring dispplay width as opposed to hard coding
display_width = 800
display_height = 600

#resolution
gameDisplay = pygame.display.set_mode((display_width,display_height))

#windowname
pygame.display.set_caption("Snake")

img= pygame.image.load("snakehead.png")

pygame.display.update()
Clock = pygame.time.Clock()
block_size = 20
FPS = 15

#font defined
font = pygame.font.SysFont(None, 25)

#define function
def snake(block_size, snakelist):
    gameDisplay.blit(img, (snakelist[-1][0], snakelist [-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
    
def message_to_screen (msg,colour):
    #true is for antialiasing
    screen_text = font.render(msg, True, colour)
    #centers the text
    gameDisplay.blit(screen_text, [display_width/2- screen_text.get_width()/2, display_height/2- screen_text.get_height()/2])
   
def gameLoop():
    #declaring variables
    gameRunning = True
    gameover = False

    head_x = display_width/2
    head_y = display_height/2

    head_x_change_pos = 0
    head_y_change_pos = 0

    snakelist = []
    snakelength = 1
    

    randEggX = random.randrange(0, display_width-block_size,10)
    randEggY = random.randrange(0, display_height-block_size,10)  

    #starts game
    while gameRunning == True:

        while gameover == True:
            gameDisplay.fill(blue)
            message_to_screen("Game over, press R to play again or Q to quit.", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameRunning=False
                        gameover=False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameRunning= False
                        gameover = False
                    elif event.key == pygame.K_r:
                        gameLoop()

        #event handleing
        for event in pygame.event.get():
            #"print (event)" shows us in the shell what is going on
            #lets the x on the window actually work
            if event.type == pygame.QUIT:
                gameRunning=False
            if event.type == pygame.KEYDOWN:
                #elif saves a little bit of processing
                #x movement
                if event.key == pygame.K_LEFT:
                    head_x_change_pos = -block_size
                    head_y_change_pos = 0
                elif event.key == pygame.K_RIGHT:
                    head_x_change_pos = block_size
                    head_y_change_pos = 0
                    
                #y movement
                elif event.key == pygame.K_UP:
                    head_y_change_pos = -block_size
                    head_x_change_pos = 0
                    
                elif event.key == pygame.K_DOWN:
                    head_y_change_pos = block_size
                    head_x_change_pos = 0

        #this had the problem that it wouldnt exe unless a KEYDOWN was pressed
        if head_x >= display_width or head_x < 0 or head_y >= display_height or head_y < 0:
            gameover = True
            

        #continious movement
        head_x += head_x_change_pos
        head_y += head_y_change_pos

        #Defines the windows colour
        gameDisplay.fill(lightgreen)

        #creating objects
        eggThickness = block_size
        pygame.draw.rect(gameDisplay, white, [randEggX,randEggY,eggThickness,eggThickness])

        snakehead = []
        snakehead.append(head_x)
        snakehead.append(head_y)
        snakelist.append(snakehead)

        if len(snakelist)> snakelength:
               del snakelist[0]

        if any(segment == snakehead for segment in snakelist[:-1]):
         gameover = True

        snake(block_size, snakelist)

        #Graphics rendering
        pygame.display.update()

        if head_x < randEggX + eggThickness and head_x > randEggX - block_size and head_y < randEggY + eggThickness and head_y > randEggY - block_size:

            randEggX = random.randrange(0, display_width-block_size,10)
            randEggY = random.randrange(0, display_height- block_size,10)
            snakelength += 1
        
        #fps, human eye cant really tell the difference between 30+
        #I chose a low fps with a high movement as this takes less processing power
        Clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()

