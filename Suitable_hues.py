#CSI 4124 Project
import cv2
import numpy as np

#save video to a global variable, use global frames as well. 
video = cv2.VideoCapture("videos/video2.avi")
ret, origframe = video.read()
frame = origframe

def adjustHue(hue):
	global frame
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	for i in range (0, frame.shape[0]): 
		for j in range (0, frame.shape[1]): 
			if(frame[i,j,0]>hue+10 or frame[i,j,0]<hue-10):
				frame[i][j] = [0,0,0]
			else:
				frame[i][j]=[255,255,255]
	cv2.imshow('Determine Hue values for colors', frame)
	frame = origframe

cv2.namedWindow('Determine Hue values for colors')
cv2.createTrackbar('Hue Value', 'Determine Hue values for colors', 0, 179, adjustHue)

cv2.imshow('original', origframe)
cv2.imshow('Determine Hue values for colors', frame)
cv2.waitKey(0)