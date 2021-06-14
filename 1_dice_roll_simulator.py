# @author : ANISHK YADAV

# DICE ROLL SIMULATION USING PYTHON RANDOM MODULE


import random
import sys

print("WELCOME TO THE DICE ROLL SIMULATOR!!!")
print("=================================")
print("Please Select The Number Of Dice")
no_dice = int(
    input("|| One Die: 1 || Two Dice: 2 || Three Dice: 3 || Four Dice: 4 || -> "))
print("1. ROLL THE DICE        2. EXIT")
if no_dice == 1:

    while True:
        cmd = int(input("What Do You Want To Do?: "))
        if cmd == 1:
            print("DICE ROLLED: ", random.randint(1, 6))

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

elif no_dice == 2:
    while True:
        cmd = int(input("What Do You Want To Do?: "))
        if cmd == 1:
            print("DICE 1 ROLLED: ", random.randint(1, 6))
            print("DICE 2 ROLLED: ", random.randint(1, 6))

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

elif no_dice == 3:
    while True:
        cmd = int(input("What Do You Want To Do?: "))
        if cmd == 1:
            print("DICE 1 ROLLED: ", random.randint(1, 6))
            print("DICE 2 ROLLED: ", random.randint(1, 6))
            print("DICE 3 ROLLED: ", random.randint(1, 6))

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

elif no_dice == 4:
    while True:
        cmd = int(input("What Do You Want To Do?: "))
        if cmd == 1:
            print("DICE 1 ROLLED: ", random.randint(1, 6))
            print("DICE 2 ROLLED: ", random.randint(1, 6))
            print("DICE 3 ROLLED: ", random.randint(1, 6))
            print("DICE 4 ROLLED: ", random.randint(1, 6))

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

else:
    print("INVALID NUMBER! PLEASE TRY AGAIN!")
