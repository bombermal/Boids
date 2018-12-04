import pygame
import bird as bd
import functions as fc
import argparse

def main(args):
    #Birds
    numBirds = args.nBirds
    birdsList = []
    numGroups = args.nGroups
    
    #pygame
    running = True
    width, height = [int(x) for x in args.resolution.split("x")]
    fps = 60
    
    #Colors
    black = (0,0,0)
    
    
    #Inicia a simulação
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    
    #Create Birds
    for ii in range(numBirds):
        birdsList.append(bd.bird(args.repulsion, args.attraction, width, height, screen, numGroups))
     
    for ii in range(numGroups):
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
            ii.draw(args.debug)
            ii.attractNRepel(birdsList)
            ii.move()
            ii.update()
                
            
        #Move pela tela    
        pygame.display.update()
        clock.tick(fps)
        
    pygame.quit()
    quit()

parser = argparse.ArgumentParser(description='Boids simulation')
parser.add_argument("-nBirds", nargs = "?", type=int, default = 100, help="Number of birds in simulation")
parser.add_argument("-nGroups", nargs = "?", type=int, default = 1, help="Number of groups in simulation")
parser.add_argument("-resolution", nargs = "?", default = "800x600", help="Windows size")
parser.add_argument("-repulsion", nargs = "?", type=int, default = 15, help="Repulsion distance")
parser.add_argument("-attraction", nargs = "?", type=int, default = 20, help="Attraction distance")
parser.add_argument("-debug", nargs = "?", type=bool, default = False, help="Debug mode")
args = parser.parse_args()

main(args)