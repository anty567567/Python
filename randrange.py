import random
import pygame
import sys
from pygame.locals import *
pygame. init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)
x = 0
y = 10
drawn = False
while True:
    clock.tick(60)

    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Game state changes
    if not drawn:
        screen.fill(white)
        for i in range(1, 11):
            pygame.draw.circle(screen, black, (random.randrange(0, 250), random.randrange(0, 250)), 20, 2)
        drawn = True
    # Update display
    pygame.display.update()
