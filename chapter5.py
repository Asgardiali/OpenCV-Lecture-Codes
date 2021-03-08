import cv2
import numpy as np

img = cv2.imread("Resources/iskambil.jpg")

width, height = 900,500

# Burada resim içerisinde seçilmek istenilen nesnenin köşelerindeki
# pixel numaralarına göre sınır belirlemesi yapılır.
pts1 = np.float32([[398,212],[506,98],[558,365],[663,250]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
