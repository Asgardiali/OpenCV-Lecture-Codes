import cv2
import numpy as np
# RGB görüntü oluşturma 8-bits
# np.zeros((Height,Width,Layers),TypeOfMatrixElements)
img = np.zeros((512,512,3),np.uint8)

imgBlue = np.zeros((512,512,3),np.uint8)
# imgBlue[Height,Width]=BGR Code
imgBlue[0:300,100:200]=255,0,0

imgBlueFull = np.zeros((512,512,3),np.uint8)
imgBlueFull[0:100,:]=0,255,0

print(img)
print(imgBlue)
print(imgBlueFull)

cv2.imshow("Image",img)
cv2.imshow("Image Blue Partially",imgBlue)
cv2.imshow("Image Full Blue",imgBlueFull)
cv2.waitKey(0)


