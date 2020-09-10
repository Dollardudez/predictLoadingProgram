import pygame as pg

#truck object
class Truck:
    """ represents a truck to be loaded with items
    """
    def __init__(self, l, w, mc):
        self.length = l
        self.width = w
        self.max_capacity = mc
        
        self.underLeft = []
        self.underLeftC = []
        self.underRightC = []
        self.underRight = []
        
        self.downOne = []
        self.downTwo = []
        self.downThree = []
        self.downFour = []
        
        self.levelOne = []
        self.levelTwo = []
        self.levelThree = []
        self.levelFour = []
        
        self.sd_1 = []
        self.sd_2 = []
        self.sd_3 = []
        self.sd_4 = []
        
        self.x = 325
        self.y = 200
    """ l = length, w = width, mc = max capacity
    """
    
    def draw_truck(self, screen):
        pg.draw.rect(screen, (183,210,233), (self.x, self.y, self.width*2, self.length*2))
        #pg.draw.rect(screen, (0,0,0), (self.x, self.y, self.width*2, self.length*2), 5)
        font = pg.font.Font('freesansbold.ttf', 30) 
        text = font.render('Truck', True, (120,130,135))
        screen.blit(text, ((self.x+50, self.y-30)))
        font1 = pg.font.Font('freesansbold.ttf', 15) 
        text1 = font1.render('under', True, (120,130,135))
        screen.blit(text1, ((self.x-50, self.y+100)))
        font2 = pg.font.Font('freesansbold.ttf', 15) 
        text2 = font2.render('down', True, (120,130,135))
        screen.blit(text2, ((self.x-50, self.y+250)))
        """ function that draws a truck onto the screen:
        using the screen, (color), (x,y pos), (width, height)
        """
    def draw_truck_array(self, screen, x, y, width, length):
        array = pg.draw.rect(screen, (255,255,255),(x,y,width*2,length*2), 2)
        array.center = (x, y)
        
    def draw_all_truck_arrays(self, screen):
        self.draw_truck_array(screen, self.x,     self.y, 25, 100)
        self.draw_truck_array(screen, self.x+50,  self.y, 25, 100)
        self.draw_truck_array(screen, self.x+100, self.y, 25, 100)
        self.draw_truck_array(screen, self.x+150, self.y, 25, 100)
        
        self.draw_truck_array(screen, self.x,     self.y+200,  25, 100)
        self.draw_truck_array(screen, self.x+50,  self.y+200,  25, 100)
        self.draw_truck_array(screen, self.x+100, self.y+200,  25, 100)
        self.draw_truck_array(screen, self.x+150, self.y+200,  25, 100)
        
        self.draw_truck_array(screen, self.x,     self.y+400,  25, 40)
        self.draw_truck_array(screen, self.x+50,  self.y+400,  25, 40)
        self.draw_truck_array(screen, self.x+100, self.y+400,  25, 40)
        self.draw_truck_array(screen, self.x+150, self.y+400,  25, 40)
