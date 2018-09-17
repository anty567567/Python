import pygame
import sys
from pygame.locals import *
pygame. init()

screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)
dx = 5
dy = 5
a = 0
b = 0
c = 0
d = 0
screen_rect = screen.get_rect
player_rect = pygame.Rect(400, 50, 50, 50)
while True:
    clock.tick(60)

    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                b = True
            if event.key == pygame.K_RIGHT:
                a = True
            if event.key == pygame.K_UP:
                c = True
            if event.key == pygame.K_DOWN:
                d = True
            if event.key == pygame.K_DOWN:
                d = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                a = False
            if event.key == pygame.K_LEFT:
                b = False
            if event.key == pygame.K_UP:
                c = False
            if event.key == pygame.K_DOWN:
                d = False
    # Game state changes
    screen.fill((250, 250, 250))
    if a:
        player_rect.move_ip(dx, 0)
    if b:
        player_rect.move_ip(-dx, 0)
    if c:
        player_rect.move_ip(0, -dy)
    if d:
        player_rect.move_ip(0, dy)
    pygame.draw.rect(screen, black, player_rect)
    # Update display
    pygame.display.update()
