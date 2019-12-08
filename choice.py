#################################################################################
# Author(s): Concepta Njolima
# Username(s): njolimac
#
# Assignment: A07 Rock paper scissors lizard spock
# Purpose: To create a game that plays a different version of rock paper scissor.
#################################################################################
# Acknowledgements:
#
#
#################################################################################
#################################################################################
import cv2
import random
from take_player_choice import identify_finger

class Choice:
    """
    Make player and computer choices
    """

    def __init__(self):
        self.player_choice = 0
        self.computer_choice = 0
        self.computer_score = 0
        self.player_score = 0
        self.count = 0

    def __str__(self):
        return "{0},{1}".format(self.player_choice, self.computer_choice)

    def identify_player_choice(self):
        """
        This function uses the identify_finger class in take_player_choice file to tell what finger is chosen
        :return: self.player_choice: the player's choice
        """
        self.player_input = identify_finger()
        self.player_choice = self.player_input.tell_finger()
        print(self.player_choice)
        return self.player_choice

    def take_computer_choice(self):
        """
        Makes a random choice for the computer
        :return: self.computer choice: the computer's random choice
        """
        options = ["rock", "lizard", "scissors", "spock", "paper"]
        self.computer_choice = random.choice(options)
        print(self.computer_choice)
        return self.computer_choice

    def compare_choices(self):
        """
        Compares computer choice and player choice and adds points to the winner
        It does not add any points when the choices are the same
        :return: None
        """

        choices = ["rock", "lizard", "scissors", "spock", "paper"]
        if self.computer_choice == self.player_choice:
            self.computer_score += 0
            self.player_score += 0
            print(self.computer_score, self.player_score)
        elif self.player_choice == "rock":
            if self.computer_choice == choices[1] or self.computer_choice == choices[2]:
                self.player_score += 1
                print(self.computer_score, self.player_score)
            elif self.computer_choice == choices[3] or self.computer_choice == choices[4]:
                self.computer_score += 1
                print(self.computer_score, self.player_score)
        elif self.player_choice == "lizard":
            if self.computer_choice == choices[3] or self.computer_choice == choices[4]:
                self.player_score += 1
                print(self.computer_score, self.player_score)
            elif self.computer_choice == choices[0] or self.computer_choice == choices[2]:
                self.computer_score += 1
        elif self.player_choice == "scissors":

            if self.computer_choice == choices[4] or self.computer_choice == choices[1]:
                self.player_score += 1
                print(self.computer_score, self.player_score)
            elif self.computer_choice == choices[0] or self.computer_choice == choices[3]:
                self.computer_score += 1
                print(self.computer_score, self.player_score)
        elif self.player_choice == "spock":

            if self.computer_choice == choices[2] or self.computer_choice == choices[0]:
                self.player_score += 1
                print(self.computer_score, self.player_score)
            elif self.computer_choice == choices[1] or self.computer_choice == choices[4]:
                self.computer_score += 1
                print(self.computer_score, self.player_score)
        elif self.player_choice == "paper":
            if self.computer_choice == choices[0] or self.computer_choice == choices[3]:
                self.player_score += 1
                print(self.computer_score, self.player_score)
            elif self.computer_choice == choices[1] or self.computer_choice == choices[2]:
                self.computer_score += 1
                print(self.computer_score, self.player_score)

# if __name__ == "__main__":
#     main()
# choice1 = Choice()
# choice1.repeat_choices()
