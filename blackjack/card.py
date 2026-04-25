
class Card:

    def __init__(self,suit,rank):
        self.rank = rank
        self.suit = suit


    def __str__(self):
        return self.rank  + ' of ' +  self.suit    
    
    def __repr__(self):
        return self.__str__()