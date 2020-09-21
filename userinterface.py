from top import Top
from truck import Truck
from base import Base
from button import Button
from time import sleep
from predictLoading import Predicter
import pygame
import sys
from interface_controller import *
from eventStuff import  EventHandler

CONST_WINDOW_WIDTH = 1200
CONST_WINDOW_LENGTH = 800
LT_CORNER = (0, 0)
RT_CORNER = (800, 0)
LB_CORNER = (0, 1200)
RB_CORNER = (800, 1200)

load = Load()
truck = Truck(240,100,3)
eventHandler = EventHandler();
count = 0
num=0

#if __name__=="__main__":
  #  main();


ux_load = Button("Load an Order", 1000, 200)
def ux_loadClickEvent():
    global count
    global num
    count+=1
    print(count)
    num = load.count_number_of_orders("test_docs/test_doc_1.txt")
    load.read_in_load("test_docs/test_doc_1.txt", num)
    print(load.entire_load)
eventHandler.registerButton(ux_load , ux_loadClickEvent)


ux_simulate = Button("Simulate a Load", 1000, 300)
def ux_simulateClickEvent():
    Predicter.predict_loading(load.entire_load, truck, num)
eventHandler.registerButton(ux_simulate , ux_simulateClickEvent)

def run_program():
    global count
    #initialize pygame library
    pygame.init()
    screen = pygame.display.set_mode((CONST_WINDOW_WIDTH, CONST_WINDOW_LENGTH))
    
    b = Base('base', 'Lopro', 60, 30, 100, False, 5)
    # load = Load()
    
    # truck = Truck(240,100,3)
    menu = Menu()






    ux_surprise = Button("Suprise Me", 1000, 400)
    ux_na = Button("N/A", 1000, 500)
    done = False
    while (done != True):
        pygame.event.pump()
        
        #constantly check for new events
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit(1)
        eventHandler.eventQueue()
        screen.fill((230,230,230))
        truck.draw_truck(screen)
        truck.draw_all_truck_lists(screen)
        pygame.draw.rect(screen, (255,0,0),(b.x, b.y, b.length*2, b.width*2), 4)
        # pygame.draw.rect(screen, (0,0,255),(t.x, t.y, t.width*2, t.length*2), 4)
        menu.side_menu(screen)
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


