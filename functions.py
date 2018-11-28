# -*- coding: utf-8 -*-
def calcNewPosition(border, borderSpeed, width, height, bird):
    if bird.positionX < border:
        bird.speedX += borderSpeed
    if bird.positionY < border:
        bird.speedY += borderSpeed
    if bird.positionX > (width - border):
        bird.speedX -= borderSpeed
    if bird.positionY > (height - border):
        bird.speedY -= borderSpeed
        
def updatePosition(bird):
    bird.positionX += bird.speedX
    bird.positionY += bird.speedY