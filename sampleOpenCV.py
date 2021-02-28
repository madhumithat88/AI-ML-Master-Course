from cv2 import *
#imread, imwrite and imshow functions:
img=imread("sample1.jpg")
imshow("sample1", img)
grayImg=cvtColor(img,cv2.COLOR_BGR2GRAY) #changes the image colour to grey
imwrite("grayscale.jpg", grayImg) #creates a new file/copy of the mentioned image
imshow("grayscale.jpg", grayImg)  #shows the specified image on the screen
#image properties:
print(img.shape) #(564, 564, 3)
print(img.size) #954288
print(img.dtype) #uint8
waitKey(0)
destroyAllWindows()
