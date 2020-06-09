#base object
class base:
    def __init__(self, l, w, we, pal, ty, val):
        self.length = l
        self.width = w
        #weight in lbs
        self.weight = we
        #is it on a pallet?
        self.pallet = pal
        #midheight, fullheight, lopro, extreme lopro
        self.type = ty
        self.value = val
