# Blackjack game
import random

def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take list of cards and return total score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
game_over = False

# Adds 2 cards to user and computer cards
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
    else:
        user_deal = input("Type 'y' for another card, type 'n' to pass: ")
        if user_deal == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)