import random

def check_straight(card1, card2, card3):
    cards = [card1, card2, card3]
    values = []
    for card in cards:
        value = card[1:]
        if value.isdigit():
            values.append(int(value))
        elif value == 'J':
            values.append(11)  # Jack
        elif value == 'Q':
            values.append(12)  # Queen
        elif value == 'K':
            values.append(13)  # King
        elif value == 'A':
            values.append(14)  # Ace
    values.sort()
    if values[0] + 1 == values[1] and values[1] + 1 == values[2]:
        return values[2]
    else:
        return 0

def check_3ofa_kind(card1, card2, card3):
    if card1[1:] == card2[1:] == card3[1:]:
        return int(card1[1:])
    else:
        return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_straight = check_straight(left1, left2, left3)
    right_straight = check_straight(right1, right2, right3)
    left_3ofa_kind = check_3ofa_kind(left1, left2, left3)
    right_3ofa_kind = check_3ofa_kind(right1, right2, right3)
    left_royal_flush = check_royal_flush(left1, left2, left3)
    right_royal_flush = check_royal_flush(right1, right2, right3)

    if left_royal_flush and not right_royal_flush:
        return -1  # Left player wins with a royal flush
    elif right_royal_flush and not left_royal_flush:
        return 1  # Right player wins with a royal flush
    else:
        # Continue with other comparison logic
        pass
    if left_straight and right_straight:
        if left_straight > right_straight:
            return -1
        elif left_straight < right_straight:
            return 1
        else:
            return 0
    elif left_3ofa_kind and right_3ofa_kind:
        if left_3ofa_kind > right_3ofa_kind:
            return -1
        elif left_3ofa_kind < right_3ofa_kind:
            return 1
        else:
            return 0
    elif left_straight:
        return -1
    elif right_straight:
        return 1
    else:
        return 0