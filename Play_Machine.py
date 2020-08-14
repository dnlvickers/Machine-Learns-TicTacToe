import pygame

class Play_Machine:
    '''this is where we can play the computer. If we have the training flag set to true, it will also take out data and
    add it to a csv of data that we will use to train the machine. We will take the first 4 moves that the player makes
    to train it (not taking the 5th since in that situation, there is only one move available in that case).'''

    def __init__(self, machine, train, screen):
        self.computer = machine
        self.training_mode = train
        self.screen = screen #we need to import the screen to play the game

        #build a blank board populate it with empty spaes
        self.board = []
        for i in range(3):
            col = []
            for j in range(3):
                col.append(0.0)
            self.board.append(col)

        #creating some values inherent to running the game
        self.turn = 0
        running = True

        gameBoardImage = pygame.image.load('images/board.png')
        xImage = pygame.image.load('images/cross.png')
        oImage = pygame.image.load('images/circle.png')

        while running:
            running = False
