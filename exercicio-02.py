import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt

# Perspective Transformation
img = io.imread('https://cbissn.ibict.br/images/phocagallery/galeria2/thumbs/phoca_thumb_l_image03_grd.png')
rows,cols,ch = img.shape
pts1 = np.float32([[73,86],[489,69],[36,514],[520,522]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(img2),plt.title('Output')
plt.show()