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
new_player_total = player_single_card_val + player_hand_value
new_dealer_total = dealer_single_card_val + dealer_hand_value


class Player:

    def __init__(self):
        self.hand = player_hand_creation
        self.value = player_hand_value

    def show_player_hand(self):
        return self.hand

    def player_hand(self):
        return self.value

    def player_hit(self):
        want_hit = input("Do you want to hit? Enter y or n ")
        while True:
            if want_hit == "n":
                print("You've chosen to stand. ")
                return player_hand_value

            elif want_hit == "y":
                print("You've chosen to hit. ")
                print("You're card is a " + str(player_single_card_val))
                return new_player_total


player = Player()
show_hand_player = player.show_player_hand()
val_player_hand = player.player_hand()
print(player.player_hit())


class Dealer:

    def __init__(self):
        self.hand = dealer_hand_creation
        self.value = dealer_hand_value

    def show_dealer_hand(self):
        return self.hand

    def dealer_hand(self):
        return self.value

    def dealer_hit(self):
        while True:
            if dealer_hand_value >= 17 and dealer_hand_value <= 21:
                print("Dealer has chosen to stand. ")
                return("Dealer's total is " + str(dealer_hand_value))


            elif dealer_hand_value < 17:
                print("Dealer has chosen to hit. ")
                return("Dealer's new total is " + str(dealer_hand_value + dealer_single_card_val))


    def outcome():
        if want_hit == "y" and dealer_hand_value < 17:
            if new_player_total > 21:
                return "You lose."
            elif new_dealer_total > 21:
                return "You win!"
            elif new_player_total < new_dealer_total:
                return "You lose."
            elif new_dealer_total < new_player_total:
                return "You win!"
            elif new_player_total == new_dealer_total:
                return "You push with the dealer."

        if want_hit == "y" and dealer_hand_value >= 17 and dealer_hand_value <= 21:
            if new_player_total > 21:
                return "You lose."
            elif new_player_total < dealer_hand_value:
                return "You lose."
            elif dealer_hand_value < new_player_total:
                return "You win!"
            elif new_player_total == dealer_hand_value:
                return "You push with the dealer."

        elif want_hit == "n" and dealer_hand_value < 17:
            if new_dealer_total > 21:
                return "You win!"
            elif player_hand_value > new_dealer_total:
                return "You win!"
            elif player_hand_value < new_dealer_total:
                return "You lose."
            elif player_hand_value == new_dealer_total:
                return "You push with the dealer."

        elif want_hit == "n" and dealer_hand_value >= 17 and dealer_hand_value <= 21:
            if player_hand_value > dealer_hand_value:
                return "You win!"
            elif player_hand_value < dealer_hand_value:
                return "You lose."
            elif player_hand_value == dealer_hand_value:
                return "You push with the dealer."

dealer = Dealer
print(dealer.dealer_hit(dealer_hand_value))
print(new_player_total)
print(new_dealer_total)
print(dealer.outcome())

