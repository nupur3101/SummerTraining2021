# 📌 Take 2 images and combine them to form a single image. For example, collage 

import cv2
import numpy as np

# Loading 2 images
p1 = cv2.imread('puzzleL.jpg')
p2 = cv2.imread('puzzleR.jpg')

# displaying images
cv2.imshow('p1',p1)
cv2.imshow('p2',p2)
cv2.waitKey()
cv2.destroyAllWindows()

# combining the images using numpy array horizontal stack function
cv2.imshow('pic2',np.hstack((p1,p2[0:477,:])))
cv2.waitKey()
cv2.destroyAllWindows()
