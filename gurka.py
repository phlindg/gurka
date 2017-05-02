import random
from deck import *
import matplotlib.pyplot as plt
import numpy
from matplotlib.pyplot import grid
import tensorflow as tf
from calcs import *
"""
TODO: FIXA RATT ORDNING NAR DE LAGGER SAMMA KORT == FIXAD TROR JAG
TODO: DET JAG SKA GORA AR ATT ESTIMERA VALUE PA ALLA KORT, MED ML!!!!
TODO: FIXA JOKERFUNKTION == LAGG TILL HOGST SEN
TODO: FIXA BATTRE KORT
"""

def last_max_index2(s):
    m_index = m = 0
    for i, elem in enumerate(s):
        
        if elem >= m:
            m, m_index = elem, i
    return m_index


class Gurka:
    def __init__(self,num_players, deck):
        self.num_players = num_players
        self.deck = deck
        self.players = []
        self.pile = []
        self.spelade_per_rond = []
        self.winning_hands = []
        self.loosing_hands = []
    def mod_deck(self):
        for kort in self.deck:
            if kort.value in [2,15]:
                kort.gurka_value = 5
            if kort.value in [3,4,13]:
                kort.gurka_value = 4
            if kort.value in [5,6,12]:
                kort.gurka_value = 3
            if kort.value in [7,8,9,10,11]:
                kort.gurka_value = 1
        joker = Card("Joker", 16,7)
        self.deck.append(joker)
        self.deck.append(joker)
    def create_players(self):
        
        for i in range(1, self.num_players+1):
            player = Player("Player"+ str(i), None)
            self.players.append(player)
        return self.players
    def deal(self):
        
        m = 0
        while m <6:
            
            for player in self.players:
                kortet = self.deck.pop(0)
                kortet.player = player
                player.hand.append(kortet)
            m+=1
    def toss(self):
        total = []
        for player in self.players:
            player.hand.sort(key = lambda x: x.gurka_value)
            for i in range(3):
                player.hand.pop(0)
            for i in range(3):
                kortet = self.deck.pop(0)
                kortet.player = player
                player.hand.append(kortet)
                
    def round(self, sista_korten,test_sista2, start_index,ii):
      #  print( "NY RUNDA")
        
        players = self.players
        
        sistor = []
        test_sista = [0]*len(players)
        lagda_kort = [0]*len(players)
        a = [x for x in sista_korten if x == max(sista_korten)]
        
        if ii == 1:
                
            index_first = 0
        else:
            if len(a) > 1:
                index_first = start_index
            else:
                index_first = sista_korten.index(max(sista_korten))
        hej = index_first
        while index_first < len(players) + hej:
            senaste = max(lagda_kort)
            
        
            player = players[index_first % len(players)]
  #          print player
   #         for kort in player.hand:
    #            print kort
     #       print ""
            player.hand.sort(key = lambda x: x.value)
            
            if senaste == 0:
                
                player.hand.sort(key = lambda x: x.value)
               # index = random.randint(0,len(player.hand)-1)
                x = player.hand.pop(-1)
                lagda_kort.append(x.value)
                test_sista.append(x)
                senaste = max(lagda_kort)
                sistor.insert(players.index(player),x)
                
                
            else:
                player.hand.sort(key = lambda x: x.value)
                
                if senaste == 16:
                    x = player.hand.pop(0)
                    sistor.insert(players.index(player),x)
                    lagda_kort.append(x.value)
                    test_sista.append(x)
                    senaste = max(lagda_kort)
                elif senaste == 15:
                    poppad = False
                    for i in player.hand:
                        if i.name == "Joker":
                            x = player.hand.pop(player.hand.index(i))
                            poppad = True
                            break
                    if poppad == False:
                        x = player.hand.pop(0)
                    sistor.insert(players.index(player),x)
                    lagda_kort.append(x.value)
                    test_sista.append(x)
                    senaste = max(lagda_kort)
                    
                else:
                    poppad = False
                    kort_index = 0
                    while kort_index < len(player.hand):
                        if player.hand[kort_index].value >= senaste:
                            x = player.hand.pop(kort_index)
                            
                            sistor.insert(players.index(player),x)
                            test_sista.append(x)
                            lagda_kort.append(x.value)
                            poppad = True
                            break
                        kort_index +=1
                            
                    if poppad == False:
                        x = player.hand.pop(0)
                        sistor.insert(players.index(player),x)
                        test_sista.append(x)
                        lagda_kort.append(x.value)
                        senaste = max(lagda_kort)
                            
                    
            player.spelbara = []
            index_first+=1
        sista_korten = []
        test_sista2 = []
        test_sista_sista = []
        test_sista_sista_values = []
        for i in lagda_kort[len(players):]:
            test_sista2.append(i)
        
        for i in test_sista[len(players):]:
            test_sista_sista.append(i)
        for value in test_sista_sista:
            test_sista_sista_values.append(value.value)
       # print(test_sista_sista_values)
        hmm = last_max_index2(test_sista_sista_values)
        
        
        
        for kort in sistor:
            sista_korten.append(kort.value)
       # print(sista_korten)
        cool = test_sista_sista[hmm].player
        wow = int(cool[-1])-1
        return sista_korten, test_sista2,wow
        
    def play(self):
        m = 0
        for player in self.players:
            player.starting_hand = player.hand[:]
        self.players[0].first = True
        x = [0]*len(self.players)
        y = [0]*len(self.players)
        ii = 0
        s = 0
        while m < 6:
            ii+=1
            x,y,s  = self.round(x,y,s,  ii)
            
            m+=1
        a = [b for b in x if b == min(x)]
        if len(a) > 1:
          #  print( "NO WINNER")
            return None, None
        else:
         #   print( "Player"+ str(x.index(min(x))+1)+ " WINS WITH STARTING CARDS BELOW")
            
         #   for i in self.players[x.index(min(x))].starting_hand:
       #         print ("   ",i)
            winning_player = self.players[x.index(min(x))]
            loosing_players = self.players
            loosing_players.remove(winning_player)
            return winning_player, loosing_players
def store(bw,bl,w,l):
    
    for kort in w.starting_hand:
        bw.append(kort.value)
    for player in l:
        for kort in player.starting_hand:
            bl.append(kort.value)


if __name__ == "__main__":
    big_winning = []
    big_loosing = []
        
    n = 100
    for i in range(n):
        deck = Deck()
        spel = Gurka(3, deck.deck)
        spel.mod_deck()
        deck.shuffle()
        
        spel.create_players()
        spel.deal()
      #  spel.toss()
       # print ("SPEL STARTAR")
        
        x,y = spel.play()
        if x:
            store(big_winning,big_loosing,x,y)
    #print( "BW: ",big_winning, "BL: ",big_loosing)
    xx = [2,3,4,5,6,7,8,9,10,11,12,13,15,16]
    yy = calc_winpercent(big_winning,big_loosing)
    plt.scatter(xx,yy)
    plt.grid()
    plt.show()
    
            