# Number Guessing Game
from random import randint
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Check number against computer number
def check_answer(user_guess, actual_answer, turns):
    """Check guess asnwer against actual anser."""
    if user_guess > actual_answer:
        print("You guessed too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("You guessed too low")
        return turns - 1
    else:
        print(f"You guessed correctly. The answer is {actual_answer}")

# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(art.logo)
    # Choose a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint(1,100)
    print(answer)

    # Let user guess a number
    turns = set_difficulty()


    # Repat the guessing functionality while still have lives
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses you lose!")
            return
        elif guess != answer:
            print("Guess Again")

game()


