import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt

print("OpenCV-Python Version {}".format(cv2.__version__))

image = io.imread('https://farrokhkarimi.github.io/images/gallery/modals/ice-m.jpg')
io.imsave('image.png', image)
image = cv2.imread('image.png')

plt.imshow(image)
plt.show()