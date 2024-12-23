import Card
import Deck
import BlackjackHand

if __name__ == '__main__':

    # Start Game
    print(f'Welcome to Bootleg Blackjack!')
    print(f' ')

    # Initialize Game
    deck = Deck.Deck()
    my_hand = BlackjackHand.BlackjackHand()
    dealers_hand = BlackjackHand.BlackjackHand()
    
    # Get the Game Started
    number_of_rounds = 1
    user_input = 'Start'
    while user_input != 'Quit':
        
        # Deal Hand
        print(f'Dealing round number {number_of_rounds}')
        my_hand.receive_card(deck.deal_card())
        dealers_hand.receive_card(deck.deal_card())
        my_hand.receive_card(deck.deal_card())
        dealers_hand.receive_card(deck.deal_card())

        # Print Hand
        print(f'My hand:')
        print(f'{my_hand[0]}')



        # End the Game
        user_input = 'Quit'
