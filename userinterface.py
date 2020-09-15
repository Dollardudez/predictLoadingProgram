from top import Top
from truck import Truck
from base import Base
from button import Button
from time import sleep
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
    
    truck = Truck(240,100,3)
    menu = Menu()
    ux_load = Button("Load an Order", 1000, 200)
    ux_simulate = Button("Simulate a Load", 1000, 300)
    ux_surprise = Button("Suprise Me", 1000, 400)
    ux_na = Button("N/A", 1000, 500)
    done = False
    count = 0
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
        if(ux_load.is_mouse_clicked_on_button(screen)):
            count = 1
            load = Load()
            num = load.count_number_of_orders("D://random_docs/testLoad_1.txt")
            load.read_in_load("D://random_docs/testLoad_1.txt", num)
            print(load.entire_load)
        if(count >= 1 and count <=  15):
            ux_load.text = "loading...."

            count = count +1
            
        elif(count >= 16 and count <=  31):
            count = count +1
            ux_load.text = "done!"
        else:
            ux_load.text = "Load an Order"
        ux_load.draw_button(screen)
        ux_simulate.draw_button(screen)
        ux_surprise.draw_button(screen)
        ux_na.draw_button(screen)
        pygame.display.flip()
        
run_program();


