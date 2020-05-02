#CSI 4124 Project
#import necessary libraries
import cv2
import numpy as np

#save video to a global variable, as well as width and height.
video=cv2.VideoCapture("videos/video1.avi")
width=int(video.get(3))
height=int(video.get(4))

#global variable for different kernels so that erosion and dilation can be used to better isolate colors. 
big_kernel=np.ones((2,2),np.uint8)
small_kernel=np.ones((1,1),np.uint8)

#upper and lower bounds for green, yellow, and red, and blue.
#If a pixel is within these color range then it is an acceptable color. 
lower_green=np.array([45,100,100])
upper_green=np.array([75,255,255])
lower_yellow=np.array([19,100,100])
upper_yellow=np.array([30,255,255])
lower_red=np.array([0,151,50])
upper_red=np.array([4,255,255])
lower_blue=np.array([95,70,0])
upper_blue=np.array([100,255,255])

#go through all frames of the video. 
while(video.isOpened()):
	#read video frame by frame
	ret, frame = video.read()
	#convert to HSV color space
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#create masks using boundaries with inRange function. 
	#based on previous testing, green color detection works best with the big kernel.
	green_mask=cv2.inRange(hsv_frame,lower_green,upper_green)
	green_mask=cv2.dilate(cv2.erode(green_mask,big_kernel,iterations=1),big_kernel,iterations=2)

	#based on previous testing, yellow color detection works best with the small kernel.
	yellow_mask=cv2.inRange(hsv_frame,lower_yellow,upper_yellow)
	yellow_mask=cv2.dilate(cv2.erode(yellow_mask,big_kernel,iterations=1),small_kernel,iterations=1)

	#based on previous testing, red color detection works best with the big kernel.
	red_mask=cv2.inRange(hsv_frame,lower_red,upper_red)
	red_mask=cv2.dilate(cv2.erode(red_mask,big_kernel,iterations=2),big_kernel,iterations=2)

	#based on previous testing, blue color detection works best with the big kernel.
	blue_mask=cv2.inRange(hsv_frame,lower_blue,upper_blue)
	blue_mask=cv2.dilate(cv2.erode(blue_mask,big_kernel,iterations=1),big_kernel,iterations=2)

	#detect contours for all colors and then for each contour set as a minimum enclosing circle. 
	im2_green, contours_green, hierarchy_blue = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	im2_yellow, contours_yellow, hierarchy_blue = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	im2_red, contours_red, hierarchy_blue = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	im2_blue, contours_blue, hierarchy_blue = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	#for all the green detected circles, draw rectangles
	for c in contours_green:
		#set the minimum enclosing circle, 
		((x, y), r) = cv2.minEnclosingCircle(c)

		#for all circles with radius larger than 9 draw the rectangles using the center of the circle and then add text. 
		if(r>9): 
			cv2.rectangle(frame, (int(x-40),int(y-30)), (int(x+40),int(y+30)), (255,255,255), 2)
			cv2.putText(frame,'green',(int(x+50),int(y+30)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'x=' + str(int(x)),(int(x+50),int(y+20)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'y='+str(int(y)),(int(x+50),int(y+10)),cv2.FONT_HERSHEY_PLAIN,1,255)

	#for all the yellow detected circles, draw rectangles
	for c in contours_yellow:
		#set the minimum enclosing circle, 
		((x, y), r) = cv2.minEnclosingCircle(c)

		#for all circles with radius larger than 9 draw the rectangles using the center of the circle and then add text. 
		if(r>9):
			cv2.rectangle(frame, (int(x-40),int(y-30)), (int(x+40),int(y+30)), (255,255,255), 2)
			cv2.putText(frame,'yellow',(int(x+50),int(y+30)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'x=' + str(int(x)),(int(x+50),int(y+20)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'y='+str(int(y)),(int(x+50),int(y+10)),cv2.FONT_HERSHEY_PLAIN,1,255)

	#for all the red detected circles, draw rectangles
	for c in contours_red:
		#set the minimum enclosing circle, 
		((x, y), r) = cv2.minEnclosingCircle(c)

		#for all circles with radius larger than 9 draw the rectangles using the center of the circle and then add text. 
		if(r>9):
			cv2.rectangle(frame, (int(x-40),int(y-30)), (int(x+40),int(y+30)), (255,255,255), 2)
			cv2.putText(frame,'red',(int(x+50),int(y+30)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'x=' + str(int(x)),(int(x+50),int(y+20)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'y='+str(int(y)),(int(x+50),int(y+10)),cv2.FONT_HERSHEY_PLAIN,1,255)

	#for all the red detected circles, draw rectangles
	for c in contours_blue:
		#set the minimum enclosing circle, 
		((x, y), r) = cv2.minEnclosingCircle(c)

		#for all circles with radius larger than 9 draw the rectangles using the center of the circle and then add text. 
		if(r>9):
			cv2.rectangle(frame, (int(x-40),int(y-30)), (int(x+40),int(y+30)), (255,255,255), 2)
			cv2.putText(frame,'blue',(int(x+50),int(y+30)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'x=' + str(int(x)),(int(x+50),int(y+20)),cv2.FONT_HERSHEY_PLAIN,1,255)
			cv2.putText(frame,'y='+str(int(y)),(int(x+50),int(y+10)),cv2.FONT_HERSHEY_PLAIN,1,255)

	#display the video 
	cv2.imshow('original', frame)

	#exit when video ends or 'q' is pressed
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

#release resources
video.release()
cv2.destroyAllWindows()