#################################################################################
# Author(s): Concepta Njolima
# Username(s): njolimac
#
# Assignment: A07 Rock paper scissors lizard spock
# Purpose: To create a game that plays a different version of rock paper scissor.
#################################################################################
# Acknowledgements:
# Dr. Scott Heggen
# Audrey M. Craft
# William J.Romano
#################################################################################
#################################################################################
from tkinter import *
from choice import Choice
import PIL.Image, PIL.ImageTk
from take_player_choice import identify_finger
import time


class Ui:
    """
    Create a new UI for the game
    """

    def __init__(self):
        """
        Initialize a new UI with a background image and
        """
        self.root = None
        self.init_window()
        self.new_choice = Choice()
        self.set_background()      # To set the background image in place
        self.count = 0

    def init_window(self):
        """
        This function enables creating of new windows everytime we click a button
        :return: None
        """
        if self.root:  # If there is a root
            self.root.destroy()  # Destroy the root
        self.root = Tk()  # Makes a new root
        self.root.geometry("1800x1800")
        self.root.title("Rock,Paper,Scissors, Spock,Lizard")
        self.player_frame = Frame(self.root, padx=100, pady=200, background="orange")
        self.player_frame.place(x=300, y=100)
        self.computer_frame = Frame(self.root, padx=100, pady=200, background="light blue")
        self.computer_frame.place(x=800, y=100)
        self.entered_name = False

        self.compScoreLabelText = StringVar()  # Makes a Tkinter string variable
        self.playerScoreLabelText = StringVar()  # Makes a Tkinter string variable
        self.compChoiceLabelText = StringVar()  # Makes a Tkinter string variable
        self.playerChoiceLabelText = StringVar()  # Makes a Tkinter string variable
        self.displayed_player_score = StringVar()
        self.displayed_computer_score = StringVar()
        self.winnerName = StringVar()  # Makes a Tkinter string variable
        self.another_choice_button = Button(self.root, text="Make another choice", height=5, width=18,
                                            background="light green", command=self.play_again)
        self.quit_match = Button(self.root, text="QUIT MATCH", height=5, width=15, background="tomato",
                                 command=self.quit_game)
        self.quit_match.place(x=675, y=600)
    def set_background(self):
        """
        This function creates a canvas for the background image
        :return: None
        """
        self.project_image_canvas = Canvas(self.root, height=1500, width=1800)
        self.background = PhotoImage(file="image/background.png")
        self.project_image_canvas.create_image(700, 450, image=self.background)
        self.project_image_canvas.pack()

    def start_game(self):
        """
        This function enables the start of the game by displaying the title,
        then calls the make choice  and display_updated_choice functions
        :return: None
        """


        self.init_window()
        self.make_choice()
        self.display_updated_choice()

        self.another_choice_button.place(x=670, y=300)

    def user_guide(self):
        """
        This functions gives instructions to the user on how to play the game
        :return: None
        """
        self.init_window()
        self.general_instruction = Label(self.root, text="""***HOW TO PLAY***\n
        1.When you hit the start Game Button, your web cam is launched\n 
        2.Ensure to position fingers according a symbol(shown below) that represents your choice \n
        3. Then click "s" on your keyboard to save the choice made!
          The rock,paper, scissors,lizard, and spock representations are as shown below\n
        **The winner of the match is announced after five choices are made**""", pady=50)
        self.general_instruction.config(font=("Helvetica", 18))
        self.general_instruction.pack()
        self.background_canvas = Canvas(self.root, height=1800, width=1800, background=None)
        self.rock_image = PhotoImage(file="image/rock.png")
        self.background_canvas.create_image(290, 90, image=self.rock_image)
        self.paper_image = PhotoImage(file="image/paper.png")
        self.background_canvas.create_image(520, 90, image=self.paper_image)
        self.scissors_image = PhotoImage(file="image/scissors.png", )
        self.background_canvas.create_image(750, 90, image=self.scissors_image)
        self.lizard_image = PhotoImage(file="image/lizard.png")
        self.background_canvas.create_image(1135, 90, image=self.lizard_image)
        self.spock_image = PhotoImage(file="image/spock.png")
        self.background_canvas.create_image(975, 90, image=self.spock_image)

        self.back_button = Button(self.background_canvas, text="BACK", height=5, width=15, background="tomato",command=self.back_button_handler)
        self.background_canvas.create_window(750, 260, window=self.back_button)
        # self.back_button.place(x=1200, y=300)
        self.background_canvas.pack()

    def back_button_handler(self):
        """
        This is the button handler for the back button after reading the instructions on how to play the game
        :return: None
        """
        self.init_window()
        self.set_background()
        self.create_welcome_window()

    def make_choice(self):
        """
        This function manages the players choice
        Creates a player board
        Calls the identify_player_choice function to identify what choice the user makes
        It displays the player's choice and score
        :return: None
        """
        # To take in and identify the player's choice from the webcam'
        self.new_choice.identify_player_choice()
        # Make a computer choice
        self.new_choice.take_computer_choice()
        # Compare these choices
        self.new_choice.compare_choices()
        # Set the choices to variables
        self.displayed_player_score = self.new_choice.player_score
        self.displayed_computer_choice = self.new_choice.computer_choice

    def display_updated_choice(self):
        """
        This function managaes the computer score board
        It enables the computer to make a random choice
        It displays the choice and score of the computer
        :return:None
        """
        self.count += 1
        print("count{0}".format(self.count))
        # Set the player label, with font
        self.player_choiceBoard = Label(self.player_frame, text="PLAYER")
        self.player_choiceBoard.config(font=("Helvetica", 18))
        self.player_choiceBoard.pack()
        # Add a separator with height 2
        self.player_space_up = Label(self.player_frame, text="", background="orange", height=2)
        self.player_space_up.pack()
        # Make a player choice label
        self.displayed_player_choice = self.new_choice.player_choice
        self.player_choiceBoard = Label(self.player_frame, text="Choice: ")
        self.player_choiceBoard.pack(side=LEFT)
        # Show the displayed choice
        self.playerChoiceLabelText.set(self.displayed_player_choice)
        self.player_choice_Label = Label(self.player_frame, textvariable=self.playerChoiceLabelText)
        self.player_choice_Label.pack(side=LEFT)
        # Separate the choice label and the choice value
        self.player_space = Label(self.player_frame, text="", background="orange", width=5)
        self.player_space.pack(side=LEFT)

        # Player score gets updated
        self.player_scoreBoard = Label(self.player_frame, text="Score: ")
        self.player_scoreBoard.pack(side=LEFT)
        self.displayed_player_score = self.new_choice.player_score
        self.playerScoreLabelText.set(self.displayed_player_score)
        self.player_score_Label = Label(self.player_frame, textvariable=self.playerScoreLabelText)
        self.player_score_Label.pack(side=LEFT)  # pack means add to window
        # make a computer choice label
        self.computer_choiceBoard = Label(self.computer_frame, text="COMPUTER")
        self.computer_choiceBoard.config(font=("Helvetica", 18))
        self.computer_choiceBoard.pack()
        # To add a separator with height of 2
        self.computer_space_up = Label(self.computer_frame, text="", background="light blue", height=2)
        self.computer_space_up.pack()
        self.comp_choiceBoard = Label(self.computer_frame, text="Choice:")
        # Make a choice board for the computer choice
        self.displayed_computer_choice = self.new_choice.computer_choice
        self.comp_choiceBoard.pack(side=LEFT)
        self.compChoiceLabelText.set(self.displayed_computer_choice)
        # Add the choice label for the computer choice
        self.comp_choice_Label = Label(self.computer_frame, textvariable=self.compChoiceLabelText)
        self.comp_choice_Label.pack(side=LEFT)  # pack means add to window
        # To add a separator between choice and score
        self.comp_space = Label(self.computer_frame, text="", background="light blue", width=5)
        self.comp_space.pack(side=LEFT)
        # The computer score board display
        self.comp_scoreBoard = Label(self.computer_frame, text="Score: ")
        self.comp_scoreBoard.pack(side=LEFT)
        self.displayed_computer_score = self.new_choice.computer_score
        self.compScoreLabelText.set(self.displayed_computer_score)
        self.comp_score_Label = Label(self.computer_frame, textvariable=self.compScoreLabelText)
        self.comp_score_Label.pack()
        self.comp_score_Label.pack(side=LEFT)

        # If the player and computer have made three choices, then declare a winner and restart another match
        if self.count == 5:
            self.display_winner()
            self.new_choice.player_score = 0
            self.new_choice.computer_score = 0

    def play_again(self):
        """
        This function is to enable continuous playing
        It is called when the user clicks the make another choice button
        :return: None
        """
        self.init_window()
        self.make_choice()
        self.display_updated_choice()
        self.another_choice_button.place(x=670, y=300)
        self.quit_Button.pack()
    def restart_game(self):
        """
        This function enables the player to restart the game after displaying the winner
        It enables another round of five choices to be made
        :return: None
        """
        self.init_window()
        self.make_choice()
        self.display_updated_choice()
        self.another_choice_button.place(x=670, y=300)
    def set_winner_screen(self):
        """
        This function creates the screen on which the winner of the game is displayed
        :return: None
        """
        self.project_image_canvas = Canvas(self.root, height=1500, width=1800)
        self.background = PhotoImage(file="background.png")
        self.project_image_canvas.create_image(700, 450, image=self.background)
        self.project_image_canvas.pack()
    def display_winner(self):
        """
        This function prints who has won the game
        :return:Nones
        """
        self.set_background()
        self.count=0
        self.play_again_button=Button(self.root,text="PLAY AGAIN",height=5, width=15, background="light green",command=self.restart_game)
        self.play_again_button.place(x=200,y=50)
        # If the computer score is higher than the player score
        if self.displayed_computer_score > self.displayed_player_score:
            comp_win_label = Label(self.root, text="Computer wins", foreground="blue")
            comp_win_label.config(font=("Helvetica", 50))
            comp_win_label.place(x=550, y=40)
        # If the player score is higher than the computer score
        elif self.displayed_computer_score < self.displayed_player_score:
            player_win_label = Label(self.root, text="Player wins", foreground="orange")
            player_win_label.config(font=("Helvetica", 50))
            player_win_label.place(x=550, y=40)
        # If both scores are equal
        elif self.displayed_computer_score == self.displayed_player_score:
            draw_label = Label(self.root, text="Equal scores. This is a draw", foreground="red")
            draw_label.config(font=("Helvetica", 50))
            draw_label.place(x=400, y=40)


    def quit_game(self):
        """
        This function is a handler for the quit game button
        :return: None
        """
        self.root.destroy()

    def create_welcome_window(self):
        """
        This function creates the UI for the welcome screen
        :return: None
        """
        # The game title
        self.game_title = Label(self.root, text="ROCK,PAPER,SCISSORS,LIZARD, SPOCK", foreground="blue")
        self.game_title.config(font=("Courier", 40))
        # The mini instructions on how to navigate the welcome
        self.instruction = Label(self.root,
                                 text="Click Start to take your first choice, or Quit to exit the game.\n Click How to play for instructions on how to play the game")
        self.instruction.config(font=("Courier", 15))
        self.game_title.place(x=100, y=100)
        self.instruction.place(x=250, y=200)
        self.quit_match.destroy()
        # Craete the buttons on the welcome screen
        self.play_Button = Button(self.root, text="START GAME", height=5, width=15, background="light green",
                                  command=self.start_game, )
        self.quit_Button = Button(self.root, text="QUIT GAME", height=5, width=15, background="tomato",
                                  command=self.quit_game)
        self.user_guide_Button = Button(self.root, text="HOW TO PLAY", height=5, width=15, background="yellow",
                                        command=self.user_guide)
        self.play_Button.place(x=400, y=400)
        self.quit_Button.place(x=900, y=400)
        self.user_guide_Button.place(x=650, y=500)
        self.root.mainloop()


def main():
    """
    This is where the running of the program begins from.
    :return: None
    """
    # Create a game UI win=th a welcome window
    gameui = Ui()
    gameui.create_welcome_window()

    while True:
        gameui.start_game()


if __name__ == "__main__":
    main()
