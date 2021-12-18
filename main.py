import random

while True:
    choices = ["rock", "paper", "scissors"]

    player1 = None
    player2 = None

    while player1 and player2 not in choices:
        player1 = input("rock, paper, or scissors?: ").lower()
        player2 = input("rock, paper, or scissors?: ").lower()

    if player1 == player2:
        print("compute chose: ", player2)
        print("You chose: ", player)
        print("It's a tie!")

    elif player1 == choices[0]:
        if player2 == choices[1]:
            print("computer chose: ", player2)
            print("You chose: ", player)
            print("You lose!")

        if computer == choices[2]:
            print("computer chose: ", player2)
            print("You chose: ", player)
            print("You Win!")
    elif player == choices[1]:
        if computer == choices[0]:
            print("computer chose: ", player2)
            print("You chose: ", player)
            print("You Win!")

        if computer == choices[2]:
            print("computer chose: ", player2)
            print("You chose: ", player)
            print("You lose!")

    elif player == choices[2]:
        if computer == choices[0]:
            print("computer chose: ", player2)
            print("You chose: ", player)
            print("You Lose!")

        if computer == choices[1]:
            print("computer chose: ", player2)
            print("You chose: ", player)
            print("You lose!")

    playAgain = input("Would you like to play again? (yes/no) ").lower()

    if playAgain == "yes":
        continue

    elif playAgain == "no":
        break
    else:
        playAgain = input("Would you like to play again? (yes/no) ").lower()

print("Thanks for playing!")