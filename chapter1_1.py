import cv2

print("****************************************************************************************************")
print("Package Installed Successfully!!!")
print("****************************************************************************************************")

# Resimleri okumak için proje dosyası içerisinden çekilmesi gerekir.
# Resources klasöründen "imread" komutuyla değişkene ataması yapılır.
img = cv2.imread("Resources/Lena.png")
# Resimleri göstermek için ise "imshow" komutu kullanılır.
cv2.imshow("Lena",img)

# waitKey içerisindeki değer ms cinsindendir.
# 0 değeri verilince sonsuz bekleme sağlar.
cv2.waitKey(0)