import numpy as np
import Card
import Deck

class BlackjackHand:

    def __init__(self):
        self.hand = []
        self.ace_status = 'Hard'

    def receive_card(self, card):
        self.hand.append(card)

    def get_blackjack_value(self):
        value = 0
        if len(self.hand) > 0:
            for k in range(0, len(self.hand)):
                if self.hand[k] == 'Ace':
                    value += 1
                    self.ace_status = "Soft"
                elif self.hand[k] == '2':
                    value += 2
                elif self.hand[k] == '3':
                    value += 3
                elif self.hand[k] == '4':
                    value += 4
                elif self.hand[k] == '5':
                    value += 5
                elif self.hand[k] == '6':
                    value += 6
                elif self.hand[k] == '7':
                    value += 7
                elif self.hand[k] == '8':
                    value += 8
                elif self.hand[k] == '9':
                    value += 9
                elif self.hand[k] == '10':
                    value += 10
                elif self.hand[k] == 'Jack':
                    value += 10
                elif self.hand[k] == 'Queen':
                    value += 10
                elif self.hand[k] == 'King':
                    value += 10
        if value > 11:
            self.ace_status = 'Soft'
        return value

    def print(self):
        if len(self.hand) > 0:
            #for k in range(0, len(self.hand)):
                #self.hand[k].print()
            print(f'Total value: {self.get_blackjack_value()}')
        else:
            print('This hand has no cards')


    