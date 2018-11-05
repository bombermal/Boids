import os,sys
import pygame
from pygame.locals import *

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado/instalado corretamente")

while 1:

    screen = pygame.display.set_mode((468,400))
    pygame.display.set_caption('Boids')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,250,250))

    if pygame.font:
        font = pygame.font.Font(None,36)
        text = font.render("BOIDS",1, (10,10,10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text,textpos)


    screen.blit(background,(0,0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        


    
