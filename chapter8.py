import cv2
import numpy as np
import stack as st

def getContours(img):

    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # Area each shape
        area = cv2.contourArea(cnt)
        print(area)

        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            # Length each contour
            peri = cv2.arcLength(cnt,True)
            # print(peri)
            # Each shape corner points
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(approx)
            print("Shape edge number =",len(approx))
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objCor == 3:objectType="Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio>0.95 and aspRatio<1.05:
                    objectType="Square"
                else:
                    objectType="Rectangle"
            elif objCor>4:
                objectType="Circle"
            else:
                objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,
                        (0,255,0),2)




path = 'Resources/Shapes.jpg'
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)

getContours(imgCanny)

# cv2.imshow("Orginal Image",img)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Image Blurred", imgBlur)
imgStack = st.stackImages(0.6, ([img, imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))
cv2.imshow("Image Stack",imgStack)

cv2.waitKey(0)