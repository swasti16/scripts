"""Image Processing using NumPy.

Converting a coloured image into grayscale.
"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm

image = misc.imread('flower.jpg')
# print image
print image.shape
"""
This has a height of 480 pixels and a width of 640 pixels.
Its stored in a 3D numpy array.
The 3rd number indicates that this is an RGB image.
A (row,column) index into this 3D matrix will give you 3 values : [R,G,B].
"""
print image[0, 0]
"""
This prints the first pixel.
The intensity of red is 32, green is 24 and blue is 21!
"""
# plt.imshow(image)
# plt.show()


"""Exploring two ways to find grayscale.

1. Simple Average
2. Weighted average
Change the function name in line 49 to check the result of that function.
"""


def simple_average(pixel):
    """G = (R+G+B) / 3."""
    return np.average(pixel)


def weighted_average(pixel):
    """G = R*0.299 + G*0.587 + B*0.114."""
    return 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]

"""Creating an array of size 480x640"""
grey = np.zeros((image.shape[0], image.shape[1]))

"""Averaging every element of the image"""
for rownum in range(len(image)):
    for colnum in range(len(image[rownum])):
        grey[rownum][colnum] = weighted_average(image[rownum][colnum])
print grey.shape

"""Plotting both, orignal and the final image and saving the final image"""
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1 = plt.imshow(image)
ax2 = fig.add_subplot(2, 1, 2)
ax2 = plt.imshow(grey, cmap=matplotlib.cm.Greys_r)
plt.show()
misc.imsave('flower-gray.jpg', grey)
