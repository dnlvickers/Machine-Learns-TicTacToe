#import pygame
import pygame

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

running = True
while running:
    #keep game running until we close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw necessy screen elements
    screen.fill((200,200,200))
    test_draw()
    pygame.display.update()