# Pizza claculator
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
totalBill = 0

if size == "S":
    totalBill += 15
    if pepperoni == "Y":
        totalBill += 2
elif size == "M":
    totalBill += 20
elif size == "L":
    totalBill += 25
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    if size == "S":
        totalBill += 2
    else:
        totalBill += 3

if extra_cheese == "Y":
    totalBill += 1

print(f"Your total is ${totalBill}")