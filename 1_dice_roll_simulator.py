import random
import sys

print("WELCOME TO THE DICE ROLL SIMULATOR!!!")
print("=================================")
print("1. ROLL THE DICE        2. EXIT")

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
