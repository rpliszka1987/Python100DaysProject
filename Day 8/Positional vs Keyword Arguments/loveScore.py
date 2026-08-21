# Love score calculator
def calculate_love_score(name1, name2):
    names = name1 + name2
    true_score = 0
    love_score = 0
    for letter in names:
        if letter == "t":
            true_score += 1
        elif letter == "r":
            true_score += 1
        elif letter == "u":
            true_score += 1
        elif letter == "e":
            true_score += 1

    for letter in names:
        if letter == "l":
            love_score += 1
        elif letter == "o":
            love_score += 1
        elif letter == "v":
            love_score += 1
        elif letter == "e":
            love_score += 1

    print(f"{true_score}{love_score}")

calculate_love_score("robert", "heidi")