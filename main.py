import pygame
import numpy as np
import bird2 as bd
import functions2 as fc

#%%Variables

#Birds
numBirds = 100
birdsList = []

#pygame
running = True
width = 800
height = 600
fps = 60

#Colors
black = (0,0,0)



#%%Simulate

#Inicia a simulação
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


#Create Birds
for ii in range(numBirds):
    birdsList.append(bd.bird(width, height, screen))
 
fc.chooseRandomLeader(birdsList)
  
while running:
    #Limpa a tela
    screen.fill(black)
    
    #Captura o evento e sai do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    #inicio das iterações com os objetos
    for ii in birdsList:
        #Debug = True
        ##Show circles
        ii.draw()
        ii.move2()
        ii.attractNRepel(birdsList)
        ii.update()
            
        
    #Move pela tela    
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
quit()