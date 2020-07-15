from item import Item

#panel object
class Panel(Item):
    
    """creates a Panel object. It inherits length, width, and weight
    from its parent class"""
    
    def __init__(self, l, w, we, pal, ty, val):
        super().__init__(self, l, w, we)
        #is it on a pallet?
        self.pallet = pal
        #4wide, 3wide, 3wideable, 4wideable, 2wide, 1wide
        self.type = ty
        #height of the item
        self.value = val
        
    def will_pair_4wide(self, pan2):
        if self.width + pan2.width <= 90 and self.width + pan2.width >= 68 :
            return True
        else : 
            return False
        
        
    def will_pair_3wide(self, pan2):
        if self.width + pan2.width <= 67 and self.width + pan2.width >= 50 :
            return True
        else :
            return False
        
    def will_pair_2wide(self, pan2):
        if self.width + pan2.width <= 45 and self.width + pan2.width >= 30 :
            return True
        else :
            return False
            
        

    
