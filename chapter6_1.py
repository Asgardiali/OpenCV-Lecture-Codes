import cv2
import numpy as np

img = cv2.imread("Resources/Lena.png")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Görüntüleri bir arada tutmaya yarayan satırda sıralama veya sütunda sıralama yapacağız.

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Image Horizontal",imgHor)
cv2.imshow("Image Vertical",imgVer)
# Bu yöntem ile resimleri tekrardan boyutlandırarak göstermek pek mümkün değildir. Bu
# nedenden dolayı birleştirilen görüntüler ekran sığmayabilir ve diğer görüntüler
# görünmeyebilir. Ayrıca bu metotta aynı görüntü kanalına sahip görüntüler gösterilebilir.
# Yani ya hepsi RGB olacak yada hepsi gray level olmalıdır.

cv2.waitKey(0)