import random

choices = ['Rock', 'Paper', 'Scissors']

computer = random.choice(choices)

player = None 

while player not in choices:

    player = input("Rock, paper or scissors? ").capitalize()

    if player == computer:
        print("You chose: {}".format(player))
        print("The computer chose: {}".format(computer))
        print("Tie!")
    elif player == 'Rock':
        if computer == 'Scissors':
            print("You chose: {}".format(player))
            print("The computer chose: {}".format(computer))
            print("You won!")
        if computer == 'Paper':
            print("You chose: {}".format(player))
            print("The computer chose: {}".format(computer))
            print("You lose!")

    elif player == 'Paper':
        if computer == 'Rock':
            print("You chose: {}".format(player))
            print("The computer chose: {}".format(computer))
            print("You won!")
        if computer == 'Scissors':
            print("You chose: {}".format(player))
            print("The computer chose: {}".format(computer))
            print("You lose!")
 
    elif player == 'Scissors':
        if computer == 'Paper':
            print("You chose: {}".format(player))
            print("The computer chose: {}".format(computer))
            print("You won!")
        if computer == 'Rock':
            print("You chose: {}".format(player))
            print("The computer chose: {}".format(computer))
            print("You lose!")

