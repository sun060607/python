import cv2
import numpy as np
src = cv2.imread('./data/colorball.jpg',cv2.IMREAD_COLOR)
dst = src.copy()
hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
lower_orange = (14,50,50) #주황색 범위
upper_orange =(28,255,255)
mask = cv2.inRange(hsv,lower_orange,upper_orange)
orange=cv2.bitwise_and(src,src,mask=mask)
gray=cv2.cvtColor(orange,cv2.COLOR_RGB2GRAY)
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=250,param2=10,minRadius=100,maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0]:
        center=(i[0],i[1])
        radius = i[2]
        cv2.circle(orange,center,radius,(255,255,255),5)
        cv2.circle(orange,center,radius=5,color=(0,255,0),thickness=-1)

cv2.imshow('orange',orange)
cv2.waitKey()
cv2.destroyAllWindows()