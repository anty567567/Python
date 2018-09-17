import pygame
import sys
from pygame.locals import *
pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)
sky_blue = (0, 191, 255)
cloud_white = (231, 243, 254)
grass_yellow = (233, 174, 38)
mountains_purple = (54, 80, 161)
forest_green = (33, 63, 55)
tree_green = (46, 99, 10)
trunk_brown = (99, 73, 15)
wheat_yellow = (126, 106, 33)
tree_shadow_grey = (124, 97, 33)
sun_colour = (255, 215, 0)

x = 0
r = 0
g = 191
b = 255
rt = r
gt = g
bt = b
new_colour = (r, g, b)
a1 = 0
a2 = 0
a3 = 0
apple_a = 0
apple_b = 0
apple_c = 0
apple_1 = pygame.Rect(600, 260, 15, 15)
apple_2 = pygame.Rect(520, 180, 15, 15)
apple_3 = pygame.Rect(454, 280, 15, 15)

sun_x = 0
sun_y = 80
sun_pos = 0
day = True
night = False

rgb_value_change = 0.04

mountains_list = [(0, 160), (31, 170), (55, 185), (81, 183), (107, 195), (133, 205), (147, 215), (161, 226), (188, 218),
                  (216, 228), (244, 239), (273, 247), (306, 237), (336, 255), (367, 268), (402, 268), (418, 246),
                  (462, 234), (509, 242), (555, 251), (591, 237), (624, 217), (654, 200), (694, 177), (740, 210),
                  (760, 217), (779, 198), (795, 193), (799, 193), (800, 324), (0, 327)]
forest_list = [(0, 187), (18, 216), (31, 209), (44, 221), (58, 234), (75, 233), (91, 230), (105, 239), (114, 253),
               (134, 267), (143, 250), (175, 259), (197, 267), (219, 253), (253, 267),
               (286, 262), (343, 238), (417, 261), (441, 269), (470, 267), (501, 267), (535, 279), (557, 256),
               (619, 254), (657, 275), (696, 264), (737, 242), (779, 235), (796, 236), (800, 376), (0, 376)]
tree_list_1 = [(491, 392), (475, 378), (432, 392), (414, 376), (373, 392), (324, 369), (330, 320), (384, 296),
               (400, 290), (405, 287), (385, 252), (404, 220), (423, 210), (420, 168), (438, 150), (467, 132),
               (500, 116), (538, 104), (584, 106), (597, 115), (644, 120), (645, 130), (672, 130), (722, 187),
               (745, 224), (747, 277), (725, 301), (715, 334), (720, 348), (738, 377), (708, 419), (640, 425),
               (619, 444), (549, 410), (516, 404), (480, 430), (489, 393)]

trunk_list = [(490, 411), (500, 434), (510, 515), (590, 514), (588, 467), (608, 435), (563, 415), (526, 402),
              (507, 406)]

tree_shadow_list = [(593, 507), (665, 480), (716, 480), (755, 474), (779, 446), (792, 408), (791, 382), (758, 374),
                    (659, 398), (620, 430), (590, 453), (580, 492), (590, 508)]


lines = 0
y = 0
drawn = False
drawn_cloud = False

grass_x = 0
grass_y = 530
lines2 = 0
grass_rect = pygame.Rect(grass_x, grass_y, 50, 100)

screen = pygame.display.set_mode((796, 600))
clock = pygame.time.Clock()

