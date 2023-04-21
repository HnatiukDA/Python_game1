import pygame
from pygame.constants import QUIT
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

# Functions


def create_ball():
    ball_size = (30, 30)
    ball_position = (WIDTH/2, random.randint(100, HEIGHT - 100))
    ball = pygame.Surface(ball_size)
    ball.fill(COLOR_WHITE)
    ball_rect = pygame.Rect(*ball_position, *ball_size)
    ball_speed = [random.choice([-1, 1]), random.choice([-1, 1])]
    return [ball, ball_rect, ball_speed]


CREATE_BALL = pygame.USEREVENT + 1
balls = []


while True:
    FPS.tick(360)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        if event.type == CREATE_BALL:
            print()

    main_dysplay.fill(COLOR_BLACK)

    if len(balls) == 0:
        balls.append(create_ball())

    for ball in balls:
        if ball[1].top <= 0:
            ball[2][1] *= -1

        if ball[1].bottom >= HEIGHT:
            ball[2][1] *= -1

        # if ball[1].right >= WIDTH:
        #     ball[2][0] *= -1

        # if ball[1].left <= 0:
        #     ball[2][0] *= -1

    for ball in balls:
        ball[1] = ball[1].move(ball[2])
        main_dysplay.blit(ball[0], ball[1])

    pygame.display.flip()

    for ball in balls:
        if ball[1].right < 0:
            balls.pop(balls.index(ball))
        if ball[1].left > WIDTH:
            balls.pop(balls.index(ball))
        if ball[1].top > HEIGHT:
            balls.pop(balls.index(ball))
    print(len(balls))
