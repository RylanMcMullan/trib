import random

x = ["rock", "paper", "scissors"]

while True:
    opp = random.choice(x)
    ask = input("what is your choice? Rock, Paper, or Scissors? Type \"stop\" to exit the loop ").lower()
    print(opp)
    print(ask)

    if ask == "stop":
        break

    elif opp == "rock":
        if ask == "paper" or ask == "p":
            print(f"Congrats you beat {opp}")
            break
        elif ask == "scissors" or ask == "s":
            print(f"You lost to {opp}")
            continue
        elif ask == "rock" or ask == "r":
            print(f"You both entered {ask}, try again")
            continue
        else:
            print("You must enter either Rock Paper or Scissors.")
            continue

    elif opp == "paper":
        if ask == "scissors" or ask == "s":
            print(f"Congrats you beat {opp}")
            break
        elif ask == "rock" or ask == "r":
            print(f"You lost to {opp}")
            continue
        elif ask == "paper" or ask == "p":
            print(f"You both entered {ask}, try again")
            continue
        else:
            print("You must enter either Rock Paper or Scissors.")
            continue

    elif opp == "scissors":
        if ask == "rock" or ask == "r":
            print(f"Congrats you beat {opp}")
            break
        elif ask == "paper" or ask == "p":
            print(f"You lost to {opp}")
            continue
        elif ask == "scissors" or ask == "s":
            print(f"You both entered {ask}, try again")
            continue
        else:
            print("You must enter either Rock Paper or Scissors.")
            continue
