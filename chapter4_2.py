import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# Görüntü üzerine doğru çizmeye yarayan kod aşağıdaki gibidir.
# opencv kütüphanesindeki "line(Görüntü,(Başlangıç noktası),(Bitiş Noktası),(Renk),(Kalınlık))"
cv2.line(img,(0,0),(512,512),(0,0,255),3)
# Köşegen boyunca doğru çizmek için kolay yol;
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(BGR Code),(Thickness))
# img.shape[0] ==>> Height
# img.shape[1] ==>> Width
# img.shape[2] ==>> Colour Layer
cv2.rectangle(img,(100,100),(250,350),(0,255,0),1)
# Görüntüye dikdörtgen eklemek için kullanılan kod parçası yukarıdaki gibidir.
# Diktörtgen ile çevrili alanı doldurmak için aşağıdaki kod parçası kullanılır.
# cv2.rectangle(img,(100,100),(250,350),(0,255,0),cv2.FILLED)
cv2.circle(img,(250,100),30,(255,0,0),cv2.FILLED)
# Görüntüye Çember eklemek için yukarıdaki kod parçası kullanılır.
cv2.putText(img,"***PYTHON OPENCV 2021***",(100,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(100,100,100),1)

cv2.imshow("Line On Image",img)

cv2.waitKey(0)