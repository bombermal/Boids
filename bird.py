# -*- coding: utf-8 -*-
import numpy as np
import pygame
import functions2 as fc


#colors
red = (255,0,0)
green = (0,255,0)
pink = (255,0,127)
yellow = (255,255,51)

boundaryLimit = 10
maxVel = 10

class bird():
    def __init__(self, width, height, screen, leader=False):
        self.screen = screen
        self.position = np.array([np.random.uniform(width), np.random.uniform(height)], dtype="float64")
        self.velocity = np.array([np.random.uniform(-maxVel, maxVel), np.random.uniform(-maxVel, maxVel)], dtype="float64")
        self.acceleration = np.array([0,0], dtype="float64")
        self.leader = leader
        self.inAGroup = False 
        self.maxVel = 2
        self.maxForce = .5
        self.screenWidth = width
        self.screenHeight = height
        self.repulsion = 10
        self.attraction = 20
        
    def draw(self, debug=False):
        xPos, yPos = [int(x) for x in self.position]
        size = 5 if self.leader else 2
        color = yellow if self.leader else pink
        #Circulo principal
        pygame.draw.circle(self.screen, (color), (xPos, yPos), size)
        if debug:
            #Circulo interno
            pygame.draw.circle(self.screen, (red), (xPos, yPos), size+self.repulsion, 1)
            #Circulo externo
            pygame.draw.circle(self.screen, (green), (xPos, yPos), size+self.attraction, 1)
        
    def applyForce(self, force):
        self.acceleration += force
        
    def move(self):
        xPos, yPos = self.position
        desired = None
        #Calculo do eixo X
        if xPos < boundaryLimit:
            desired = np.array([self.maxVel, self.velocity[1]])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
        elif xPos > self.screenWidth - boundaryLimit:
            desired = np.array([-self.maxVel, self.velocity[1]])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
        #Calculo do eixo Y
        if yPos < boundaryLimit:
            desired = np.array([self.velocity[0], self.maxVel])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
        elif yPos > self.screenHeight - boundaryLimit:
            desired = np.array([self.velocity[0], -self.maxVel])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
            
    def update(self):
        self.velocity += self.acceleration
        
        #Limita a velocidade máxima
        self.velocity = fc.normalise(self.velocity)*self.maxVel
        
        #Salva a nova posição em position
        self.position += self.velocity
        #Zera a aceleração
        self.acceleration *= 0
        
    def attractNRepel(self, birdsList):
        xPos, yPos = self.position
        for ii in birdsList:
            iiXPos, iiYPos = ii.position
            if ii != self:
                #Distância entre os dois objetos
                distance = np.hypot(xPos-iiXPos, yPos-iiYPos)
                #Afasta os objetos caso a distância seja menor que o campo de repulsão
                if distance < self.repulsion:
                    ii.velocity = -self.velocity
                    
                #Igulha o vetor de velocidade dos objetos caso dentro do espaço de atração
                #elif distance < self.attraction and distance >self.repulsion:# and self.leader:
                #    ii.velocity = self.velocity# + ( distance - self.repulsion )


    def move2(self):
        xPos, yPos = self.position
        desired = None
        #Calculo do eixo X
        if xPos < boundaryLimit:
            desired = np.array([self.maxVel, self.velocity[1]])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
        elif xPos > self.screenWidth - boundaryLimit:
            desired = np.array([-self.maxVel, self.velocity[1]])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
        #Calculo do eixo Y
        if yPos < boundaryLimit:
            desired = np.array([self.velocity[0], self.maxVel])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)
        elif yPos > self.screenHeight - boundaryLimit:
            desired = np.array([self.velocity[0], -self.maxVel])
            steer = desired - self.velocity
            steer = fc.normalise(steer)*self.maxForce
            self.applyForce(steer)           
        
        
    