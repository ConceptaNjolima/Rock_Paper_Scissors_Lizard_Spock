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
import tkinter as tk
import choice


class game:
    """
    Create a new game
    """

    def __init__(self, windowtext="Rock it, Paper the rock,scissor the paper"):
        self.start = False
        self.score = 0
        self.root = tk.Tk()  # Create the root window where all widgets go
        self.root.minsize(width=250, height=100)  # Sets the window's minimum size
        self.root.maxsize(width=250, height=100)  # Sets the window's maximum size
        self.root.title(windowtext)  # Sets root window title
        self.rockButton = None
        self.myTextLabel1Text = tk.StringVar()  # Makes a Tkinter string variable
        self.myTextLabel1 = None

    def __str__(self):
        """
        This function over rides the built-in string method
        :return: string
        """
        return "{0},{1}".format(self.start, self.score)

    def create_player_choice_button(self, buttontext="Choose option"):
        """
        Creates a button with the given buttontext

        :param buttontext: The text on the button
        :return: None
        """
        self.player_choice_Button = tk.Button(self.root, text=buttontext, command=self.player_choice_button_handler)
        # when player_choice_Button is pushed, self.player_choice_button_handler is called
        self.player_choice_Button.pack()  # pack means add to window

    def player_choice_button_handler(self):
        """
        Handler for player_choice_button
        Calls methods in choice class
        :return: None
        """
        player_choice = choice.choice()
        player_choice.take_player_choice()
        player_choice.identify_player_choice()


def main():
    """
    The game begins here
    :return: None
    """
    new_game = game()
    new_game.create_player_choice_button()
    new_game.root.mainloop()  # Needed to start the event loop


if __name__ == "__main__":
    main()
