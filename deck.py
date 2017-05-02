'''
Created on 11 apr. 2017

@author: Phili
'''

import random
import itertools


class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = []
        self.spelbara = []
        self.starting_hand = None
        self.score = 0
        self.first = False
    
    def __str__(self):
        return str(self.name)
    def __getitem__(self, i):
        namn = str(self.name)
        return namn[i]
class Card:
    def __init__(self, name, value, gurka_value=None):
        self.name = name
        self.value = value
        self.player = None
        self.gurka_value = gurka_value
    def __str__(self):
        return str(self.name)
class Deck:
    def __init__(self, num_decks = 1):
        self.num_decks = num_decks
        self.deck = self.create_deck()
    def create_deck(self):
        deck = []
        suits = ['Hearts', 'Spades', 'Cloves', 'Diamonds']
        ranks = ["2","3","4","5","6","7","8","9","10","11","12","13","15"]
        for i in suits:
            for j in ranks:
                
                    
                if j == "11":
                    kort = Card("Jack of "+i, int(j))
                    deck.append(kort)
                elif j == "12":
                    kort = Card("Queen of "+i, int(j))
                    deck.append(kort)
                elif j == "13":
                    kort = Card("King of "+i, int(j))
                    deck.append(kort)
                elif j == "15":
                    kort = Card("Ace of "+i, int(j))
                    deck.append(kort)
                else:
                    kort = Card(j + " of " +i, int(j))
                    deck.append(kort)
        return deck
    def shuffle(self):
        deck = self.deck
        random.shuffle(deck)
        self.deck = deck
                
        