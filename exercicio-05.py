import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt


img = io.imread('https://cbissn.ibict.br/images/phocagallery/galeria2/thumbs/phoca_thumb_l_image03_grd.png')


img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


_, binary_img = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


img_with_contours = cv2.drawContours(img.copy(), contours, -1, (0, 255, 0), 3)

plt.imshow(cv2.cvtColor(img_with_contours, cv2.COLOR_BGR2RGB))
plt.show()