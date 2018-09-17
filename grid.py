import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pink = (255, 192, 203)
black = (0, 0, 0)
white = (250, 250, 250)
water = "~"
grass = ","
concrete = "-"
player = "P"
player_pos_x = 0
# 0 is water
# 1 is grass
# 2 is concrete
BACKGROUND = [
    [0, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 2, 2],
    [0, 1, 1, 1, 2, 2],
    [1, 1, 2, 2, 2, 2],
]
scene = list(BACKGROUND)

while True:
    for row in BACKGROUND:
        for tile in row:
            if tile == 0:
                print(water, end="")
            elif tile == 1:
                print(grass, end="")
            elif tile == 2:
                print(concrete, end="")
            elif tile == 3:
                print(player, end="")
        print()
    print("--------------------------------------------------------------------------------------")
    print()
    print("[1] to move forward\n[2] to move backwards\n[3] to move down\n[4] to move up")
    move = input()
    if move == 1:
        player_pos_x += 1
