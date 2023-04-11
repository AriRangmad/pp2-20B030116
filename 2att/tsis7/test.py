import pygame
from datetime import datetime
import math

clock = pygame.time.Clock()

pygame.init()

RES = WIDTH, HEIGHT = 1400, 1050
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100, 'digit': RADIUS - 30}
RADIUS_ARK = RADIUS + 8

screen = pygame.display.set_mode((1400, 1050))

clock60 = dict(zip(range(60), range(0, 360, 6)))  # for hours, minutes and seconds
font = pygame.font.Font('Roboto-MediumItalic.ttf',48)# create text
realimage = pygame.image.load('bg4.jpeg')

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(realimage, (0,0))
    # get time now
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    # draw face
    for digit, pos in clock60.items():
        radius = 20 if not digit % 3 and not digit % 5 else 8 if not digit % 5 else 2
        pygame.draw.circle(screen, pygame.Color('gainsboro'), get_clock_pos(clock60, digit, 'digit'), radius, 7)


    # draw clock
    pygame.draw.line(screen, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(screen, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(screen, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pygame.draw.circle(screen, pygame.Color('white'), (H_WIDTH, H_HEIGHT), 8)
   


    pygame.display.update()
    clock.tick(20)