while True:
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if apple_1.collidepoint(event.pos):
                a1 = 1
            if apple_2.collidepoint(event.pos):
                a2 = 1
            if apple_3.collidepoint(event.pos):
                a3 = 1

    # Game state changes
    cloud_list_1 = [(x + 192, 108), (x + 191, 109), (x + 178, 109), (x + 165, 110), (x + 150, 106), (x + 135, 107),
                    (x + 129, 110), (x + 118, 111), (x + 102, 115), (x + 85, 111), (x + 72, 91), (x + 68, 79),
                    (x + 72, 63), (x + 77, 60), (x + 100, 56), (x + 114, 60), (x + 125, 60), (x + 137, 59),
                    (x + 147, 58), (x + 155, 52), (x + 167, 46), (x + 181, 45), (x + 201, 56), (x + 225, 77),
                    (x + 225, 91), (x + 208, 101), (x + 186, 110)]
    lines = 0
    while lines != 300:
        pygame.draw.line(screen, new_colour, (0, y), (800, y), 8)
        y += 8
        rt = int(r + (rgb_value_change * (255 - r)))
        gt = int(g + (rgb_value_change * (255 - g)))
        bt = int(b + (rgb_value_change * (255 - b)))
        r = rt
        g = gt
        b = bt
        new_colour = (r, g, b)
        lines += 1
    y = -5
    if day:
        r = 0
        g = 191
        b = 255
    elif night:
        r = 25
        g = 25
        b = 112
    if sun_x < 375 and sun_pos == 0:
        pygame.draw.circle(screen, sun_colour, (sun_x, sun_y), 50)
        sun_x += 3
        sun_y -= 1
    elif sun_x >= 375:
        sun_pos = 1
    if sun_pos == 1:
        pygame.draw.circle(screen, sun_colour, (sun_x, sun_y), 50)
        sun_y += 1
        sun_x += 3
    if day and sun_x >= 1000:
        day = False
        rgb_value_change = 0.01
        sun_colour = (255, 255, 240)
        sun_x = 0
        sun_y = 80
        sun_pos = 0
        night = True
    elif night and sun_x >= 950:
        day = True
        sun_colour = (255, 215, 0)
        sun_x = 0
        sun_y = 80
        sun_pos = 0
        night = False
        rgb_value_change = 0.04

    if apple_a != 280 and a1 != 0:
        apple_a += 5
        apple_1.move_ip(0, 5)
        pygame.draw.rect(screen, red, apple_1)
    if apple_b != 330 and a2 != 0:
        apple_b += 5
        apple_2.move_ip(0, 5)
        pygame.draw.rect(screen, red, apple_2)
    if apple_c != 275 and a3 != 0:
        apple_c += 5
        apple_3.move_ip(0, 5)
        pygame.draw.rect(screen, red, apple_3)
    if x < 728:
        pygame.draw.polygon(screen, cloud_white, cloud_list_1)
        x += 1
    elif x == 728:
        x = -225

    if day:
        pygame.draw.rect(screen, grass_yellow, (0, 325, 800, 325))
    elif night:
        pygame.draw.rect(screen, tree_shadow_grey, (0, 325, 800, 325))
    pygame.draw.polygon(screen, mountains_purple, mountains_list)
    pygame.draw.polygon(screen, forest_green, forest_list)
    pygame.draw.polygon(screen, tree_shadow_grey, tree_shadow_list)

    grass_x = 2

    while lines2 != 200:
        grass_y = 515
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 2)
        grass_y = 460
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 2)
        grass_y = 450
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 3)
        grass_y = 410
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 2)
        grass_y = 395
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 2)
        grass_y = 380
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 1)
        grass_y = 365
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 1)
        lines2 += 1
        grass_x += 7
    lines2 = 0

    pygame.draw.polygon(screen, trunk_brown, trunk_list)
    pygame.draw.polygon(screen, tree_green, tree_list_1)

    grass_x = 0
    while lines2 != 100:
        grass_y = 530
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 3)
        grass_y = 490
        pygame.draw.arc(screen, wheat_yellow, (grass_x, grass_y, 50, 100), -4, -2.7, 3)
        lines2 += 1
        grass_x += 10
    lines2 = 0

    pygame.draw.rect(screen, red, apple_1)
    pygame.draw.rect(screen, red, apple_2)
    pygame.draw.rect(screen, red, apple_3)

    #  Update display
    pygame.display.update()
