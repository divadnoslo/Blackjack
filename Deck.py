import numpy as np
import Card as Card

class Deck:

    def __init__(self):
        self.cards = []
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        increment = 0
        for ii in suits:
            for jj in values:
                self.cards.append(Card.Card(jj,ii))
                increment += 1

    def get_number_of_cards(self):
        return len(self.cards)
    
    def print(self):
        for k in range(0, self.get_number_of_cards()):
            self.cards[k].print()

    # def shuffle(self):
    #    number_of_cards = self.get_number_of_cards()
    #    indicies = range(0, number_of_cards)
    #    new_indices = np.sort(indicies
    #    self.cards.

    def deal_card(self):
        if self.get_number_of_cards() == 0:
            print(f'There are no more cards in the deck!')
        else:
            return self.cards.pop()