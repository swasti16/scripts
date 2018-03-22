import numpy as np
import cv2

# Load an color image in grayscale

# img = cv2.imread('flower.jpg', 0)
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.imwrite('flowergray.png', img)
# print img
# print type(img), img.shape

# img = cv2.imread('flower.jpg')
# px = img[100, 100]
# print px
# blue = img[100,100,0]
# print blue
# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.imwrite('flowermodified.png', img)


img = cv2.imread('rose.jpg')
px = img[100, 100]
print px
blue = img[100,100,0]
print blue

