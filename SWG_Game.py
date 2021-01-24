#Snake water Gun Game

"""
Developer: Mukesh Kumar
Date Created: 2021-01-25
"""

import random
User = 0
Comp = 0
i = 1
try:
    def IntoGame():
        """This Function contains scripts for the Game(Snake,Water,Gun)"""

        List = ["S", "W", "G"]
        print("\n\n\t ********Welcome to the Game....!******** \n \nPlease Choose and Enter Your Choice from below:")
        print("\t S for Snake")
        print("\t W for Water")
        print("\t G for Gun")

        while (True):
            NoOfAttemps = input("Enter No of attempts you want to play:")
            if NoOfAttemps.isnumeric() == False or NoOfAttemps is None:
                print("Please enter valid numeric value!")
                continue
            else:
                NoOfAttemps = int(NoOfAttemps)
                break

        global i, Comp, User
        while i <= NoOfAttemps:
            inp = input("\nEnter Your Choice of Option..:")
            inp = inp.upper()
            result = random.choice(List)

            if inp in List:
                if result == inp:
                    print(f"Match! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
                elif result == "S" and inp == "W":
                    Comp += 1
                    print(f"Computer Won! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
                elif result == "W" and inp == "S":
                    User += 1
                    print(f"You Won! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
                elif result == "S" and inp == "G":
                    User += 1
                    print(f"You Won! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
                elif result == "G" and inp == "S":
                    Comp += 1
                    print(f"Computer Won! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
                elif result == "W" and inp == "G":
                    Comp += 1
                    print(f"Computer Won! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
                elif result == "G" and inp == "W":
                    User += 1
                    print(f"You Won! \nComputer Result is: {result} \nYour Input was: {inp}")
                    print(f"\nTotal Attempts Left: {NoOfAttemps-i}")
                    i += 1
            else:
                print(f"\nInvalid Input..! {inp}")
except Exception as e:
    print(f"Some unwanted error occured. Please try again! {e}")
    IntoGame()

IntoGame()

#Final Score Results
if User > Comp:
    print(f"\nGame Over..! \n\nWoohoo..! You Won. Final Score is here: \n\tYour Score: {User} \n\tComputer Score: {Comp}")
elif User < Comp:
    print(f"\nGame Over..! \n\nComputer Won..!. Final Score is here: \n\tYour Score: {User} \n\tComputer Score: {Comp}")
else:
    print(f"\nGame Over..! \n\nIts a Tie..!. Final Score is here: \n\tYour Score: {User} \n\tComputer Score: {Comp}")
