# OpenCV-Lecture-Codes

------------------------------------------------------------------
Chapter of Video Lecture
------------------------------------------------------------------
1 - Read Image/Videos/Webcam
2 - Basics Functions
3 - Resizing and Cropping
4 - Shapes and Texts
5 - Warp Prespective
6 - Joining Image
7 - Color Detection
8 - Contours / Shape Detection
9 - Face Detection
10 - Project 1
11 - Project 2
12 - Project 3

# If you want to call function in py files out of main.py, you will go on these steps;
1 - Your function name is stackImage() in stack.py
2 - import stack
3 - stack.stackImages()
# 
import stack
path = 'Resources/Shapes.jpg'
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgStack = stack.stackImages(0.5, ([img, imgGray]))
cv2.imshow("Image with gray level",imgStack)
