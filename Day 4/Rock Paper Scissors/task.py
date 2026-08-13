# Rock Paper Scissors Game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Combining choices into a list.
choices = [rock, paper, scissors]
computer_number = random.randint(0, len(choices))

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# prevent user from choosing number out of range.
if user_choice > 2 or user_choice < 0:
    print("Please choose a valid number")

if user_choice == computer_number:
    print("It's a draw")
    print(choices[computer_number])
    print(choices[user_choice])
elif user_choice == 0 and computer_number == 2:
    print("You win")
    print(choices[computer_number])
    print(choices[user_choice])
elif user_choice == 2 and computer_number == 0:
    print("You lose")
    print(choices[computer_number])
    print(choices[user_choice])
elif user_choice == 1 and computer_number == 2:
    print("You loose")
    print(choices[computer_number])
    print(choices[user_choice])
elif user_choice == 2 and computer_number == 1:
    print("You win")
    print(choices[computer_number])
    print(choices[user_choice])
elif user_choice == 0 and computer_number == 1:
    print("You loose")
    print(choices[computer_number])
    print(choices[user_choice])
else:
    print("You win")
    print(choices[computer_number])
    print(choices[user_choice])

print(f"Comp: {computer_number}, user: {user_choice}")
