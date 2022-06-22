# hack-arch

numpy
Numpy was imported to take data from the webcam of the device.

tensorflow
tensorflow was imported to train the data.For our project the number plates of various vehicles was used as data.

opencv
opencv was used to operate the webcam.This module integrates the program with the device being used.

YOLOv4
YOLOv4 is used to input pretrained weights for object detection.

![image](https://user-images.githubusercontent.com/92539781/174950685-134d36e2-bcd0-494b-8b40-8b6baeaad042.png)

Tesseract OCR
We have created a custom function to feed Tesseract OCR the bounding box regions of license plates found by custom YOLOv4 model in order to read and extract the license plate numbers. Thorough preprocessing is done on the license plate in order to correctly extract the license plate number from the image. The function that is in charge of doing the preprocessing and text extraction is called recognize_plate and can be found in the file core/utils.py.

First step of the process is taking the bounding box coordinates from YOLOv4 and simply taking the subimage region within the bounds of the box. Since this image is super small the majority of the time we use cv2.resize() to blow the image up 3x its original size.

Then we convert the image to grayscale and apply a small Gaussian blur to smooth it out.

Following this, the image is thresholded to white text with black background and has Otsu's method also applied. This white text on black background helps to find contours of image.

The image is then dilated using opencv in order to make contours more visible and be picked up in future step.

Next we use opencv to find all the rectangular shaped contours on the image and sort them left to right.

[image](https://user-images.githubusercontent.com/92539781/174951625-36ea8084-8229-4bca-8ac9-09ba8a7a362e.png)

As you can see this causes many contours to be found other than just the contours of each character within the license plate number. In order to filter out the unwanted regions we apply a couple parameters to be met in order to accept a contour. These parameters are just height and width ratios (i.e. the height of region must be at least 1/6th of the total height of the image). A couple other parameters on area of region etc are also placed. Check out code to see exact details. This filtering leaves us with.

[image](https://user-images.githubusercontent.com/92539781/174951593-c07e8357-82ee-4a23-a22a-46ddae695381.png)

The individual characters of the license plate number are now the only regions of interest left. We segment each subimage and apply a bitwise_not mask to flip the image to black text on white background which Tesseract is more accurate with. The final step is applying a small median blur on the image and then it is passed to Tesseract to get the letter or number from it. Example of how letters look like when going to tesseract.

[image](https://user-images.githubusercontent.com/92539781/174951554-206eb0d0-0e66-4cce-9cbc-379affaef56e.png)

Each letter or number is then just appended together into a string and at the end you get the full license plate that is recognized.

