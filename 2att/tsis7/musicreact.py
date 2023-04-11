import pygame

pygame.init()
WIDTH = 500
HIGH = 500
screen = pygame.display.set_mode((WIDTH, HIGH))
clock  = pygame.time.Clock()
pygame.display.set_caption("Game playlist")

melody = pygame.mixer.Sound('music.mp3')
melody2 = pygame.mixer.Sound('music2.mp3')
melody3 = pygame.mixer.Sound('music3.mp3')


songs = [melody, melody2, melody3]

mus_count = 0

running = True
while running:

    screen.fill((183, 250, 167))
    pygame.display.update()


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        pygame.mixer.music.load(songs[0+mus_count])

        if mus_count ==2:
            mus_count=0

        else:
            mus_count+=1


        #if event.type == pygame.KEYDOWN: 
         #   if event.key == pygame.K_a:
          #      songs = songs[1:] + [songs[0]]
                #pygame.mixer.music.load(songs[0])
           #     pygame.mixer.music.play()
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
         #   songs = [songs[-1]] + songs[:-1]
            #pygame.mixer.music.load(songs[0])
          #  pygame.mixer.music.play()
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
         #   pygame.mixer.music.pause()
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
         #   pygame.mixer.music.unpause()
    

    clock.tick(5)
