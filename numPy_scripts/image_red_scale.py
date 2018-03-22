"""Image Processing using NumPy.

Converting a coloured image into red,blue,or green channels.
put 0 for red channel, 1 for green channel and 2 for blue channel in line 16
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt


image = misc.imread('flower.jpg')


""" Crearting a new zero martix of same size as that of image.
Using slicing of array we are getting r,g,b channel
"""
image_new = np.zeros_like(image)
image_new[:, :, 1] = image[:, :, 1]


"""Saving the final image, and then plotting them"""
misc.imsave('flower-new.jpg', image_new)
image_new = misc.imread('flower-new.jpg')
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1 = plt.imshow(image)
ax2 = fig.add_subplot(2, 1, 2)
ax2 = plt.imshow(image_new)
plt.show()
