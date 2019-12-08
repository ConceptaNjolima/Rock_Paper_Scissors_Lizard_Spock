# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:55:25 2018
@author: Sourav
https://github.com/srvindian/handgesture_fingers_count
edited by:
Concepta Njolima
"""

import cv2
import numpy as np
import PIL.Image, PIL.ImageTk
class identify_finger:
    def __init__(self):
        """
        The function initiazes opens the cascade Classifier, the video capture and scaling factor to be used in resizing
        """
        self.cascade = cv2.CascadeClassifier('fingertip_cascade.xml')
        self.cap = cv2.VideoCapture(0)
        self.scaling_factor = 1
        (self.ret,self.frame)=(None,None)

    def __str__(self):
        """
        This function over writes the built in string method
        :return: a string of the attributes
        """
        return "{0},{1}".format(self.cascade,self.scaling_factor)
    def tell_finger(self):
        """
        This function identifies fingers raised using the fingertip_cascade.xml
        Draws a rectangle around the fingertip
        :return: None
        """
        while True:
            # Stores read video in the frame variable
            (self.ret, self.frame) = self.cap.read()
            # Keeps the video running until a key is pressed
            self.key = cv2.waitKey(1)
            # To resize the captured video fram
            self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor, interpolation=cv2.INTER_AREA)
            self.frame = cv2.flip(self.frame, 2)
            # To convert the image to Gray scale
            self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            # To draw rectangles around the detected finger tips, a variable rects is declared for those rectangles
            rects = self.cascade.detectMultiScale(self.gray, 1.2, 20)
            self.n = 0
            # A list of the game options;rock,paper,scissors,lizard,spock
            self.items=["rock","lizard","scissors","spock","paper"]
            for (x, y, w, h) in rects:
                # draw the rectangles around the finger tips
                cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.n += 1
                # To write the text of what game option was chosen
                cv2.putText(self.frame, str(self.n), (x + np.uint8(w / 2) - 8, y + np.uint8(h / 2) + 5), cv2.FONT_HERSHEY_SIMPLEX, .8,
                            (255, 0, 0), 2)
                cv2.circle(self.frame, (x + np.uint8(w / 2), y + np.uint8(h / 2)), 2, (0, 0, 255), -1)

            # print(self.n)
            # To show the game option corresponding to the finger tips indentified
            for number_of_tips in range(len(self.items)):
                if self.n<5:
                    cv2.putText(self.frame, self.items[self.n], (10, 450), cv2.FONT_HERSHEY_SIMPLEX,5, (200, 255, 120),2)
                    cv2.imshow('Video Feed', self.frame)

            if self.key & 0xFF == ord("s"): # if key s is clicked, save the choice made and destroy all video capturing windows
                self.captured_choice = self.items[self.n]
                self.cap.release()
                cv2.destroyAllWindows()
                return self.captured_choice
            if self.key & 0xFF==ord("q"): # if key q is clicked, quit the video capturing window
                cv2.destroyAllWindows()
                self.cap.release()
                break



