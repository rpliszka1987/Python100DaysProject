# Prime Number Checker
user_number = int(input("Please enter a number to check: "))

def is_prime(num):
    # Any number under 1
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(user_number))