from deck import deck
from player import Player
from dealer import Dealer

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


    deck.make_deck()
    player = Player()
    dealer = Dealer()


    print("Your hand is " + str(player.hand) + " which has a value of " + str(player.value))
    print("Dealer's first card is " + str(dealer.hand[0]))
    print(player.player())

    if player.value > 21:
        play_again = input("Do you want to play again? Enter y or n ")
        continue

    print(dealer.dealer())

    if dealer.value == 21 and player.value != 21:
        print("Dealer got Blackjack! You lose! ")
        play_again = input("Do you want to play again? Enter y or n ")
        continue

    game = Game()

    print(game.outcome())


    play_again = input("Do you want to play again? Enter y or n ")