# BMI calculator with different output depending on weight and height
weight = int(input("Enter a weight: "))
height = float(input("Enter a height: "))

bmi = round(weight / (height ** 2), 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi} which is underweight. ")
elif bmi < 25:
    print(f"Your bmi is {bmi} which is normal weight.")
else:
    print(f"Your bmi is {bmi} which is overweight.")