import pygame


clock = pygame.time.Clock()

pygame.init() #начинаем создавать проект 
screen = pygame.display.set_mode((700, 400)) #устанавливаем размер дисплея, если хотим избавиться от рамки, то добавляем НОУФРЕМ
pygame.display.set_caption("Pygame_Start")
icon = pygame.image.load('images/pikachu.png')#иконка на окно
pygame.display.set_icon(icon)


realimage = pygame.image.load('images/bg.png').convert()#background
#player = pygame.image.load('images/playerleft1.png')

#создаем анимаию хотьбы через список:

walk_left = [
            pygame.image.load('images/playerleft1.png'),
            pygame.image.load('images/playerleft2.png')
]# to the left

walk_right = [
            pygame.image.load('images/playerright1.png'),
            pygame.image.load('images/playerright2.png')
]# to the right

player_anim_count = 0

#player = pygame.image.load('images/icon.png')
#player = pygame.transform.scale(player, (100, 100)) # Изменяем размер на 100x100 пикселей./1`1`
realimage_x = 0 #для движения заднего фона

sound = pygame.mixer.Sound('sounds/music.mp3')
sound.play()

#новое dlya dvijenya
player_speed = 5
player_x = 150 #расположение игрока по иксу
player_y = 220
is_Jump = False
jump_count = 7 #на столько позиций будет прыгать игрок

ghost = pygame.image.load('images/ghost.png')
ghost = pygame.transform.scale(ghost, (50, 50))
ghost_x = 720 #изначальная позиция за пределами экрана 
ghost_timer = pygame.USEREVENT +1 #timer for ghost appear
pygame.time.set_timer(ghost_timer, 7000)

ghost_list_in_game =[] #list of monsters

running = True
while running:
    
    screen.blit(realimage, (0,0))
    screen.blit(realimage, (realimage_x+700,0)) #для движения заднего фона
    realimage_x-=30
    if realimage_x<=-700:
        realimage_x =0
    
    #screen.blit(ghost, (ghost_x, 220))
    #ghost_x-=10

    player_rect = walk_left[0].get_rect(topleft = (player_x, player_y)) #квадрат вокруг игрока для столкновений

    if ghost_list_in_game:
        for el in ghost_list_in_game:
            screen.blit(ghost, el)
            el.x -=10 
    #ghost_rect = ghost.get_rect(topleft = (ghost_x, 220))
            if player_rect.colliderect(el):#ghost_rect):
                print('you lose')


    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    
    #for dvijenie:
    
    if keys[pygame.K_a] and player_x>50:
        player_x -= player_speed

    elif keys[pygame.K_d] and player_x<650:
        player_x += player_speed

    if not is_Jump: #for jumpping
        if keys[pygame.K_SPACE]:
            is_Jump = True
    else:
        if jump_count >=-7:
            if jump_count>0:
                player_y -= (jump_count **2)/2 #для мощного прыжка возводим в квадрат
            else:
                player_y += (jump_count **2)/2 #ставим игрока на место, летит вниз
            jump_count -=1
        else:
            is_Jump = False #завершаем прыжок, когда выйдем за рамки 7ки
            jump_count = 7


    if player_anim_count ==1:
        player_anim_count=0

    else:
        player_anim_count+=1

    
    pygame.display.update() #обновление дисплея

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #если тип ивента = выход, то выходим и делаем фолс раннинга
            pygame.quit() 
            running=False
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft = (720, 220)))


    clock.tick(9)# для более медленного изменения картинок (задержка)