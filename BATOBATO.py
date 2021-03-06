import random

while True:
    choice = ["Rock", "Paper", "Scissors"]

    userHand = input("Rock, Paper or Scissors: ").title()

    computerHand = (random.choice(choice))

    def game(first, second):

        if userHand == computerHand:
            print("You Chose", first)
            print("Computer Chose", second)
            print("It's a tie.")
            
        elif userHand == "Rock":
            if computerHand == "Scissors":
                print("You Chose", first)
                print("Computer Chose", second)
                print("You Win!")
            else:
                print("You Chose", first)
                print("Computer Chose", second)
                print("You Lose!")
                
        elif userHand == "Paper":
            if computerHand == "Rock":
                print("You Chose", first)
                print("Computer Chose", second)
                print("You Win!")
            else:
                print("You Chose", first)
                print("Computer Chose", second)
                print("You Lose!")
                
        elif userHand == "Scissors":
            if computerHand == "Paper":
                print("You Chose", first)
                print("Computer Chose", second)
                print("You Win!")
            else:
                print("You Chose", first)
                print("Computer Chose", second)
                print("You Lose!")

        else:
            print("Please enter either Rock, Paper or Scissors")

    game(userHand, computerHand)
