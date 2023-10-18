
#!/usr/bin/python3
#ProSlimer
#Vsauce2 - A Game You Can Always Win - https://youtu.be/dUXW3Kh_kxo

#computer vs human: winner is the first to get to 100 without going over.
#level 1: computer makes random guesses
#level 2: computer makes random guess until 50 and then moves to optimal strategy.
#level 3: the computer always plays optimal strategy.

#To Do:
#Clean up the code a bit. It is kinda hard to follow at this point. I jsut got shit everywhere

import random

# Initiate all used variables to 0
number = 0
useradd = 0
cpuadd = 0
turn = 0
difficulty = 0
scores = [0, 0]

# Read scores from the file
file_path = "D:/Documents/PyProjects/Vsauce-100-Game/scores.txt"  # Replace with the actual file path
try:
    with open(file_path, "r") as score_file:
        player_score, computer_score = map(int, score_file.readline().strip().split(","))
        scores = [computer_score, player_score]  # Update scores based on the file data
except FileNotFoundError:
    # Handle the case where the file doesn't exist
    scores = [0, 0]  # Initialize scores with default values

def start(difficulty):
    while True:
        try:
            print(
                f'''
                ============================
                |                          |
                | Welcome to The 100 Game! |
                |                          |
                ============================
                        SCOREBOARD
                ============================
                Player:                    {scores[1]}
                Computer:                  {scores[0]}
                '''
            )
            input_difficulty = input("What difficulty would you like to play? (1-3)\n")
            difficulty = int(input_difficulty)
            if difficulty not in {1, 2, 3}:
                raise ValueError("Invalid difficulty selection")
            break  # Exit the loop if a valid difficulty is selected
        except ValueError:
            print("That is not a valid difficulty option, please try again.\n")
    
    return difficulty

def userturn(number):
    useradd = input("Please enter your number. (1-10)\n")
    # Convert useradd to an integer
    useradd = int(useradd)
    
    if useradd > 10 or useradd < 1:
        print("That number isn't between 1 and 10, please enter a number between 1 and 10")
        return userturn(number)
    elif useradd + number > 100:
        print("That number is too high, please enter a smaller number so you don't pass 100")
        return userturn(number)
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
    if difficulty == 1:
        number = computerrandom(number)
    elif difficulty == 2:
        if number < 50:
            number = computerrandom(number)
        else:
            cpuadd = min(11 - useradd, 100 - number)  # Ensure the total doesn't go over 100
            number += cpuadd
            print(f"The computer chose {cpuadd} the new number is {number}.")
    elif difficulty == 3:
        if useradd == 0:
            number = computerrandom(number)  # Computer chooses a random number if it's turn is first
        else:
            cpuadd = min(11 - useradd, 100 - number)  # Ensure the total doesn't go over 100
            number += cpuadd
            print(f"The computer chose {cpuadd} the new number is {number}.")
    else:
        print(f"Difficulty variable is invalid? The current difficulty variable is:{difficulty}. Fix something.")
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
    scores[0] += 1  # Increment the computer's score
elif turn == 1:
    print("You win! Great job!")
    scores[1] += 1  # Increment the player's score
else:
    print("The turn variable is invalid. How did you do that? Turn:", turn)

# Save the scores list to a file with the specified path
file_path = "D:/Documents/PyProjects/Vsauce-100-Game/scores.txt"
with open(file_path, "w") as score_file:
    score_file.write(f"{scores[1]},{scores[0]}\n")