import pygame as pg
from base import Base
from load import Load

class Menu():
    def __init__(self):
        self.mouse_is_clicked = False
        self.mouse_was_clicked = False     
        
    def side_menu(self, screen):
        font = pg.font.Font('freesansbold.ttf', 30) 
        text = font.render('Menu', True, (120,130,135))
        textRect = text.get_rect()
        textRect.center = (1100, 180)
        screen.blit(text, textRect)

class DrawItems():
    """
    Class that defines methods for drawing items to the screen.
    """

    def DrawBase(screen, base_x, base_y, base_len, base_width):
        """
        Method that draws a base to the screen from given the parameters.
        """
        pygame.draw.rect(screen, (255,0,0),(base_x, base_y, base_len*2, base_width*2), 4)
        

    def DrawPanel(screen, panel_x, panel_y, panel_len, panel_width):
        """
        Method that draws a panel to the screen from given the parameters.
        """
        pygame.draw.rect(screen, (255,0,0),(panel_x, panel_y, panel_len*2, panel_width*2), 4)

    def DrawTop(screen, top_x, top_y, top_len, top_width):
        """
        Method that draws a top to the screen from given the parameters.
        """
        pygame.draw.rect(screen, (255,0,0),(top_x, top_y, top_len*2, top_width*2), 4)
        
        
    
        
