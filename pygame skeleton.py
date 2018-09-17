import pygame
import sys
from pygame.locals import *
pygame. init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)

while True:
    clock.tick(60)

    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Game state changes
    screen.fill((0, 0, 0))

    # Update display
    pygame.display.update()
