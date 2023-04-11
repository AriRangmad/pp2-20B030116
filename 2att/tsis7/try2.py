import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

x = 500/2
y = 500/2
clock = pygame.time.Clock()
running = True

while running:

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ('Red'), (x, y), 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y>=30:  
        y-=20
    if pressed[pygame.K_DOWN] and y<=500-30: 
        y+=20
    if pressed[pygame.K_LEFT] and x>=30:  
        x-=20
    if pressed[pygame.K_RIGHT] and x<500-30: 
        x+=20

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
clock.tick(30)