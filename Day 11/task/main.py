# Blackjack game
import random

user_card = []
computer_card = []

def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Adds 2 cards to user and computer cards
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())