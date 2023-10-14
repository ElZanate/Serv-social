import numpy as npgit 
import pygame as pg
import random
import sys
from numpy.core.fromnumeric import transpose
from numpy.core.shape_base import stack
from pygame.constants import MOUSEBUTTONDOWN
import time
import asyncio




pg.init()


pg.display.set_caption("Juego de la Vida")



# Interfaz.

ancho , alto = 600, 600
screen = pg.display.set_mode((ancho, alto))
Fondo = 5 , 5 , 5
screen.fill(Fondo)

nxc , nyc = 8 , 8

dimcw = ancho/nxc
dimch = alto/nyc

# Matriz de Juego.

gameMatrix = np.zeros((nxc,nyc)) 

# Bucle de Ejecución.

running = True
pause = False


while running:


    NewgameMatrix = np.copy(gameMatrix) 
    
    time.sleep(0.1)

    screen.fill(Fondo)

    ev = pg.event.get()

    

    for event in ev:

        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            pause= not pause
        mouseclick =pg.mouse.get_pressed() 
        if sum(mouseclick)>0:
            posx, posy = pg.mouse.get_pos()
            celx, cely = int(np.floor(posx/dimcw)), int(np.floor(posy/dimch))
            if gameMatrix[celx,cely]==0:
                NewgameMatrix[celx,cely]=1
            if gameMatrix[celx,cely]==1:
                NewgameMatrix[celx,cely]=0    
   
   
    for x in range (0,nxc):
        for y in range (0,nyc):
            
            if not pause:
                n_neigh= gameMatrix[(x-1)%nxc,(y-1)%nyc] + \
                     gameMatrix[(x)%nxc,(y-1)%nyc] + \
                     gameMatrix[(x+1)%nxc,(y-1)%nyc] + \
                     gameMatrix[(x+1)%nxc,(y)%nyc] + \
                     gameMatrix[(x+1)%nxc,(y+1)%nyc] + \
                     gameMatrix[(x)%nxc,(y+1)%nyc] + \
                     gameMatrix[(x-1)%nxc,(y+1)%nyc] + \
                     gameMatrix[(x-1)%nxc,(y)%nyc]

                if gameMatrix[x,y]==0 and n_neigh==3:
                   NewgameMatrix[x,y]=1
                if gameMatrix [x,y]==1 and (n_neigh < 2 or n_neigh > 3):
                   NewgameMatrix[x,y]=0  

            poly = [(x*dimcw, y * dimch),
                ((x+1)*dimcw, y * dimch),
                ((x+1)*dimcw, (y+1) * dimch),
                (x*dimcw, (y+1) * dimch) ]
            if NewgameMatrix[x,y] == 0:
                 pg.draw.polygon(screen,(128,128,128),poly, 1 )
            if NewgameMatrix[x,y] == 1:
                 pg.draw.polygon(screen,(250,250,250),poly, 0 )
                 pg.draw.polygon(screen,(28,28,128),poly, 5 )   
 

        
    
    
   
    gameMatrix = np.copy(NewgameMatrix)
    
            
            

    pg.display.flip()