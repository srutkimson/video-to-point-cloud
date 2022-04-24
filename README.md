# video-to-point-cloud
how to use: 

1) you need to install two python libraries: cv2 and pillow
2) python3 -m pip install --upgrade Pillow
3) python3 -m pip install opencv-python
4) run the "main.py" script and follow the instructions

_____________________________________________________________________________________________

# description and feature:

turns each video frame into a coordinate layer. Z coordinate is a frame layer

in the "pixel_to_coordinates.py" file you can change the format of the output coordinate line

it is recommended to resize images to 150-200 pixels and use a video that is 15-30 seconds long

grayscale pixels below 238 in the decimal code become a dot
