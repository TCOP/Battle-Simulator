#Build 0.1 Alpha

import random
import sys

# CONTANTS
Morale1 = 100
Morale2 = 100


def Roll():
    roll = random.randint(1,9)
    return roll


def Battle():
    global Morale1, Morale2  
    Morale1 = Morale1 - (0.5 * Roll())
    Morale2 = Morale2 - (0.5 * Roll())


while Morale1 > 0 and Morale2 > 0:
    Battle() 


if Morale1 <= 0:
    print("Side 2 wins!")
    print(f"Morale: {Morale2}")
elif Morale2 <= 0:
    print("Side 1 wins!")
    print(f"Morale: {Morale1}")

sys.exit()


