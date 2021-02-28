from cv2 import *
#drawing a rectangle around a certain object
#rectangle(sourceimg, startpoint, endpoint, colour, thickness)
img=imread("sample2.jpg")
rectangle(img,(30, 40),(550,500),(0,255,0),2)
imwrite("rectangle.jpg", img)
imshow("rectangle.jpg", img)
#putting text on an image
putText(img,"Watermelon Suga Highhh", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
imwrite("putText.jpg", img)
imshow("putText.jpg", img)
#findContours:
cnts=cv2.findContours(img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
imwrite("Contour.jpg", cnts)
imshow("Contour.jpg", cnts)
