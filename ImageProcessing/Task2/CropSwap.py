# 📌 Take 2 images, crop some part of both the images and swap them.

import cv2
import numpy as np

#loading image 1
photo = cv2.imread('white.jpg')

#loading image 2
pic = cv2.imread('violet.jpg')

# Displaying both images
cv2.imshow('pic1',photo)
cv2.imshow('pic2',pic)
cv2.waitKey()
cv2.destroyAllWindows()

#Cropping some part of both images
x = photo[70:280, 200:450]
y = pic[50:260, 210:460]

#Displaying cropped portion
cv2.imshow('crop_pic1',x)
cv2.imshow('crop_pic2',y)
cv2.waitKey()
cv2.destroyAllWindows()


photo = cv2.imread('white.jpg')
pic = cv2.imread('violet.jpg')

#Swapping the images
photo[70:280, 200:450] = y
pic[50:260, 210:460] = x
cv2.imshow('swap_pic1',photo)
cv2.imshow('swap_pic2',pic)
cv2.waitKey()
cv2.destroyAllWindows()
