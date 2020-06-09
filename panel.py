#panel object
class panel:
    def __init__(self, l, w, we, pal, ty, val):
        self.length = l
        self.width = w
        #weight in lbs
        self.weight = we
        #is it on a pallet?
        self.pallet = pal
        #4wide, 3wide, 3wideable, 4wideable, 2wide, 1wide
        self.type = ty
        self.value = val
