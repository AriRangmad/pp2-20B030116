import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
RADIUS_ARK = RADIUS + 8

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds

font = pygame.font.SysFont('Verdana', 60)
#img = pygame.image.load('2.png').convert_alpha()
bg = pygame.image.load('bg4.jpeg').convert()
bg_rect = bg.get_rect()
bg_rect.center = WIDTH, HEIGHT
dx, dy = 1, 1


def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # set bg
    dx *= -1 if bg_rect.left > 0 or bg_rect.right < WIDTH else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < HEIGHT else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    surface.blit(bg, bg_rect)
    # get time now
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    # draw face
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(surface, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)


    # draw clock
    pygame.draw.line(surface, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pygame.draw.circle(surface, pygame.Color('white'), (H_WIDTH, H_HEIGHT), 8)
   


    pygame.display.update()
    clock.tick(20)