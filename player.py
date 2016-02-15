
from deck import deck

class Player:

    def __init__(self):
        self.hand = deck.create_player_hand()
        self.value = deck.get_player_hand_value(self.hand)
        self.hit_card = deck.give_player_one()
        self.hit_val = deck.get_player_single_value(self.hit_card)

    def player(self):

        while True:

            want_hit = input("Do you want to hit? Enter y or n ")
            if want_hit == "n":
                print("You've chosen to stand. ")
                return("You're total hand value is " + str(self.value))

            elif want_hit == "y":
                self.hit_card = deck.give_player_one()
                self.hit_val = deck.get_player_single_value(self.hit_card)
                self.value += self.hit_val
                print("You've chosen to hit. ")
                print("You're card is a " + str(self.hit_card + " with a value of " + str(self.hit_val)))
                print("You're total hand value is " + str(self.value))
                if self.value > 21:
                    return("Too many, you lose! ")

            else:
                print("Not a valid choice. Do you want to hit? Enter y or n ")
                continue




