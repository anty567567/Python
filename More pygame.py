import pygame
import sys
from pygame.locals import *
pygame. init()
screen = pygame.display.set_mode((1000, 900))

clock = pygame.time.Clock()
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)
dx = 0
dy = 1
x_move = 0
player_rect = pygame.Rect(400, 50, 50, 50)
while True:
    clock.tick(60)

    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_rect.move_ip(10, 0)
    # Game state changes
    screen.fill(white)

    pygame.draw.rect(screen, black, player_rect)
    # Update display
    pygame.display.update()
