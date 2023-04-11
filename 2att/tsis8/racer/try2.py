import pygame
import random
import time
import sys
from pygame.locals import*

pygame.init()
fps=pygame.time.Clock()
BLUE=(0, 0, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLACK=(0, 0, 0)
WHITE = (255, 255, 255)

w=400
h=600
SPEEDENEMY=random.randint(1,5)
SPEEDCOIN=random.randint(1,5)
SCORE=0
COINS=0
SPEED=5
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('racer/Enemy.png')
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,w-40), 0))

BACKGROUND = pygame.image.load('racer/AnimatedStreet.png')

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer/Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,w-40), 0))
      def move(self):
        global SCORE, SPEEDENEMY
        self.rect.move_ip(0,SPEEDENEMY)
        if (self.rect.bottom > 600):
            SCORE += 1
            SPEEDENEMY = random.randint(1,5)
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer/Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < w:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("racer/coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center=(random.randint(40, w - 40), 0))
        self.state = False
    def move(self):
        global SPEEDCOIN
        self.rect.move_ip(0, SPEEDCOIN)
        if (self.rect.bottom > 600 or self.state) :
            SPEEDCOIN = random.randint(1, 5)
            self.state = False
            self.rect.top = 0
            self.rect.center = (random.randint(40, w - 40), 0)
enemy = Enemy()
player = Player()
coIn=Coin()
enemies = pygame.sprite.Group()
enemies.add(enemy)
coins=pygame.sprite.Group()
coins.add(coIn)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coIn)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
while True:
    for event in pygame.event.get():
        for event in pygame.event.get():
            if event.type == INC_SPEED:
              SPEED += 2
            if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()

    screen.blit(BACKGROUND, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    collect=font_small.render(str(COINS),True,BLACK)
    screen.blit(collect, (w - 30, 10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        if pygame.sprite.spritecollideany(player, enemies):
          screen.fill(RED)
          GAMEOVER=game_over.get_rect(center=(w // 2, h // 2))
          screen.blit(game_over, GAMEOVER)
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    if pygame.sprite.spritecollideany(player, coins):
        COINS += 1
        for entity in coins:
            entity.state = True
    pygame.display.update()
    
   
    fps.tick(60)