# -*- coding: utf-8 -*-
import numpy as np

class bird():
    positionX = None
    positionY = None
    speedX = None
    speedY = None
    
    def __init__(self, width, height, posSpread, speedSpread, leader=False):
        """
            width = Largura da tela
            height = Altura da Tela
            posSpread = Distribuição dos birds em detrimento da posição
            speedSpread = Define a velocidade dentro de um range
            
        """
        
        if leader:
            self.positionX = width
            self.positionY = height
            self.speedX = posSpread
            self.speedY = speedSpread
        
        else:
            #O 'midX/midY' faz com que os birds sejam geras proximos ao centro
            midX = width/2
            midY = height/2
            
            #Definição dos valores para cada objeto
            """
                Verificar se uniform é mesmo melhor que ranint!!!
            """
            self.positionX = np.random.uniform(midX - posSpread, midX + posSpread)
            self.positionY = np.random.uniform(midY - posSpread, midY + posSpread)
            self.speedX = np.random.uniform(-speedSpread, speedSpread)
            self.speedY = np.random.uniform(-speedSpread, speedSpread)
        
    def returnAll(self):
        return [ self.positionX, self.positionY, self.speedX, self.speedY ]
        
