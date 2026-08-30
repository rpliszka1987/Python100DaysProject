year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
# Make sure that 1994 is included in the condition
elif year >= 1994:
    print("You are a Gen Z.")
