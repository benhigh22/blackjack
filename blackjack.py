import random

class Deck:

    def __init__(self):
        self.suit = ["H", "C", "S", "D"]
        self.val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
        self.deck = []

    def make_deck(self):
        for s in self.suit:
            for v in self.val:
                self.deck.append(v + s)
        return self.deck

    def give_one(self):
        card = self.deck.pop()
        return card

    def create_hand(self):
        hand = []
        for card in range(2):
            hand.append(self.give_one())
        return hand


    def get_hand_value(self, hand):
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


deck = Deck()
deck_creation = deck.make_deck()
print(deck_creation)
hit_one = deck.give_one()
hand_creation = deck.create_hand()
print(hand_creation)
hand_value = deck.get_hand_value(hand_creation)
print(hand_value)




class Player:

    def __init__(self):
        self.hand = hand_creation
        self.value = hand_value

    def show_player_hand(self):
        return self.hand

    def player_hand(self):
        return self.value

    def player_hit(self):
        want_hit = input("Do you want to hit? Enter y or n ")
        while True:
            if want_hit == "y":
                print("You've chosen to hit. ")
                return hit_one

            elif want_hit == "n":
                print("You've chosen to stand. ")
                break



player = Player()
show_hand_player = player.show_player_hand()
val_player_hand = player.player_hand()
print(player.player_hit())