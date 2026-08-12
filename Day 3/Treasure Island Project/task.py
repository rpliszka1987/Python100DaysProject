print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

rightOrLeft = input(" Do you want to go right or left? ")
if rightOrLeft == "left":
    swimOrWait = input(" Do you want to swim or wait? ")
    if swimOrWait == "wait":
        doorChoice = input("Which door do you want to open? Red , Blue, or Yellow? ")
        if doorChoice == "yellow":
            print("You Win!")
        elif doorChoice == "red":
            print("Burned by fie. Game Over!")
        elif doorChoice == "blue":
            print("Eaten by beasts. Game Over!")
        else:
            print("Game Over!")
    elif swimOrWait == "swim":
        print("You been attacked by trout. Game Over!")
    else:
        print("Please enter either 'wait' or 'swim'")
elif rightOrLeft == "right":
    print("You fell into a hole. Game Over!")
else:
    print("Please choose from right or left.")