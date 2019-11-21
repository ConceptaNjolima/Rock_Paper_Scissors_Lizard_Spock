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
import tkinter,turtle
import cv2
image = cv2.imread("picture.jpg", 0)
cv2.imshow('wn',image)
key=cv2.waitKey(0)
capture=cv2.VideoCapture(0)

while True:
    (returned,frame) = capture.read()
    key = cv2.waitKey(1)
    gray_representation=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray_representation)
    if key& 0xFF==ord("q"):
        break
cv2.destroyAllWindows()
capture.release()
