import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('image_test.jpg',0) #reads image
cv2.imshow('image',img) #displays image
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('graypic.png',img)
    cv2.destroyAllWindows()
