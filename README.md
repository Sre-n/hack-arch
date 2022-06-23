# hack@arch

# "Innovation is the only way to win"- Steve Jobs
This project is done as part of abstarct submission of a 36-hours offline hackathon under the aLluring arch of GEC.

![image](https://user-images.githubusercontent.com/92539781/175336796-847088f7-1ba6-45c9-9b5a-8d123b9e7820.png)


# Problem Statement
Bus Map How to help riders know bus route information



# Solution
A pamphlet that gives better demonstration of bus route information



# Our goal
![image](https://user-images.githubusercontent.com/92539781/175337271-c1fb49a4-aaaf-47a7-89d7-23bcd7136a94.png)


# Modules Used
♦numpy
♦tensorflow
♦opencv
♦Tesseract OCR
♦imutils
♦skimage
♦pytesseract
♦argparse


# Approach
First step of the process is simply taking the subimage region within the bounds of the box. Since this image is super small 
majority of the time we use cv2.resize() to blow the image up to 3x its original size. Then we convert the image to grayscale
and applied a small Gaussian blur to smooth it out. Following this, the image is thresholded to white text with black background 
and has Otsu's method also applied. This white text on black background helps to find contours of image.
![image](https://user-images.githubusercontent.com/92539781/175347998-abe38586-35b9-46fa-b179-fe0ac01e1bc7.png)

The image is then dilated using opencv in order to make contours more visible and be picked up in future step.
![image](https://user-images.githubusercontent.com/92539781/175348083-55a2c042-0543-4cec-95fe-fe19cef2b4f3.png)

Next we use opencv to find all the rectangular shaped contours on the image and sort them left to right.
![image](https://user-images.githubusercontent.com/92539781/174951625-36ea8084-8229-4bca-8ac9-09ba8a7a362e.png)

In order to filter out the unwanted regions we apply a couple parameters to be met in order to accept a contour. 
These parameters are just height and width ratios (i.e. the height of region must be at least 1/6th of the total height of the image).
A couple other parameters on area of region etc are also placed. Check out code to see exact details.

![image](https://user-images.githubusercontent.com/92539781/174951593-c07e8357-82ee-4a23-a22a-46ddae695381.png)

The individual characters of the license plate number are now the only regions of interest left. We segment each subimage and apply 
a bitwise mask to flip the image to black text on white background which Tesseract is more accurate with. The final step is applying 
a small median blur on the image and then it is passed to Tesseract to get the letter or number from it. Example of how letters look 
like when going to tesseract.

![image](https://user-images.githubusercontent.com/92539781/174951554-206eb0d0-0e66-4cce-9cbc-379affaef56e.png)

![image](https://user-images.githubusercontent.com/92539781/175357172-3768a7c6-5c51-4425-9d0f-a25eb46c63fc.png)


Since we are done with object detection, scanning of number plate and character recognition our next aim lies in showing the bus route.
Here we followed the measure of integrating google map api via google cloud and exported a html file to direct to the webpage showing
the complete route
♦ gmaps

![image](https://user-images.githubusercontent.com/92539781/175357378-0226a36f-d420-448f-8f50-893aa45da70e.png)

