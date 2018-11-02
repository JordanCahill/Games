'''

Author: Jordan Cahill
Date: 30/10/2018

Command line implementation of the classic BlackJack (or 21) card game
At the moment only supports player vs dealer

The aim is to get as close as you can to 21 without going above it.
Numeric cards are worth their face value (2♠ = 2, 10♦ = 10)
Ace is worth 1 or 11 depending on your score; J, Q, and K are all worth 10

You're dealt 2 cards, dealer dealt 1, and given two choices - hit or stand;
Hit - Dealer gives you another card
Stand - You're happy with your cards and pass play to next player

The dealer then draws cards until he reaches at least 17. Whoever has the closest to 21 but not above it, wins.

'''

import os
import random

# TODO: Possibly implement suits using Unicode chars ♠♥♦♣
deck = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
        "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
        "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
        "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]

# Players balance - starts at $10.00 at the beginning of the game and is updated after each game
# Global wager variable used to update balance and reset each game
# TODO: Store this in a server?
balance = 10.0
wager = 0


# To prevent the game from running out of cards
def replace_deck():
    global deck
    deck = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
            "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥",
            "A♦", "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦",
            "A♣", "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣"]
    random.shuffle(deck)
    return deck


# Deal a hand
def deal(deck, i=None):

    if i is "dealer":  # If flag is set, deal one card (dealer case)
        num_cards = 1
    else:
        num_cards = 2

    hand = []

    for j in range(num_cards):
        if not deck:
            deck = replace_deck()
        card = deck.pop()
        hand.append(card)
    return hand


def hit(hand):
    global deck
    if not deck:
        deck = replace_deck()
    card=deck.pop()
    hand.append(card)
    return hand


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_scores(dealer_hand, player_hand):
    print("The dealer has: " + str(dealer_hand) + " giving a score of: " + str(get_hand_value(dealer_hand)))
    print("You have: " + str(player_hand) + " giving a score of: " + str(get_hand_value(player_hand)))


def bet():
    global balance, wager
    wager = 0
    while wager is 0:
        try:
            print("Your balance is $" + str(balance))
            user_in = float(input("Enter your wager:"))
            if balance > user_in > 0:
                wager = user_in
            else:
                print("You can't afford that!")
        except ValueError:
            print("That's not a number..")

    balance = balance - wager


def play_again():

    valid_choice = False
    while valid_choice is False:
        choice = input("Do you want to play again? (Y/N) : ").lower()
        if choice in {"y", "yes", "[y]"}:  # Case 1: Betting commences and new game begins
            valid_choice = True
            bet()
            game()
        elif choice in {"n", "no", "[n]"}:  # Case 2: Exit game
            valid_choice = True
            print("Thanks for playing.. you finished with $" + str(balance))
            exit()
        else:  # Default case
            print("That's not an option, please use [Y] to play again or [N] to quit")


def check_blackjack(dealer_hand, player_hand):
    if get_hand_value(player_hand) == 21:
        return 1
    elif get_hand_value(dealer_hand) == 21:
        return 2
    else:
        return 0


def get_hand_value(hand):
    value = 0
    for card in hand:
        for i in range(2,10):
            if str(i) in card:
                value += i
        if ("J" in card) or ("Q" in card) or ("K" in card):
            value += 10
        elif "A" in card:
            if value > 10:
                value += 1
            else:
                value += 11
    return value


def evaluate(dealer_hand, player_hand):
    global balance, wager
    if get_hand_value(player_hand) == 21:
        print("Blackjack! You win!")
        balance = balance + (wager * 2)
    elif get_hand_value(dealer_hand) > 21:
        print("Dealer busts. You win!")
        balance = balance + wager * 2
    elif get_hand_value(player_hand) < get_hand_value(dealer_hand):
        print("Hard luck. You lose.")
    elif get_hand_value(player_hand) > get_hand_value(dealer_hand):
        print("Congratulations. You win")
        balance = balance + wager *2
    elif get_hand_value(player_hand) == get_hand_value(dealer_hand):
        print("Draw, you got your money back.")
        balance = balance + wager
    play_again()


def game():
    global wager, balance
    random.shuffle(deck)
    dealer_hand = deal(deck, "dealer")
    player_hand = deal(deck)
    player_turn = True

    # Case where player receives blackjack in first hand, they win
    if check_blackjack(dealer_hand,player_hand) == 1:
        print_scores(dealer_hand,player_hand)
        player_turn = False
        print("Blackjack, you win!")
        balance = balance + (wager * 2.5)
        play_again()

    while player_turn:
        print_scores(dealer_hand, player_hand)
        if get_hand_value(player_hand) > 21:
            print("Bust! You lose..")
            play_again()

        valid_choice = False
        while valid_choice is False:
            choice = input("Would you like to hit or stand? (Enter [H]/[S]) ").lower()
            if choice in {"h", "[h]", "hit"}:
                player_hand = hit(player_hand)
                valid_choice = True
            elif choice in {"s", "[s]", "stand"}:
                player_turn = False
                valid_choice = True
            else:
                print("Please enter [H] to hit or [S] to stand..")

        if len(player_hand) == 5:
            player_turn = False
            print_scores(dealer_hand,player_hand)
            print("Five card trick, you win!")
            balance = balance + (wager * 1.5)
            play_again()

    while get_hand_value(dealer_hand) < 17:
        print("Dealer draws a card..")
        dealer_hand = hit(dealer_hand)
        print_scores(dealer_hand, player_hand)

    evaluate(dealer_hand, player_hand)


if __name__ == '__main__':
    bet()
    game()