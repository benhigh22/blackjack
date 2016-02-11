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


deck = Deck()

deck_creation = deck.make_deck()
player_hit_one = deck.give_player_one()
dealer_hit_one = deck.give_dealer_one()
player_single_card_val = deck.get_player_single_value(player_hit_one)
dealer_single_card_val = deck.get_dealer_single_value(dealer_hit_one)
player_hand_creation = deck.create_player_hand()
player_hand_value = deck.get_player_hand_value(player_hand_creation)
print("Your hand is " + str(player_hand_creation) + " which has a value of " + str(player_hand_value))
dealer_hand_creation = deck.create_dealer_hand()
dealer_hand_value = deck.get_dealer_hand_value(dealer_hand_creation)
print("Dealer's first card is " + str(dealer_hand_creation[0]))

while True:
    want_hit = input("Do you want to hit? Enter y or n ")
    if want_hit == "n":
        print("You've chosen to stand. ")
        print("You're total hand value is " + str(player_hand_value))
        break

    elif want_hit == "y":
        player_hit_one = deck.give_player_one()
        player_single_card_val = deck.get_player_single_value(player_hit_one)
        player_hand_value += player_single_card_val
        print("You've chosen to hit. ")
        print("You're card is a " + str(player_hit_one) + " with a value of " + str(player_single_card_val))
        print ("You're total hand value is " + str(player_hand_value))
        if player_hand_value > 21:
            print("You busted! ")
            break

    else:
        print("Not a valid choice. Do you want to hit? Enter y or n ")
        continue


while True:

    if dealer_hand_value >= 17 and dealer_hand_value <= 21:
        print("Dealer has chosen to stand. ")
        print("Dealer's total is " + str(dealer_hand_value))
        break

    elif dealer_hand_value < 17:
        dealer_hit_one = deck.give_dealer_one()
        dealer_single_card_val = deck.get_dealer_single_value(dealer_hit_one)
        dealer_hand_value += dealer_single_card_val
        print("Dealer has chosen to hit. ")
        print("Dealer's new total is " + str(dealer_hand_value))
        if dealer_hand_value >= 17 and dealer_hand_value <= 21:
            print("Dealer has chosen to stand. ")
            print("Dealer's total is " + str(dealer_hand_value))
            break
        elif dealer_hand_value > 21:
            print("Dealer busted!")
            break

def outcome():

    if player_hand_value > 21:
        return "You lose!"
    elif dealer_hand_value > 21:
        return "You win!"
    elif player_hand_value > dealer_hand_value:
        return "You win!"
    elif player_hand_value < dealer_hand_value:
        return "You lose."
    elif player_hand_value == dealer_hand_value:
        return "You pushed with the dealer!"

print(outcome())


