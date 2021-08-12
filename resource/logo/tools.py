import os
import cv2
import numpy as np

print(os.getcwd())
img = cv2.imread("V5++_logo.jpg")

b_,g_,r_ = cv2.split(img)
a_ = np.ones(b_.shape,dtype=b_.dtype)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        a_[i][j] = 255
        if b_[i][j] > 220 and g_[i][j] > 220 and r_[i][j] >220:
            a_[i][j] = 0

result = cv2.merge((b_,g_,r_,a_))

cv2.imshow("show",result)
cv2.imwrite('V5++-logo-alpha.png',result)
cv2.waitKey(0)

