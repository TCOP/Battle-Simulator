#Build 0.6 Stable

import random
import sys
import json
import os

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
    manpowerroll = random.randint(20, 85)
    return manpowerroll


def Battle():
    global Morale1, Morale2, Manpower1, Manpower2, Losses1, Losses2  
    Morale1Damage = (4 * Roll9()) # 4 - 36 damage
    Morale1 = Morale1 - Morale1Damage
    Morale2Damage = (4 * Roll9()) # 4 - 36 damage
    Morale2 = Morale2 - Morale2Damage
    Manpower1 = Manpower1 - (ManpowerRoll() * Morale1Damage)
    Manpower2 = Manpower2 - (ManpowerRoll() * Morale2Damage)
    Losses1 = 10000 - Manpower1
    Losses2 = 10000 - Manpower2


def load_win_counts(filename):
    try:
        with open(filename, "r") as f:
            win_counts = json.load(f)
            print(f"Loaded win_counts: {win_counts}")  # Add this print statement
    except FileNotFoundError:
        win_counts = {"Army 1": 0, "Army 2": 0}
        print(f"File not found, initialized win_counts: {win_counts}")  # Add this print statement
    return win_counts


def save_win_counts(filename, win_counts):
    with open(filename, "w") as f:
        json.dump(win_counts, f)
        print(f"Saved win_counts: {win_counts}")  # Add this print statement


script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

win_counts = load_win_counts("win_counts.json")


while Morale1 > 0 and Morale2 > 0:
    Battle()
    print(f"Day {Days}")
    print(f"Army 1 Morale: {round(Morale1, 1)}")
    print(f"Army 1 Remaining Men: {Manpower1}")
    print(f"Army 2 Morale: {round(Morale2, 1)}")
    print(f"Army 2 Remaining Men: {Manpower2}")
    print("")
    Days += 1


if Morale1 <= 0 and Morale2 <= 0:
    print(f"It's a draw after {Days - 1} Days!")
    print(f"Army 1 Morale: {Morale1}")
    print(f"Army 2 Morale: {Morale2}")
elif Morale1 <= 0:
    print(f"Army 2 wins after {Days - 1} Days!")
    print(f"Morale: {round(Morale2, 1)}")
    win_counts["Army 2"] += 1
    save_win_counts("win_counts.json", win_counts)
elif Morale2 <= 0:
    print(f"Army 1 wins after {Days - 1} Days!")
    print(f"Morale: {round(Morale1, 1)}")
    win_counts["Army 1"] += 1
    save_win_counts("win_counts.json", win_counts)

print(f"Army 1 Casualties: {round(Losses1)} Men")
print(f"Army 2 Casualties: {round(Losses2)} Men")

sys.exit()


print("Hello")
#TESTING TESTING


