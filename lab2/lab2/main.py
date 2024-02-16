import random
from cards import play_cards

def main():
    # Define the cards
    cards = ['S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA']

    # Shuffle the cards
    random.shuffle(cards)

    # Assign cards to left and right players
    left_cards = cards[:3]
    right_cards = cards[3:6]

    # Determine the winner of the game
    result = play_cards(*left_cards, *right_cards)

    # Print the result
    if result == -1:
        print("Left player wins!")
    elif result == 0:
        print("It's a draw!")
    elif result == 1:
        print("Right player wins!")

if __name__ == "__main__":
    main()