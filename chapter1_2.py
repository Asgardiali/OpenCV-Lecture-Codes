import cv2

print("OpenCV Library Installed Succesfully!!!")

cap = cv2.VideoCapture("Resources/videoplayback.mp4")
# Proje içerisindeki kayıtlı videodan veri çekmek için kullanılır.

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    # 'q' basıldığında videodan çıkar.
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break