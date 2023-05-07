#Build 0.3 Stable

import random
import sys

# CONTANTS
Morale1 = 100
Morale2 = 100
Manpower1 = 10000
Manpower2 = 10000
Days = 0


def Roll9():
    roll9 = random.randint(1,9)
    return roll9


def ManpowerRoll():
    manpowerroll = random.randint(1, 50)
    return manpowerroll


def Battle():
    global Morale1, Morale2, Manpower1, Manpower2, Losses1, Losses2  
    Morale1 = Morale1 - (0.5 * Roll9())
    Morale2 = Morale2 - (0.5 * Roll9())
    Manpower1 = Manpower1 - (ManpowerRoll() * Roll9())
    Manpower2 = Manpower2 - (ManpowerRoll() * Roll9())
    Losses1 = 10000 - Manpower1
    Losses2 = 10000 - Manpower2

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
    print(f"Army 1 Remaining Men: {Manpower1}")
    print(f"Army 2 Morale: {Morale2}")
    print(f"Army 2 Remaining Men: {Manpower2}")
    print("")
    Days += 1


if Morale1 <= 0:
    print(f"Army 2 wins after {Days} Days!")
    print(f"Morale: {Morale2}")
elif Morale2 <= 0:
    print(f"Army 1 wins adter {Days} Days!")
    print(f"Morale: {Morale1}")

print(f"Army 1 Casualties: {Losses1} Men")
print(f"Army 2 Casualties: {Losses2} Men")

sys.exit()


