# import random of some sort
# make a function that does the random roll
# make a function that asks user input nd calls the random
# roll function
# have it have the option to quit

import random


def roll_number():
    num = random.randint(1, 6)
    return num


def user_input():
    roll = True
    while roll:
        user = input("Press 'r' to roll")
        if user.lower() == "r":
            print(" You rolled: " + str(roll_number()))
        else:
            roll = False
            print("Have a nice day!")


user_input()




