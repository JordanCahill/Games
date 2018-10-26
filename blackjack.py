import os
import random

deck = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] * 4


def deal(deck):
    hand =[]
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand


def get_hand_value(hand):
    value = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            value += 10
        elif card == "A":
            if value > 10:
                value += 1
            else:
                value += 11
        else:
            value += card
    return value


def hit(hand):
    card=deck.pop()
    hand.append(card)
    return(hand)

clear = lambda: os.system('cls')
#def clear():
    #os.system('cls' if os.name == 'nt' else 'clear')

def print_scores(dealer_hand, player_hand):
    clear()
    print(dealer_hand)

random.shuffle(deck)
for i in range(1,10):
    hand = deal(deck)
    print(hand)
    print(get_hand_value(hand))
    hand=hit(hand)
    print(hand)
    print(get_hand_value(hand))
print_scores(hand,hand)