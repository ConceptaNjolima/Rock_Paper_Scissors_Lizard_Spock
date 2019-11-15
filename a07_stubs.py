#################################################################################
# Author(s): Concepta Njolima, Immanuela Belaineh
# Username(s): belainehi, njolimac
#
# Assignment: A07 Rock paper scissors lizard spock
# Purpose: To create a game that plays a different version of rock paper scissor.
#################################################################################
# Acknowledgements:
# Liberty Mupotsa
#
#################################################################################
#################################################################################
import random

computer_score = 0
user_score = 0
rounds = 0


def player_choice(start):
    """
    This function asks the user to choose between rock,paper,scissor,lizard, or spock
    return: choice:The choice made by the player
    """
    trials = 1
    while start:
        while trials < 6:
            # print(trials)
            # prompt the player to input their choice
            choice = input(str(
                "So, what do you choose(lower case letters only)? s for spock? l for lizard? r for rock? p for paper? sc for scissor?"))
            if choice == "s" or choice == "l" or choice == "r" or choice == "p" or choice == "sc":
                # if choice is the expected then return choice
                choice_made = True
                print(choice)
                return choice
            else:
                # if an unexpected choice is entered
                choice_made = False
                print("only s,p,l,r, or sc are expected")
                print("You have {0} entry(s) out of the 5 permitted wrong entries".format(trials))
                trials += 1
        break
    pass


def begin_game():
    """
    This function provides a user to begin or not begin the game
    :return: begin: True if the user chooses y or False if the user uses n
    """
    begin = False
    wrong_trials = 1
    while not begin:
        # To limit the wrong trials to 6
        while wrong_trials < 6:
            print("Rock!Paper!Scissor!Spock!Lizard")
            # Ask the user to choose y to begin the game or n to not begin the game
            user_begin = str(input("Enter y to start a New game or n to Close the game"))
            if user_begin == "y":
                begin = True
                return begin
            elif user_begin == "n":
                begin = False
                return begin
            else:
                print("Wrong choice entered")
                print("You have used up {0} entries out of the 5 permitted wrong entries".format(wrong_trials))
                wrong_trials += 1
        break


def comparison(playerchoice, computerchoice):
    """
    Docstring for function_1
    This function compares the player's and computer's choice to show who has won this particular game.
    :param playerchoice: It is returned from the player_choice function.
    :param computerchoice: It is returned from the computer_choice function.
    :return: computernumber, playernumber
    """
    global computer_score
    global user_score

    # We compare the computer's choice and the player's choice then award points according to the rules of rock-paper-spock-scissor-lizard
    if playerchoice == computerchoice:
        print("the computer's choice was {0} and Paper covers rock".format(computerchoice))
        print("Your choice is similar to the computers")
        print("Your score is:", user_score, "Computer's score is:", computer_score)
    elif playerchoice == "r":
        if computerchoice == "p":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Paper covers rock".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)
        if computerchoice == "sc":
            user_score += user_score
            print("the computer's choice was {0} and Rock crushes scissors".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)
        if computerchoice == "l":
            user_score = user_score + 1
            print("the computer's choice was {0} and Rock crushes lizard".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "s":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Spock vaporizes rock ".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

    elif playerchoice == "p":
        if computerchoice == "r":
            user_score = user_score + 1
            print("the computer's choice was {0} and paper covers rock".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "sc":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and scissors cut paper ".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)
        if computerchoice == "l":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Lizard eats paper".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "s":
            user_score = user_score + 1
            print("the computer's choice was {0} and Paper disproves spock".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

    elif playerchoice == "sc":
        if computerchoice == "r":
            user_score = user_score + 1
            print("the computer's choice was {0} and Rock crushes scissors".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "p":
            user_score = user_score + 1
            print("the computer's choice was {0} and Scissors cut paper".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "l":
            user_score = user_score + 1
            print("the computer's choice was {0} and Scissors decapitate Lizard ".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "s":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Spock smashes scissors".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)
    elif playerchoice == "l":
        if computerchoice == "r":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Rock crushes lizard".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "p":
            user_score = user_score + 1
            print("the computer's choice was {0} and Lizard eats paper".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "sc":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Scissors decapitate Lizard".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "s":
            user_score = user_score + 1
            print("the computer's choice was {0} and Lizard poisons Spock".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

    elif playerchoice == "s":
        if computerchoice == "r":
            user_score = user_score + 1
            print("the computer's choice was {0} and Spock vaporizes Rock".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "p":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Paper disproves Spock ".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "sc":
            user_score = user_score + 1
            print("the computer's choice was {0} and Spock smashes Scissors ".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)

        if computerchoice == "l":
            computer_score = computer_score + 1
            print("the computer's choice was {0} and Lizard poisons Spock".format(computerchoice))
            print("Your score is:", user_score, "Computer's score is:", computer_score)


def computer_choice():
    """
    Docstring for function_2
    This function let's the computer generate a random choice from "rock","paper","scissor","lizard" and"spock".
    :return: Computer's choice
    """
    options = ["r", "p", "sc", "l", "s"]
    # To randomly select from the options list
    computer_random = random.choice(options)
    # print(computer_random)
    return computer_random


def main():
    """
    This is where the whole function comes together.
    :return: None
    """
    global rounds
    start_game = begin_game()
    if start_game:
        while rounds < 5:
            choice_computer = computer_choice()  # Function call to computer_choice
            choice_player = player_choice(start_game)
            comparison(choice_player, choice_computer)
            rounds += 1
            # print(rounds)
            # To limit the number of rounds for each play session to 5
            if rounds == 5:
                if computer_score > user_score:
                    print("Computer wins!!!")
                elif user_score > computer_score:
                    print("User wins!!!")
                elif user_score == computer_score:
                    print("You draw!!!This deserves a new game!")
    elif not start_game:
        print("Game closed")
        pass


main()
