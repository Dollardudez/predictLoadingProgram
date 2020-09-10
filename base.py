from item import Item
#base object
class Base(Item):
    """
    represents a Base object. It inherits length, width, and weight
    from the Item class
    """
    
    def __init__(self, ty, l, w, we, pal, val):
        super().__init__(l, w, we)
        #is it on a pallet?
        self.pallet = pal
        #midheight, fullheight, lopro, extreme lopro
        self.type = ty
        #height of base
        self.value = val
        
        
    def will_3piggy(self, base2, base3):
        if(self.width + base2.width < 73):
            if(base3.width + self.length  < 100 and base3.width + base2.length  < 100):
                return True
        elif(self.width + base3.width < 73):
            if(base2.width < 40):
                return True
        else: return False
    
