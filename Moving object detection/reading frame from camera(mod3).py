from cv2 import *
vs=VideoCapture(0) #(0) specifies which camera to use. here, 0 is the primary cam i.e laptop's webcam
while True:
    x,img=vs.read() #read() function returns 2 values. we dont need the first one(x) and we're naming the second one img for future use
    imshow("VideoStream", img) #displays the videostream on the screen
    key=waitKey(1) & 0xFF #determines when to stop the display
    if key==ord("q"): #here, we are giving the trigger as char "q" to stop the video(we can put any string/number we want)
        break
vs.release() #frees the camera i.e stops it's running
destroyAllWindows()
