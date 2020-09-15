from top import Top
from truck import Truck
from base import Base
import pygame
import sys
from interface_controller import *

CONST_WINDOW_WIDTH = 1200
CONST_WINDOW_LENGTH = 800
LT_CORNER = (0, 0)
RT_CORNER = (800, 0)
LB_CORNER = (0, 1200)
RB_CORNER = (800, 1200)

def run_program():

    #initialize pygame library
    pygame.init()
    screen = pygame.display.set_mode((CONST_WINDOW_WIDTH, CONST_WINDOW_LENGTH))
    
    b = Base('Lopro', 60, 30, 100, False, 5)
    t = Top(90, 21, 15, False, 55)
    truck = Truck(240,100,3)
    menu = Menu()
    done = False
    b.orient_vertical()

    while (done != True):
        pygame.event.pump()
        
        #constantly check for new events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)
        screen.fill((230,230,230))
        truck.draw_truck(screen)
        truck.draw_all_truck_arrays(screen)
        pygame.draw.rect(screen, (255,0,0),(b.x, b.y, b.length*2, b.width*2), 4)
        # pygame.draw.rect(screen, (0,0,255),(t.x, t.y, t.width*2, t.length*2), 4)
        menu.side_menu(screen)
        pygame.display.flip()
        
run_program();


