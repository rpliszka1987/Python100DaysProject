from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# Fixed the range from 0 to 5 instead of 1 to 6 to stop error.
dice_num = randint(0, 5)
print(dice_images[dice_num])
