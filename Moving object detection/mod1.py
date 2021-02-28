from cv2 import *
from imutils import *
#resizing the image
img=imread("sample2.jpg")
resizeImg=resize(img, width=200) #resizes the given image
imwrite("resizedimage.jpg", resizeImg) #creates the above image in the folder
imshow("resizedimage.jpg", resizeImg) #displays the mentioned image on the screen when we run the program
#applying GaussianBlur
gbimg=GaussianBlur(img,(21,21),0) #function: cv2.GaussianBlur(sourceimage, (kernel), borderType)
imwrite("GaussianBlurImage.jpg", gbimg)
imshow("GaussianBlurImage.jpg", gbimg)
#thresholding:
thresholdimg=threshold(gbimg, 200, 255, THRESH_BINARY)[1] #the function returns a tuple of two values and we're choosing the [1] value of the tuple
imwrite("thresholdedImage.jpg", thresholdimg)
imshow("thresholdedImage.jpg", thresholdimg)
