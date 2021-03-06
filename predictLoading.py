from top import Top
from truck import Truck
from base import Base
from panel import Panel
from load import Load
from item import IItem
import copy
from collections import Counter
from linked_list import *


class Predicter:

    def predict_loading(whole_order: [], truck: Truck, num_orders):
        print(len(truck.underLeft.list))
        copy2 = copy.deepcopy(whole_order)

        for i in range(0, num_orders):
            while(whole_order[i].head != None):
                if(whole_order[i].head.data.b_t_p == "base"):
                    copy1 = whole_order[i].copy()
                    base = whole_order[i].head.data
                    while(copy1.head != None):
                        copy1.head = copy1.head.next_node
                        if(copy1.head != None):
                            if(isinstance(copy1.head.data, Base)):
                                print("true instance")
                                if(copy1.head.data.type == base.type ):
                                    if(copy1.head.data == base): continue
                                    print("match!")
                                    truck.underLeft.add_item(base)
                                    truck.underLeftC.add_item(base)
                                    truck.underRightC.add_item(base)
                                    truck.underLeft.add_item(copy1.head.data)
                                    truck.underLeftC.add_item(copy1.head.data)
                                    truck.underRightC.add_item(copy1.head.data)
                elif(whole_order[i].head.data.b_t_p == "top"): print(whole_order[i].head.data.b_t_p)
                whole_order[i].head = whole_order[i].head.next_node
                print("\n")
        count = sum(isinstance(x, IItem) for x in truck.underLeft.list)
        print(count)
        for item in truck.underLeft.list:
            print(item)
        for i in range(0, num_orders):
            while(copy2[i].head != None):
                print(copy2[i].head.data.b_t_p)
                copy2[i].head = copy2[i].head.next_node
                
# any(email_service in user_email for email_service in email_services)

    
"""


font1 = pg.font.Font('freesansbold.ttf', 25) 
        text1 = font1.render('Blue is a Top', True, (0,0,255))
        screen.blit(text1, (300, 5))
        font2 = pg.font.Font('freesansbold.ttf', 25) 
        text2 = font2.render('Red is a Base', True, (255,0,0))
        screen.blit(text2, (500, 5))
        menu.side_menu(screen)
        if(b.x != truck.x+25*2):
            b.x = b.x + 1
        if(b.y != truck.y+100):
            b.y = b.y + 1
        if(t.x != truck.x):
            t.x = t.x + 1
        if(t.y != truck.y):
            t.y = t.y + 1
"""