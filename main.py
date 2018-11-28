# -*- coding: utf-8 -*-
import bird as bd
import functions as fc
import pygame, time, math
import numpy as np

#%%
# tamanho da tela
width = 500
height = 500
#Birds
birdsNum = 200
posSpread = 10
speedSpread = 5

birdlist = []
leaderBird = bd.bird(300, 300, 5, 2, True)
# Generate birds
"""
    Tranfromar o bird em um objeto
"""
for _ in range(birdsNum):
	birdlist.append(bd.bird(width, height, posSpread, speedSpread))


#%%tela


"""
Border seria uma borda de segurança? Lembra paspatu

"""
border = 100
borderSpeed = 0.2

#Cria Janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boids")
 
running = True

while running:
    pygame.init()
    #Fecha a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Limpa a tela da ultima passagem
    screen.fill((0,0,0)) 
    
    #Loop
    pygame.draw.circle(screen, (255,0,255), (int(leaderBird.positionX), int(leaderBird.positionY)), 5)  
    #Atualizaposição do Lider
    fc.calcNewPosition(border, borderSpeed, width, height, leaderBird)
    
    fc.updatePosition(leaderBird)
    #Trabalha com a lista de birds
    for ii in birdlist:
        #Desenha os birds
        pygame.draw.circle(screen, (255, 2, 4), (int(ii.positionX), int(ii.positionY)), 2)  
    
        #Determina as nova posições posições
        fc.calcNewPosition(border, borderSpeed, width, height, ii)
        
        #Move em diração do lider
        ii.speedX += np.random.uniform(.001, .009) * (leaderBird.positionX - ii.positionX)
        ii.speedY += np.random.uniform(.0001, .009) * (leaderBird.positionY - ii.positionY)
        
        """
        avxtotal = 0
        avytotal = 0
        avcount = 0
        for num, jj in enumerate(birdlist):
            if jj != ii:
                tempX = jj.positionX - ii.positionX
                tempY = jj.positionY - ii.positionY
                dist = math.sqrt(tempX*tempX + tempY*tempY)
                if dist < 10:
                    ii.speedX -= tempX * 0.2
                    ii.speedY -= tempY * 0.2
                if dist < 40:
                    avxtotal += jj.speedX
                    avytotal += jj.speedY
                    avcount += 1
        if avcount != 0:
            ii.speedX = .9 * ii.speedX + .1 * (avxtotal/avcount)
            ii.speedY = .9 * ii.speedY + .1 * (avytotal/avcount)
        """
        #Salva as novas posições nos objetos
        fc.updatePosition(ii)
        
    
    #Espera entre simulações
    time.sleep(0.1)
    #Desenha tudo
    pygame.display.flip()