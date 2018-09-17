import pygame
import sys
from pygame.locals import *
pygame. init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)
lines = 0
y = 0
new_colour = (0, 0, 0)  # Put a colour for the gradient
r = 0
g = 0
b = 0

while True:
    clock.tick(60)

    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Game state changes
    screen.fill((0, 0, 0))
    while lines != 300:
        pygame.draw.line(screen, new_colour, (0, y), (800, y), 8)
        y += 8
        lines += 1
        rt = int(r + (0.015 * (255 - r)))
        gt = int(g + (0.015 * (255 - g)))
        bt = int(b + (0.015 * (255 - b)))
        r = rt
        g = gt
        b = bt
        new_colour = (r, g, b)
    # Update display
    pygame.display.update()
