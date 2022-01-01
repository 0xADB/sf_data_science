"""Guess number game"""

import numpy as np

# Select a number.
number = np.random.randint(1, 101)

# Number of tries,
count = 0

while True:
    count += 1
    predict_number = int(input("Guess number from 1 to 100: "))

    if predict_number > number:
        print("The number is less!")
    elif predict_number < number:
        print("The number is greater!")
    else:
        print(f"Correct! It's {number}, {count} tries.")
        break