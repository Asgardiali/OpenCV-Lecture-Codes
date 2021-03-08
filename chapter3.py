import cv2
import numpy as np

img = cv2.imread("Resources/talisman.jpg")
print(img.shape)
# "img.shape" komutu ile görüntünün boyutu elde edilir.
# Yükseklik Genişlik RGB bilgisini verir. (Height,Width,BGR)

imgResized = cv2.resize(img,(500,300))
print(imgResized.shape)
# Görüntüyü tekrardan boyutlandırmak için "resize" metodu kullanılır.
# imgResized = cv2.resize(Boyutlandırılmak istenilen görüntü,(Width,Height))

imgCropped = img[200:300,0:300]
# imgCropped = img[Height,Width]
# Görüntüyü kırpmak için matris olarak düşünülen görüntünün
# hengi pixeller arasında kesilmesi isteniyor ise ona göre
# sınırlarının belirlenmesidir.


cv2.imshow("Renault Talisman Image",img)
cv2.imshow("Renault Talisman Image Resized",imgResized)
cv2.imshow("Renault Talisman Image Cropped",imgCropped)


cv2.waitKey(0)