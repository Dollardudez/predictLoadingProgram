import pygame as pg

#truck object
class Truck:
    """ 
    Represents a truck to be loaded with items.

    Attributes:
        length: the length (in feet) of the Truck, default value is 240 ft.
        width: the width (in feet) of the Truck, default value is 100 ft.
        max_capacity: the max capacity of weight allowed in the truck (in lbs.), the default value is 1200 lbs.
        underLeft: a list that represents the leftmost 25 inches of the "UNDER" in the Truck
        underLeftC: a list that represents the 25 inches between the underLeft and the centerline of the Truck
        underRightC: a list that represents the 25 inches between the underRight and the centerline of the Truck
        underRight: a list that represents the rightmost 25 inches of the "UNDER" in the Truck
        etc...
           ...
        x: the x position of the Truck on the display
        y: the y position of the Truck on the display
    """
    def __init__(self, l = 240, w = 100, mc = 1200):
        self.length = l
        self.width = w
        self.max_capacity = mc
        
        self.underLeft = []
        self.underLeftC = []
        self.underRightC = []
        self.underRight = []
        
        self.downLeft = []
        self.downLeftC = []
        self.downRightC = []
        self.downRight = []
        
        self.levelLeft = []
        self.levelLeftC = []
        self.levelRightC = []
        self.levelRight = []
        
        self.sd_Left = []
        self.sd_LeftC = []
        self.sd_RightC = []
        self.sd_Right = []
        
        self.x = 325
        self.y = 200
    
    def draw_truck(self, screen):
        """
        Method that draws the representation of the truck onto the screen

        Parameters:
            screen: the pygame display
        """
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
        
    def draw_truck_array(self, screen, x, y, width, length):
        """
        Draws a 25 inch wide slice of the truck onto the screen.
        
        !Remember! 25 in wide is 1/4 the width of the truck irl
        """
        array = pg.draw.rect(screen, (255,255,255),(x,y,width*2,length*2), 2)
        array.center = (x, y)
        
    def draw_all_truck_arrays(self, screen):
        """
           Draws all of the slices of the truck onto the screen.
           Each slice representsa certain and very important area of the truck
        """

        #under
        self.draw_truck_array(screen, self.x,     self.y, 25, 100)
        self.draw_truck_array(screen, self.x+50,  self.y, 25, 100)
        self.draw_truck_array(screen, self.x+100, self.y, 25, 100)
        self.draw_truck_array(screen, self.x+150, self.y, 25, 100)
        
        #down
        self.draw_truck_array(screen, self.x,     self.y+200,  25, 100)
        self.draw_truck_array(screen, self.x+50,  self.y+200,  25, 100)
        self.draw_truck_array(screen, self.x+100, self.y+200,  25, 100)
        self.draw_truck_array(screen, self.x+150, self.y+200,  25, 100)
        
        #sd
        self.draw_truck_array(screen, self.x,     self.y+400,  25, 40)
        self.draw_truck_array(screen, self.x+50,  self.y+400,  25, 40)
        self.draw_truck_array(screen, self.x+100, self.y+400,  25, 40)
        self.draw_truck_array(screen, self.x+150, self.y+400,  25, 40)
