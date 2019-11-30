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


# class image:
#     def __init__(self):
#         self.capture=cv2.VideoCapture(0)
#
#     def __str__(self):
#         return "{0}".format(self.capture)
#     def take_image(self):
#         while True:
#             (self.returned, self.frame) = self.capture.read()
#             key = cv2.waitKey(1)
#
#             self.gray_representation = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
#             # denoised_representation=cv2.fastNlMeansDenoisingColored(capture,None,20,10,7,21)
#             cv2.imshow('frame', self.gray_representation)
#             if key & 0xFF == ord("s"):
#                 self.captured_choice = cv2.imwrite("captured_image.jpg", self.gray_representation)
#
#             elif key & 0xFF == ord("q"):
#                 break
#         cv2.destroyAllWindows()
#         self.capture.release()


class choice:
    """
    Make player and computer choices
    """

    def __init__(self):
        self.player_choice = cv2.VideoCapture(0)
        self.computer_choice = 0

    def __str__(self):
        return "{0},{1}".format(self.player_choice, self.computer_choice)

    def take_player_choice(self):
        """
        Launch webcam to take the player's choice
        :return: the gray scale representation of the image captured
        """
        while True:
            (self.returned, self.frame) = self.player_choice.read()
            key = cv2.waitKey(1)

            self.gray_representation = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', self.gray_representation)
            self.blur_img = cv2.medianBlur(self.gray_representation, 5)
            self.th_img = cv2.adaptiveThreshold(self.blur_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 11, 2)

            if key & 0xFF == ord("s"):
                self.captured_choice = cv2.imwrite("captured_image.jpg", self.th_img)
                break

            elif key & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()
        self.player_choice.release()

    def identify_player_choice(self):
        (self.returned_th,self.th)=cv2.threshold(self.gray_representation,127,255,0)
        (self.contours,self.hierarchy)=cv2.findContours(self.th,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        self.contour_img=cv2.drawContours(self.gray_representation,self.contours,-1,(0,255,0),3)
        self.captured_contours=cv2.imwrite("captured_contours.jpg",self.contour_img)


    def take_computer_choice(self):
        """
        Makes a random choice for the computer
        :return: the computer's random choice
        """
        options = ["rock", "paper", "scissors", "spock", "lizard"]
        computer_choice = random.choice(options)
        return computer_choice

# if __name__ == "__main__":
#     main()
# choice1 = choice()
# choice1.take_player_choice()
# # print(choice1.take_computer_choice())
