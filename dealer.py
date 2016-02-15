from deck import deck


class Dealer():

    def __init__(self):
        self.hand = deck.create_dealer_hand()
        self.value = deck.get_dealer_hand_value(self.hand)
        self.hit_card = deck.give_dealer_one()
        self.hit_val = deck.get_dealer_single_value(self.hit_card)

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
