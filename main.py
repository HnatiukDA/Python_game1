import pygame
from pygame.constants import QUIT, K_w, K_s, K_a, K_d
import random

pygame.init()

# Consts
FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

# Colors
COLOR_WHITE = ('#ffffff')
COLOR_BLACK = ('#000000')
COLOR_RED = ('#ff0000')
COLOR_GREEN = ('#00ff00')
COLOR_NET = ('#aaccaa')


main_dysplay = pygame.display.set_mode((WIDTH, HEIGHT))

net_size = (WIDTH/80, 300)
net_position = (main_dysplay.get_width()/2, HEIGHT)
net = pygame.Surface(net_size)
net.fill(COLOR_NET)
net_rect = pygame.Rect(*net_position, *net_size)

# Controls
player_move_up = (0, -4)
player_move_down = (0, 4)

# Functions


def create_ball():
    ball_size = (30, 30)
    ball_position = (WIDTH/2, random.randint(100, HEIGHT - 100))
    ball = pygame.Surface(ball_size)
    ball.fill(COLOR_WHITE)
    ball_rect = pygame.Rect(*ball_position, *ball_size)
    ball_speed = [random.choice([-4, 4]), random.choice([-4, 4])]
    return [ball, ball_rect, ball_speed]


def create_player():
    player_size = (20, HEIGHT/5)
    player_position = (0, random.randint(100, HEIGHT - 100))
    player = pygame.Surface(player_size)
    player.fill(COLOR_WHITE)
    player_rect = pygame.Rect(*player_position, *player_size)
    player_speed = [0, 0]
    return [player, player_rect, player_speed]


CREATE_BALL = pygame.USEREVENT + 1
balls = []

CREATE_PLAYER = pygame.USEREVENT + 2
players = []

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

    keys = pygame.key.get_pressed()

    if len(balls) == 0:
        balls.append(create_ball())
    if len(players) == 0:
        players.append(create_player())

    for ball in balls:
        if ball[1].top <= 0:
            ball[2][1] *= -1

        if ball[1].bottom >= HEIGHT:
            ball[2][1] *= -1

        if ball[1].right >= WIDTH:
            ball[2][0] *= -1

        for player in players:
            player_right = player[1].right
            player_top = player[1].top
            player_bottom = player[1].bottom
            if keys[K_w]:
                add_ball_speed = 1
            elif keys[K_s]:
                add_ball_speed = -1
            else:
                add_ball_speed = 0

        if ball[1].left <= player_right and ball[1].bottom > player_top and ball[1].top < player_bottom:
            ball[2][0] *= -1
            ball[2][1] += add_ball_speed

    for ball in balls:
        ball[1] = ball[1].move(ball[2])
        main_dysplay.blit(ball[0], ball[1])

    for player in players:
        if keys[K_w] and player[1].top > 0:
            player[1] = player[1].move(player_move_up)
        if keys[K_s] and player[1].bottom < HEIGHT:
            player[1] = player[1].move(player_move_down)

        main_dysplay.blit(player[0], player[1])

    pygame.display.flip()

    for ball in balls:
        if ball[1].right < 0:
            balls.pop(balls.index(ball))
            for player in players:
                players.pop(players.index(player))
        if ball[1].left > WIDTH:
            balls.pop(balls.index(ball))
            for player in players:
                players.pop(players.index(player))
