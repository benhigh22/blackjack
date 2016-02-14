from deck import Deck

class Player:

    def __init__(self):
        self.hand = player_hand_creation
        self.value = player_hand_value
        self.hit_card = player_hit_one
        self.hit_val = player_single_card_val

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

class Dealer:

    def __init__(self):
        self.hand = dealer_hand_creation
        self.value = dealer_hand_value
        self.hit_card = dealer_hit_one
        self.hit_val = dealer_single_card_val

    def dealer(self):

        while True:

            if self.value >= 17 and self.value <= 21:
                print("Dealer has chosen to stand. ")
                return("Dealer's total is " + str(self.value))


            elif self.value < 17:
                self.hit_card = deck.give_dealer_one()
                self.hit_val = deck.get_dealer_single_value(self.hit_card)
                self.value += self.hit_val
                print("Dealer has chosen to hit. ")
                print("Dealer's new total is " + str(self.value))
                if self.value >= 17 and self.value <= 21:
                    print("Dealer has chosen to stand. ")
                    return("Dealer's total is " + str(self.value))
                elif self.value > 21:
                    return("Dealer busted!")

class Game:

    def __init__(self):
        self.player_value = player.value
        self.dealer_value = dealer.value

    def outcome(self):
        if self.player_value > 21:
            return "You lose!"
        elif self.dealer_value > 21:
            return "You win!"
        elif self.player_value > self.dealer_value:
            return "You win!"
        elif self.player_value < self.dealer_value:
            return "You lose."
        elif self.player_value == self.dealer_value:
            return "You pushed with the dealer!"



play_again = "y"
while play_again == "y":

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

    player = Player()
    print(player.player())

    if player.value > 21:
        play_again = input("Do you want to play again? Enter y or n ")
        continue

    dealer = Dealer()
    print(dealer.dealer())

    if dealer.value == 21 and player.value != 21:
        print("Dealer got Blackjack! You lose! ")
        play_again = input("Do you want to play again? Enter y or n ")
        continue

    game = Game()
    print(game.outcome())

    play_again = input("Do you want to play again? Enter y or n ")