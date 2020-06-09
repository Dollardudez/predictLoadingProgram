#top object
class top:
    def __init__(self, l, w, val, pal, we, f):
        self.length = l
        self.width = w
        #weight in lbs
        self.weight = we
        #is it on a pallet?
        self.pallet = pal
        #in a fat box or not?
        self.fat = f
        self.value = val
