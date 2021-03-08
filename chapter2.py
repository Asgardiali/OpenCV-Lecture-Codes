import cv2
import numpy as np

img = cv2.imread("Resources/Lena.png")
# Kernel oluşturmak için matematik kütüphanesi olan numpy import edildi.
# Unsigned integer tipinde 5x5 lik matrisin tüm elemanları 1 yapıldı.
kernel = np.ones((5,5),np.uint8)

# Görüntüyü grayscale görüntüye çevirmek için "cvtColor(img,cv2.COLOR_BGR2GRAY)" komutu kullanılır.
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Görüntüye Gaussian Filtre ekleyerek blurlama yapılıyor. Burada ksize = Kernel sayısıdır.
# Yani maskeleme matrisinin boyutudur.
imgBlur = cv2.GaussianBlur(imgGray,(3,3),0)
# Köşeleri bulmak için Canny metodu kullanılır. Bununda kodu aşağıdaki gibidir.
imgCanny = cv2.Canny(imgGray,50,200)
# Morfolojik işlemlerde görüntü dialation işlemi için aşağıdaki kod parçası kullanılır.
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# Dialation işleminin tersi olan erode işlemi yapmak için aşağıdaki kod parçası kullanılır.
imgErode = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Gray Scale Lena Image",imgGray)
cv2.imshow("Blurred Lena Image",imgBlur)
cv2.imshow("Canny Edge Detection Lena Image",imgCanny)
cv2.imshow("Dialation Process Lena Image",imgDialation)
cv2.imshow("Erode Process Lena Image",imgErode)
cv2.waitKey(0)
