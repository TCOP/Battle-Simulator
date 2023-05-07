#Build 0.3 Stable

import random
import sys

# CONTANTS
Morale1 = 100
Morale2 = 100
Days = 0


def Roll():
    roll = random.randint(1,9)
    return roll


def Battle():
    global Morale1, Morale2  
    Morale1 = Morale1 - (0.5 * Roll())
    Morale2 = Morale2 - (0.5 * Roll())

    #if random.choice([True, False]):
       # Morale1 = Morale1 - morale_loss1
       # Morale2 = Morale2 - morale_loss2
    #else:
       # Morale2 = Morale2 - morale_loss2
       # Morale1 = Morale1 - morale_loss1


while Morale1 > 0 and Morale2 > 0:
    Battle()
    print(f"Day {Days}")
    print(f"Army 1 Morale: {Morale1}")
    print(f"Army 2 Morale: {Morale2}")
    print("")
    Days += 1


if Morale1 <= 0:
    print("Army 2 wins!")
    print(f"Morale: {Morale2}")
elif Morale2 <= 0:
    print("Army 1 wins!")
    print(f"Morale: {Morale1}")

sys.exit()


