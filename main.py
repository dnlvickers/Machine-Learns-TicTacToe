#import pygame
import pygame
import Machine
import Play_Machine
import Train_Machine

#generate initial game instance and screen
pygame.init()
pygame.display.set_caption('Machine Learns Tic-Tac-Toe')
screen = pygame.display.set_mode((800, 600))

#The only art assets are three incredible images made by yours truely
gameBoardImage = pygame.image.load('images/board.png')
xImage = pygame.image.load('images/cross.png')
oImage = pygame.image.load('images/circle.png')

def test_draw():
    screen.blit(gameBoardImage, (0, 0))
    screen.blit(xImage, (0, 0))
    screen.blit(oImage, (100, 0))
    screen.blit(xImage, (200, 0))
    screen.blit(oImage, (0, 100))
    screen.blit(xImage, (100, 100))
    screen.blit(oImage, (200, 100))
    screen.blit(xImage, (000, 200))
    screen.blit(oImage, (100, 200))
    screen.blit(xImage, (200, 200))

#Needed globals for the training
trainingMode = True
epochs = 10

running = True
while running:
    #fill in background color
    screen.fill((200, 200, 200))

    #keep game running until we close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #buttom check to see if they want to activate training mode while they play the machine

    #button to take in integer from player and train the computer for that number of epochs based upon the training data

    #button to begin a game of tic-tac-toe and test the machine

    #draw necessy screen elements

    test_draw()
    pygame.display.update()