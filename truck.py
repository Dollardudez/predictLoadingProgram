import pygame as pg
from item import IItem
from truck_list import TruckList

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
        
        self.underLeft = TruckList(50)
        self.underLeftC = TruckList(50)
        self.underRightC = TruckList(50)
        self.underRight = TruckList(50)
        
        self.downLeft = TruckList(100)
        self.downLeftC = TruckList(100)
        self.downRightC = TruckList(100)
        self.downRight = TruckList(100)
        
        self.levelLeft = TruckList(30)
        self.levelLeftC = TruckList(30)
        self.levelRightC = TruckList(30)
        self.levelRight = TruckList(30)
        
        self.sd_Left = TruckList(25)
        self.sd_LeftC = TruckList(25)
        self.sd_RightC = TruckList(25)
        self.sd_Right = TruckList(25)
        
        self.x = 325
        self.y = 200


    
    def draw_truck(self, screen):
        """
        Method that draws the representation of the truck onto the screen.

        Parameters:
            screen: the pygame display.
        """
        self.font = pg.font.SysFont(None, 24)

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
        
    def draw_truck_list(self, screen, x, y, width, length):
        """
        Blits a 25 inch wide surface of the truck onto the screen.
        
        !Remember! 25 in wide is 1/4 the width of the truck irl.
        """
        surf = pg.Surface((width*2 , length*2))
        surf.fill((183,210,233))

        text = self.font.render("yo",True,(34,139,3))
        surf.blit(text,(20,50))
        array = pg.draw.rect(surf, (255,255,255),(0,0,width*2,length*2), 2)
        screen.blit(surf , (x , y))
        
    def draw_all_truck_lists(self, screen):
        """
           Draws all of the slices of the truck onto the screen.
           Each slice represents a certain and very important area of the truck.
        """

        #under
        self.draw_truck_list(screen, self.x,     self.y, 25, 100)
        self.draw_truck_list(screen, self.x+50,  self.y, 25, 100)
        self.draw_truck_list(screen, self.x+100, self.y, 25, 100)
        self.draw_truck_list(screen, self.x+150, self.y, 25, 100)
        
        #down
        self.draw_truck_list(screen, self.x,     self.y+200,  25, 100)
        self.draw_truck_list(screen, self.x+50,  self.y+200,  25, 100)
        self.draw_truck_list(screen, self.x+100, self.y+200,  25, 100)
        self.draw_truck_list(screen, self.x+150, self.y+200,  25, 100)
        
        #sd
        self.draw_truck_list(screen, self.x,     self.y+400,  25, 40)
        self.draw_truck_list(screen, self.x+50,  self.y+400,  25, 40)
        self.draw_truck_list(screen, self.x+100, self.y+400,  25, 40)
        self.draw_truck_list(screen, self.x+150, self.y+400,  25, 40)



    def add_4_wide_under(self, item):
        """
        Method adds the item to all lists in the under area of the truck.
        """
        self.underLeft.add_item(item)
        self.underLeftC.add_item(item)
        self.underRightC.add_item(item)
        self.underRight.add_item(item)

    def add_4_wide_down(self, item):
        """
        Method adds the item to all lists in the down area of the truck.
        """
        self.downLeft.add_item(item)
        self.downLeftC.add_item(item)
        self.downRightC.add_item(item)
        self.downRight.add_item(item)



    def add_3_wide_under_left(self, item):
        """
        Method adds the item to the 3 leftmost lists in the under area of the truck. 
        """
        self.underLeft.add_item(item)
        self.underLeftC.add_item(item)
        self.underRightC.add_item(item)

    def add_3_wide_under_right(self, item):
        """
        Method adds the item to the 3 rightmost lists in the under area of the truck.
        """
        self.underRight.add_item(item)
        self.underRightC.add_item(item)
        self.underLeftC.add_item(item)

    def add_3_wide_down_left(self, item):
        """
        Method adds the item to the 3 leftmost lists in the down area of the truck.
        """
        self.downLeft.add_item(item)
        self.downLeftC.add_item(item)
        self.downRightC.add_item(item)


    def add_3_wide_down_right(self, item):
        """
        Method adds the item to the 3 rightmost lists in the down area of the truck.
        """
        self.downRight.add_item(item)
        self.downRightC.add_item(item)
        self.downLeftC.add_item(item)




    def add_2_wide_under_left(self, item):
        """
        """
        self.underLeft.add_item(item)
        self.underLeftC.add_item(item)

    def add_2_wide_under_center(self, item):
        """
        """
        self.underLeftC.add_item(item)
        self.underRightC.add_item(item)

    def add_2_wide_under_right(self, item):
        """
        """
        self.underRightC.add_item(item)
        self.underLeftC.add_item(item)

    def add_2_wide_down_left(self, item):
        """
        """
        self.downLeft.add_item(item)
        self.downLeftC.add_item(item)

    def add_2_wide_down_center(self, item):
        """
        """
        self.downLeftC.add_item(item)
        self.downRightC.add_item(item)

    def add_2_wide_down_right(self, item):
        """
        """
        self.downRightC.add_item(item)
        self.downLeftC.add_item(item)



        #####################################################################################################################
        ###### BOOLEAN METHODS ######

    def is_3wide_under_left_even():
        if self.underLeft.height == self.underLeftC.height == self.underRightC.height: return True
        return False

    def is_3wide_under_right_even():
        if self.underRight.height == self.underRightC.height == self.underLeftC.height: return True
        return False
    def is_3wide_down_left_even():
        if self.downLeft.height == self.downLeftC.height == self.downRightC.height: return True
        return False

    def is_3wide_down_right_even():
        if self.downRight.height == self.downRightC.height == self.downLeftC.height: return True
        return False

    def is_4wide_under_even():
        if self.underLeft.height == self.underLeftC.height == self.underRightC.height == self.underRight.height: return True
        return False

    def is_4wide_down_right_even():
        if self.downRight.height == self.downRightC.height == self.downLeftC.height == self.downRight.height: return True
        return False




