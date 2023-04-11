import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE) #начальное положение змейки, с шагом размера сайз
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE) #начальное положение яблока
length = 1 #длина змейки

snake = [(x, y)] #сама змека, (список координат)
dx, dy = 0, 0 #направление движения
fps = 5 #скорость змейки

pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
 


while True: 
    surface.fill(pygame.Color('black'))
    [pygame.draw.rect(surface, ('Green'), (i, j, SIZE - 1, SIZE - 1), new_func() i, j in snake)]
    pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))

    x+=dx*SIZE
    y+=dy*SIZE
    snake.append((x,y))
    snake = snake[-length] #чтобы змейка не была бесконечной

    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length+=1
        fps+=1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# управление змейки за счет клавиш 
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
        
    elif key[pygame.K_s]:
        
        dx, dy = 0, 1

    elif key[pygame.K_a]:

        dx, dy = -1, 0
    
    elif key[pygame.K_d]:
        
        dx, dy = 1, 0
        

    pygame.display.update()
    clock.tick(fps)


    