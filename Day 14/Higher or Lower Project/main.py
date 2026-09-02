# Higher or Lower Game Project
import random
from game_data import data
# Display art
from art import logo, vs
def format_data(account):
    # Format the account data into printable format
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Check if the user guesses the correct answer."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)

# Make the game repeatable
while continue_game:
    # Generate a random account from the game data

    # Making accounts at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    # Makes user the account dont genearate same comparison
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong! Final Score: {score}")
        continue_game = False




