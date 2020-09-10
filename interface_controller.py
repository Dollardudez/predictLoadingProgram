import pygame as pg
from base import Base
from loadpy import Load
#controller for user interface

class Menu():
    def __init__(self):
        self.mouse_is_clicked = False
        self.mouse_was_clicked = False
    
    def button(self, screen, text, x, y):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if mouse[0] > x and y+100 > mouse[1] > y:
            self.mouse_is_clicked = click[0] == 1
            pg.draw.rect(screen, (204, 204, 255),(x-7.5,y-5,200,100),8)
            if (not self.mouse_is_clicked and self.mouse_was_clicked):
                pg.draw.rect(screen, (255, 254, 198),(x-7.5,y-5,200,100))
                load = Load()
                num = load.count_number_of_orders("D://random_docs/testLoad_1.txt")
                load.read_in_load("D://random_docs/testLoad_1.txt", num)
                self.mouse_was_clicked = False
            elif (self.mouse_is_clicked):
                self.mouse_was_clicked = True

               
        else:
            pg.draw.rect(screen, (20, 20, 20),(x,y,185,90),2)
        font = pg.font.Font('freesansbold.ttf', 20) 
        text = font.render(text, True, (120,130,135))
        textRect = text.get_rect()
        textRect.center = (x+100, y+50)
        screen.blit(text, textRect)

        
        
    def side_menu(self, screen):
        font = pg.font.Font('freesansbold.ttf', 30) 
        text = font.render('Menu', True, (120,130,135))
        textRect = text.get_rect()
        textRect.center = (1100, 180)
        screen.blit(text, textRect)
        Menu.button(self, screen, "Load an Order", 1000, 200)
        Menu.button(self, screen, "Simulate a Load", 1000, 300)
        Menu.button(self, screen, "Suprise Me", 1000, 400)
        Menu.button(self, screen, "N/A", 1000, 500)
        
        
        
        
