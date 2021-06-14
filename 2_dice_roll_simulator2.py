# @author : ANISHK YADAV

# DICE ROLL SIMULATION USING PYTHON RANDOM MODULE


import random
import sys

print("WELCOME TO THE DICE ROLL SIMULATOR!!!")
print("=================================")
print("Please Enter The Number Of Dice You Want To Roll")
no_dice = int(
    input("||ENTER A NUMBER|| -> "))
print("1. ROLL THE DICE        2. EXIT")
while True:
    cmd = int(input("What Do You Want To Do? 1 or 2: "))
    if cmd == 1:
        for i in range(1, no_dice + 1):
            print("DICE", i, "ROLLED: ", random.randint(1, 6))

    elif cmd == 2:
        print("Are You Sure Want To Quit?")
        quits = input("Type Yes Or No: ")
        if quits == 'Yes':
            sys.exit()
        elif quits == 'No':
            continue
        else:
            print("INVALID COMMAND!")
            continue

    else:
        print("INVALID COMMAND!!!")
        continue
