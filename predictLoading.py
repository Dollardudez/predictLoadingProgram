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
        return
                
# any(email_service in user_email for email_service in email_services)

    def item_flow(item):
        if type(item) == Base:
            return "Base"
        elif type(item) == Top:
            return "Top"
        elif type(item) == Panel:
            return "Top"
        else:
            return;

    def base_flow(base):
        if 62 > base.length >= 50: return 3
        elif base.length < 50: return 2

    def top_flow(top):
        if top.length > 72: return 4;
        elif top.length >= 50: return 3;
        else: return 2

    def panel_flow(panel):
        if panel.width >= 71: return 4
        elif panel.width >= 50: return 3
        elif panel.width >= 30: return 2
        else: return 1

    def panel_3wide_flow(panel: Panel, list: [], truck: Truck):
        if truck.is_3wide_down_left_even():
            truck.add_3_wide_under_left(panel)
        elif truck.is_3wide_under_right_even():
            truck.add_3_wide_under_right
        elif truck.is_3wide_down_left_even():
            truck.add_3_wide_down_left
        elif truck.is_3wide_down_right_even():
            truck.add_3_wide_down_right

    def panel_4wide_flow(panel: Panel, list: [], truck: Truck):
        if truck.is_4wide_under_even(): truck.add_4_wide_under()
        if truck.is_4wide_down_even(): truck.add_4_wide_down()

    
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