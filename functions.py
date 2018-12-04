# -*- coding: utf-8 -*-

import numpy as np

def chooseRandomLeader(birdsList):
    aux = np.random.choice(birdsList)
    if aux.leader == True:
        chooseRandomLeader(birdsList)
    else:
        aux.leader = True
    
def normalise(vector):
    """
        esse lambda eleva cada elemento do vetor ao quadrado e depois soma tudo
        em seguida, step recebe o valor do somatório e eleva a 0.5
    """
    step = (np.sum([(lambda x: x*x)(x) for x in vector]))**.5
    if step != 0:
        vector = vector/step
        
    return vector