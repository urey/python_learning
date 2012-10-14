#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      urey
#
# Created:     12/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *
import random

WHITE = (255,255,255)
RED = (255,0,0)   #rgba
BLUE = (0,0,255)
BLACK = (0,0,0)

FPS = 30
fpsClock = pygame.time.Clock()
def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((500,400),0,32)
    pygame.display.set_caption('hello world')
    DISPLAY.fill(WHITE)
    pygame.draw.polygon(DISPLAY, BLUE, ((146,0), (291,106),(236, 277), (56,277), (0,106)))

    pixobj = pygame.PixelArray(DISPLAY)
    pixobj[480][380] = BLACK
    del pixobj
    catImg = pygame.image.load("E:\\python learning\\cat.png")
    catx = 10
    caty = 10
    direction = 'right'

    while True:
        """
        DISPLAY.fill(WHITE)
        if direction == 'right':
            catx += 5
            if catx == 280:
                direction = 'down'
        elif direction == 'down':
            caty += 5
            if caty == 220:
                direction = 'left'
        elif direction == 'left':
            catx -= 5
            if catx == 10:
                direction = 'up'
        elif direction == 'up':
            caty -= 5
            if caty == 10:
                direction = 'right'
        DISPLAY.blit(catImg, (catx, caty))
        """
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                pygame.draw.polygon(DISPLAY, (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)), ((146,0), (291,106),(236, 277), (56,277), (0,106)))
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
    pass

if __name__ == '__main__':
    main()
