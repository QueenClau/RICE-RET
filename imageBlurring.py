import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('image_test.png')

# blur = cv2.blur(img,(5,5))
# blur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()