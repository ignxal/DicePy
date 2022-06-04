import random

def parse_input(input_string):
    """
    Check if `input_string` is an integer number between 1-6.
    If so, return an integer with the same value.
    Else, warn user and quit the program.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

def roll_dice(num):
    """
    Return a list of integers with length `num`.
    """
    results = []
    for _ in range(num):
        roll = random.randint(1, 6)
        results.append(roll)
    return results



######################### MAIN ######################### 

# Get Input
num_input = input("Write the amount of dices to be rolled: [1-6] ")
num = parse_input(num_input)

# Let's rock&roll
roll_results = roll_dice(num)
print(roll_results)
