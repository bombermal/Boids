import os,sys
import pygame
import numpy as np
 
from pygame.locals import *

BLACK=(0,0,0)
WHITE = (255, 255, 255)

done=False

try:
    pygame.init()
except:
    print("O modulo pygame não foi inicializado/instalado corretamente")



def create_point(surface,list_pos):
    for ii in list_pos:
        print(ii)
        pygame.draw.circle(surface, BLACK, ii , 5)


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Boids')
pygame.mouse.set_visible(0)

list_pos = np.random.randint(400, size=(100,2))

screen.fill(WHITE)
create_point(screen,list_pos)       
pygame.display.flip()

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done=True


    
