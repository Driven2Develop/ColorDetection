# Color Detection

This a program meant to detect colors in a sample video. The colors are highlighted in real time and a box is drawn around them. 

The main program is executed from the *Image_processing.py* script while *Suitable_hues.py* is a supplementary script meant to run tests to determine the best range of HSV (Hue, Saturation, Value) values for the desired colors.

## The methodology

Colors in computer vision are represented as an ordered triple. Each of them represent an RGB value. The *Suitable_hues.py* script is meant to find the best range to identify different colors. These values can be modified manually, but are susceptible to filtering, color correction, brightening, and more. Therefore, the video will first be filtered to remove noise, erode the video, and dilate the video.

Each of the pixels in the video are analyzed and checked to see if they fit within the desired ranges specified within the code. If the pixels fit with the desired range then they are combined together and a rectangle is drawn around them. 

Finally, to avoid false positive colors, rectangles are only drawn around groups of pixels with a suitable size.

Finally, the color, shape and movement information are used to track the colors as the video progresses. 

## Executing the program

Be sure to run the program *Image_Processing.py* from the main directory: ColorDetection, OpenCV is not a library that is well versed in handling paths to videos efficiently. It is also necessary to have the [OpenCV Python Module](https://docs.opencv.org/) installed.

```pip install opencv-python```

For more details consult with the *Image_processing.docx* document.  