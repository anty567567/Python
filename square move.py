import pygame
import sys
import random
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1080, 650))
clock = pygame.time.Clock()

# Variables to store the location of the square
pieces = False
game = False
font = pygame.font.SysFont("None", 35)
dx = 0
dy = 0
win = 0
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)
colours = [(204, 0, 0), (255, 153, 51), (255, 255, 0), (102, 204, 0), (0, 255, 255), (0, 128, 255), (107, 0, 255),
           (255, 0, 127)]
box_x = 100
box_y = 100
box_width = 50
box_height = 50
size = (25, 50, 75, 100)
box = Rect(box_x, box_y, box_width, box_height)
sbox = Rect(500, 300, 20, 20)
sboxes = list()
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
sboxes.append(Rect(random.randint(10, 1000), random.randint(10, 550), 10, 10))
box_colour = black
click = False
color = white
while True:
    clock.tick(60)
    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if box.collidepoint(event.pos) and click is False:
                click = True
            elif sbox.collidepoint(event.pos) and click is False:
                click = True
            elif click is True and box.collidepoint(event.pos):
                click = False
        elif event.type == KEYDOWN:
            if event.key == K_c:
                box_colour = random.choice(colours)
                color = random.choice(colours)
            elif event.key == K_UP:
                box.inflate_ip(10, 10)
                box_height += 10
            elif event.key == K_SPACE:
                game = True

    # Game state change
    screen.fill(color)
    if box_height >= 250 and game is False:
        screen.fill(black)
        box_colour = black
        screen.blit(font.render("You exploded, start collecting all your pieces to regrow by pressing space!", 0,
                                (250, 250, 250)), (150, 300))
        pieces = True

    if click is True:
        box.center = pygame.mouse.get_pos()
        sbox.center = pygame.mouse.get_pos()
    if pieces is False:
        pygame.draw.rect(screen, box_colour, box)
        screen.blit(font.render(
            "Click your box to pick it up. Press c to change colours. Press up and keep growing!", 0,
            (0, 0, 0)), (75, 300))
    if pieces is True and game is True:
        pygame.draw.rect(screen, box_colour, sbox)
        for square in sboxes:
            pygame.draw.rect(screen, box_colour, square)
            if square.colliderect(sbox):
                destroy = sboxes.index(square)
                sboxes.pop(destroy)
                sbox.inflate_ip(4, 4)
                win += 1
    if win == 10:
        screen.blit(font.render("Good job, you are back to your original size!", 0,
                                (0, 0, 0)), (200, 300))

    # Update display
    pygame.display.update()
