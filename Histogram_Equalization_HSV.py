# IMAGE ENHANCEMENT USING HISTOGRAM EQUALIZATION OF VALUE IN HSV COLOR SPACE

"""
    Created by Sang Kim date 05/31/2020
    Email: sangkimit@gmail.com
"""

#import numpy as np 
import cv2
#import matplotlib.pyplot as plt 


im = cv2.imread("airblade.jpeg")

#(b, r, g) = cv2.split(im)

im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

(h, s, v) = cv2.split(im_hsv)

#hist = cv2.calcHist([v], [0], None, [256], [0, 256])

equ = cv2.equalizeHist(v)

hsv_equ = cv2.merge((h, s, equ))

img_output = cv2.cvtColor(hsv_equ, cv2.COLOR_HSV2BGR)

cv2.imshow("View",img_output)
cv2.imwrite("airblade_equalization.jpg", img_output)

cv2.waitKey()
cv2.destroyAllWindows()