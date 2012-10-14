#-------------------------------------------------------------------------------
# Name:        match
# Purpose:
#
# Author:      urey
#
# Created:     12/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, random,sys
from pygame.locals import *

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
order = [1,2,1,2]
def main():
    pygame.init()
    DISPLAY = pygame.display.set_mode((400,300),0,32)
    rect = []
    for i in range(len(order)):
        rect.append(pygame.rect)
        rect[i].Rect((10,10),(40,40))



    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

if __name__ == '__main__':
    main()
