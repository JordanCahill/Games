import os
import random

# TODO: Possibly implement suits using Unicode chars ♠♥♦♣
deck = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"] * 4


def deal(deck):
    hand =[]
    for i in range(2):
        card = deck.pop()
        hand.append(card)
    return hand


def hit(hand):
    card=deck.pop()
    hand.append(card)
    return(hand)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_scores(dealer_hand, player_hand):
    print("The dealer has: " + str(dealer_hand) + " giving a score of: " + str(get_hand_value(dealer_hand)))
    print("You have: " + str(player_hand) + " giving a score of: " + str(get_hand_value(player_hand)))


def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again in {"y", "yes"}:
        game()
    else:
        print("Thanks for playing..")
        exit()


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
        if card in {"J", "Q", "K"}:
            value += 10
        elif card == "A":
            if value > 10:
                value += 1
            else:
                value += 11
        else:
            value += card
    return value


def evaluate(dealer_hand, player_hand):
    if get_hand_value(player_hand) == 21:
        print("Blackjack! You win!")
    elif get_hand_value(dealer_hand) > 21:
        print("Dealer busts. You win!")
    elif get_hand_value(player_hand) < get_hand_value(dealer_hand):
        print("Hard luck. You lose.")
    elif get_hand_value(player_hand) > get_hand_value(dealer_hand):
        print("Congratulations. You win")
    play_again()


def game():
    random.shuffle(deck)
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    player_turn = True

    # Case where player receives blackjack in first hand, they win
    if check_blackjack(dealer_hand,player_hand) == 1:
        player_turn = False
        print("Blackjack, you win!")
        play_again()

    while player_turn:
        print_scores(dealer_hand, player_hand)
        if get_hand_value(player_hand) > 21:
            print("Bust! You lose..")
            play_again()
        choice = input("Would you like to hit or stand? (Enter [H]/[S]) ").lower()
        if choice in {"h", "hit"}:
            player_hand = hit(player_hand)
        else:
            player_turn = False

    while get_hand_value(dealer_hand) < 17:
        print("Dealer draws a card..")
        dealer_hand = hit(dealer_hand)
        print_scores(dealer_hand, player_hand)

    evaluate(dealer_hand, player_hand)


if __name__ == '__main__':
    game()