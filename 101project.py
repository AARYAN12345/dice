import random

def roll():
    dice = random.randint(1,6)
    print(dice)
    inp()

def inp():
    r=input("Do you want to roll the dice.y or n")
    if r == "y":
        roll()

    elif r == "n":
        exit()

inp()