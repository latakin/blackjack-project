import random
from .card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',    'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))


    def shuffle_deck(self):
         random.shuffle(self.deck)
    
    def deal_one(self):
        return self.deck.pop(-1)

    def __str__(self):
        return self.deck