import random

class Deck:

    def __init__(self):
        self.suit = ["Hearts", "Clubs", "Spades", "Diamonds"]
        self.val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
        self.deck = []

    def make_deck(self):
        for s in self.suit:
            for v in self.val:
                self.deck.append(v + " of " + s)
        return random.shuffle(self.deck)

    def give_player_one(self):
        card = self.deck.pop()
        return card

    def give_dealer_one(self):
        card = self.deck.pop()
        return card

    def create_player_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_player_one())
        return hand

    def create_dealer_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_dealer_one())
        return hand


    def get_player_hand_value(self, hand):
       d = 0
       for card in hand:
           for value in card[0]:
               try:
                   value = int(value)
                   if int(value) == 1:
                       value = 10
               except ValueError:
                   if value == 'A':
                       value = 11
                   elif value in 'JQK':
                       value = 10
           d += int(value)
       return d

    def get_dealer_hand_value(self, hand):
       d = 0
       for card in hand:
           for value in card[0]:
               try:
                   value = int(value)
                   if int(value) == 1:
                       value = 10
               except ValueError:
                   if value == 'A':
                       value = 11
                   elif value in 'JQK':
                       value = 10
           d += int(value)
       return d


    def get_player_single_value(self, card):
        d = 0
        for value in card[0]:
            try:
                value = int(value)
                if int(value) == 1:
                    value = 10
            except ValueError:
               if value == 'A':
                   value = 11

               elif value in 'JQK':
                   value = 10
        d += int(value)
        return d

    def get_dealer_single_value(self, card):
        d = 0
        for value in card[0]:
            try:
                value = int(value)
                if int(value) == 1:
                    value = 10
            except ValueError:
               if value == 'A':
                   value = 11
               elif value in 'JQK':
                   value = 10
        d += int(value)
        return d

