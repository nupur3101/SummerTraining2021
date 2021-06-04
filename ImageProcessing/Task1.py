# 📌 Create image by yourself Using Python Code

import cv2
import numpy as np

# Creating a 3D array with all elements 0 (black)
b = np.zeros((900,900,3))

# Creating circle for face
bCircle=cv2.circle(b, (450,450), 250, [0,255,255], -1)

# drawing eyes
eye1=cv2.circle(b, (360,370), 50, [0,0,0],-1)
eye2=cv2.circle(b, (520,370), 50, [0,0,0],-1)
iris1=cv2.circle(b, (360,390), 15, [1,1,1],-1)
iris2=cv2.circle(b, (520,390), 15, [1,1,1],-1)

# Drawing mouth
line = cv2.line(b, (360,530), (520,530), [0,0,0], 5)
t1 = cv2.rectangle(b, (400,535), (440,570), [1,1,1], -1)
t2 = cv2.rectangle(b, (445,535), (485,570), [1,1,1], -1)

# Displaying complete image
cv2.imshow('pic2',bCircle)
cv2.waitKey()
cv2.destroyAllWindows()
