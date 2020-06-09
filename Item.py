class item():
    def __init__(self, l, w, we, pal=False):#, ty = 1, val = 1):
        self.length = l
        self.width = w
        #weight in lbs
        self.weight = we
        #is it on a pallet?
        self.pallet = pal
        #4wide, 3wide, 3wideable, 4wideable, 2wide, 1wide

        #sets the 'wideness'
        self.type = getType(self.width)

        #will be initialized in setType()
        self.willPair = None

    #takes width in inches, returns the wide value as integer(1-4) for panels/bases. defaults to -1
    def getType(self , itemWidth):
        itemType = -1
        if(itemWidth<=22):
            itemType = 1
        elif(itemWidth<=49):
            itemType = 2
        elif(itemWidth<=71):
            itemType = 3
        elif(itemWidth<=101):
            itemType = 4

    #takes two item objects as input, returns wide value for combined widths
    def willPair(self , item1 , item2):
        return getType(item1.width , item2.width)
        