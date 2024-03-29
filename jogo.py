"""
---------------- GRUPO AGL --------------------

André de Miche Fialho – 42076218

Guilherme Henrique de Moura Guedes – 42010012

Lucca Romano Mari Mancusi – 42031575

-----------------------------------------------

"""

import pygame, sys
from pygame.locals import *
import random, time
from pygame import mixer 

pygame.init()
 
#Configurando o FPS 
FPS = 40
FramePerSec = pygame.time.Clock()
 
#Cores
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
CorFundo2 = (204,229,255)
 
#Variáveis do jogo
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
 
#Configuração das fontes de escrita
font = pygame.font.SysFont("Verdana", 17)
font_small = pygame.font.SysFont("Verdana", 20)
furou_a_dieta = font.render("DAMN IT!!! YOU BROKE YOUR DIET", True, ORANGE)
furou_a_dieta2 = font.render("HEALTHY EATING BRINGS RESULTS", True, RED)
#Criando a janela do jogo
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game Project - Grupo AGL")
 
#Música de fundo
mixer.music.load("Cyberpunk Moonlight Sonata.mp3")
mixer.music.play(-1)

class Game():
  def __init__(self):
    self.SPEED = 5
    self.SCORE = 0
    self.P1 = Player()
    self.P2 = Player2()
    self.E1 = Enemy()
    self.E2 = Enemy2()
    self.E3 = Enemy3()
    self.E4 = Enemy4()
    self.E5 = Enemy5()
    self.E6 = Enemy6()
    self.enemies = pygame.sprite.Group()
    self.enemies2 = pygame.sprite.Group()
    self.players = pygame.sprite.Group()
    self.all_sprites = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pizza.png")
        self.image = pygame.transform.scale(self.image, [88, 113])
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-294)
                                                 , 0))
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-294), 0)
 
class Enemy2(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("burger.png")
        self.image = pygame.transform.scale(self.image, [88, 113])
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(146, SCREEN_WIDTH-188)
                                                 , 0))
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(146, SCREEN_WIDTH-188), 0)

class Enemy3(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Pataepollo.png")
        self.image = pygame.transform.scale(self.image, [88, 113])
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(252,SCREEN_WIDTH-46)
                                                 , 0))
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(252,SCREEN_WIDTH-46), 0) 

class Enemy4(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("apple.png")
        self.image = pygame.transform.scale(self.image, [88, 113])
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-294)
                                                 , 0))
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-294), 0)

class Enemy5(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("zucchini.png")
        self.image = pygame.transform.scale(self.image, [88, 113])
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(146, SCREEN_WIDTH-188)
                                                 , 0))
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(146, SCREEN_WIDTH-188), 0)

class Enemy6(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("carrot.png")
        self.image = pygame.transform.scale(self.image, [88, 113])
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(252,SCREEN_WIDTH-46)
                                                 , 0))
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(252,SCREEN_WIDTH-46), 0) 
                                             
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Flavio_Sedentario.png")
        self.image = pygame.transform.scale(self.image, [64, 106])
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Flavio_Saudavel.png")
        self.image = pygame.transform.scale(self.image, [94, 126])
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('rua.png')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.movingUpSpeed = 5
         
      def update(self):
        self.bgY1 -= self.movingUpSpeed
        self.bgY2 -= self.movingUpSpeed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
         DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))
         
#Sprites        
P1 = Player()
P2 = Player2()
E1 = Enemy()
E2 = Enemy2()
E3 = Enemy3()
E4 = Enemy4()
E5 = Enemy5()
E6 = Enemy6()
 
back_ground = Background()
 
#Criando grupo dos Sprites 
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
enemies.add(E3)

enemies2 = pygame.sprite.Group()
enemies2.add(E4)
enemies2.add(E5)
enemies2.add(E6)

players = pygame.sprite.Group()
players.add(P1)
players.add(P2)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

def play(): 
#Game Loop
  game = Game()
  while True:
    
    #Fase 1 do jogo
    if SCORE == 0:
     all_sprites.add(E1)
    #Fase 2 do jogo
    if SCORE >= 1:
     all_sprites.add(E2)
    #Fase 3 do jogo
    if SCORE > 4:
     all_sprites.add(E3)
    #Fase 4 do jogo
    if SCORE > 9:
     all_sprites.remove(P1)
     all_sprites.remove(E1,E2,E3)
     all_sprites.add(P2, E4, E5)
    #Fase 5 do jogo
    if SCORE > 12:
     all_sprites.add(E6)
    
    

    #Cycles through all occurring events   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              game.SPEED += 0.2     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    back_ground.update()
    back_ground.render()
 
    #DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy

    if pygame.sprite.spritecollideany(P2, enemies2):
          pygame.mixer.Sound('bzzzt.wav').play()
          time.sleep(2)
	         
          DISPLAYSURF.fill(CorFundo2)
          DISPLAYSURF.blit(furou_a_dieta2, (55,250))

          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit() 
          
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('bzzzt.wav').play()
          time.sleep(2)
	
                    
          DISPLAYSURF.fill(BLACK)
          DISPLAYSURF.blit(furou_a_dieta, (55,250))

          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit() 

    pygame.display.update()
    FramePerSec.tick(FPS)
