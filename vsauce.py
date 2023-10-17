
#!/usr/bin/python3
#Archer Fortier
#Vsauce2 - A Game You Can Always Win - https://youtu.be/dUXW3Kh_kxo

#computer vs human: winner is the first to get to 100 without going over.
#level 1: computer makes random guesses
#level 2: computer makes random guess until 50 and then moves to optimal strategy.
#level 3: the computer always plays optimal strategy.

#TODO:
#Fix the counting system for the player and the computer
#Maybe keep score in a file?

import random

# Initiate all used variables to 0
number = 0
useradd = 0
cpuadd = 0
turn = 0
difficulty = 0

def start(difficulty):
    difficulty = 0
    print("Welcome to The 100 Game!")
    difficulty = int(input("What difficulty would you like to play? (1-3)\n"))
    difficulty = int(difficulty)
    if difficulty > 3 or difficulty < 1:
        print("That is not a valid difficulty option, please try again.\n")
        difficulty = 0
        start(difficulty)
    return difficulty

def userturn(number):
    useradd = int(input("Please enter your number. (1-10)\n"))
    if useradd > 10 or useradd < 1:
        print("That number isn't between 1 and 10, please enter a number between 1 and 10")
        return userturn(number)  # Return the result of the recursive call
    elif useradd + number > 100:
        print("That number is too high, please enter a smaller number so you don't pass 100")
        return userturn(number)  # Return the result of the recursive call
    else:
        number += useradd
        print(f"The new number is {number}.\n")
    return useradd, number

def computerrandom(number):
    cpuadd = random.randint(1, 10)
    if cpuadd + number > 100:
        return computerrandom(number)
    else:
        number += cpuadd
        print(f"The computer chose {cpuadd}, the new number is {number}.")
    return number

def computerturn(useradd, difficulty, number):
    print("DEBUG: `USERADD` after being passed to `COMPUTERTURN` function:", useradd)
    if difficulty == 1:
        number = computerrandom(number)
    elif difficulty == 2:
        if number < 50:
            number = computerrandom(number)
        else:
            cpuadd = 11 - useradd
            number += cpuadd
            print(f"The computer chose {cpuadd} the new number is {number}.")
    elif difficulty == 3:
        if useradd == 0:
            computerrandom(number)
        else:
            cpuadd = 11 - useradd
            number += cpuadd
            print(f"The computer chose {cpuadd} the new number is {number}.")
    else:
        print(f"difficulty variable is invalid? The current difficulty variable is:{difficulty}. Fix something.")
        quit()
    return number

difficulty = start(difficulty)
turn = random.randint(0, 1)

if turn == 0:
    print("You get to go first!")
else:
    print("The computer will go first.")

while number < 100:
    if turn == 0:
        useradd, number = userturn(number)
        turn = 1
    else:
        number = computerturn(useradd, difficulty, number)
        turn = 0

if turn == 0:
    print("The computer wins, better luck next time!")
elif turn == 1:
    print("You win! Great job!")
else:
    print("The turn variable is invalid. How did you do that? Turn:", turn)