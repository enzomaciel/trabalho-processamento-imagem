import numpy as np
import cv2
from skimage import io
import matplotlib.pyplot as plt

image = io.imread('https://farrokhkarimi.github.io/images/gallery/modals/ice-m.jpg')
io.imsave('image.png', image)
imagem = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)

# Aplicar o operador de Sobel para detecção de bordas
sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=5)

# Combine as respostas em x e y para obter as bordas
bordas = np.sqrt(sobel_x**2 + sobel_y**2)

# Normalização para exibição
bordas = cv2.normalize(bordas, None, 0, 255, cv2.NORM_MINMAX)

# Converter para uint8 (tipo de dados de imagem)
bordas = np.uint8(bordas)

# Exibir a imagem de bordas resultante
plt.figure(figsize=(8, 8))
plt.imshow(bordas, cmap='gray')
plt.title('Imagem de Bordas (Operador de Sobel)')
plt.axis('off')
plt.show()