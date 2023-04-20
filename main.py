import pygame
from pygame.constants import QUIT
import random

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
BLINK = (10, 10, 10)
PLAYER_COLOR_PALETTE = [(255, 0, 0), (255, 165, 0), (255, 255, 0),
                        (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

main_dysplay = pygame.display.set_mode((WIDTH, HEIGHT))

player_w = 20
player_h = 20
player = pygame.Surface((player_w, player_h))

# Get random position
random_x = random.randint(1, WIDTH - 1)
random_y = random.randint(1, HEIGHT - 1)

player.fill(COLOR_WHITE)

# Set player_rect
player_rect = pygame.Rect(random_x, random_y, player_w, player_h)

# Set initial random speed
random_speed_x = random.choice([-1, 1])
random_speed_y = random.choice([-1, 1])

player_speed = [random_speed_x, random_speed_y]

random_palette_color = 0

def set_random_color():
    random_palette_color = (random.randint(0, len(PLAYER_COLOR_PALETTE) - 1))
    player.fill(PLAYER_COLOR_PALETTE[random_palette_color])

while True:
    FPS.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    main_dysplay.fill(COLOR_BLACK)
    
    
    if player_rect.bottom >= HEIGHT:
        player_speed[1] *= -1
        set_random_color()
        main_dysplay.fill(BLINK)

    if player_rect.top <= 0:
        player_speed[1] *= -1
        set_random_color()
        main_dysplay.fill(BLINK)

    if player_rect.right >= WIDTH:
        player_speed[0] *= -1
        set_random_color()
        main_dysplay.fill(BLINK)

    if player_rect.left <= 0:
        player_speed[0] *= -1
        set_random_color()
        main_dysplay.fill(BLINK)

    main_dysplay.blit(player, player_rect)

    player_rect = player_rect.move(player_speed)

    pygame.display.flip()
