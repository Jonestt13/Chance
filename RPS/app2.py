import random

print("Hi I'm Chance! I'm here to help you make a tough decision you've been stuck on. Do you have two options?")
option_1 = input("Option 1: ")
option_2 = input("Option 2: ")

items = ["rock", "paper", "scissors"]
pc_wins = 0
comp_wins = 0
rounds = 0
while (pc_wins < 3 or comp_wins < 3):
    if pc_wins == 2:
        print(f"You win the game!!{option_1}")
        exit()
    if comp_wins == 2:
        print(F"You Lost the game!!{option_2}")
        exit()

    rounds += 1
    champion = input("choose your champion. Rock, Paper, Scissors ")
    comp = random.choice(items)
    if champion == comp:
        print("Tied! lets play again", comp, rounds)
    elif champion.upper() == "PAPER":
        if comp == "scissors":
            print(comp, "You Lost this round!", rounds)
            comp_wins += 1
        else:
            print("You Win this round!", rounds)
            pc_wins += 1
    elif champion.upper() == "ROCK":
        if comp == "paper":
            print(comp, "You Lost this round!", rounds)
            comp_wins += 1
        else:
            print("You Win this round!", rounds)
            pc_wins += 1
    elif champion.upper() == "SCISSORS":
        if comp == "rock":
            print(comp, "You Lost this round!", rounds)
            comp_wins += 1
        else:
            print("You Win this round!", rounds)
            pc_wins += 1
    elif champion == "stop":
        exit()
    elif champion.upper() != "PAPER" and "ROCK" and "SCISSORS":
        print("I didnt get that.")
