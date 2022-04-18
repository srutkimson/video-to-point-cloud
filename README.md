# video-to-point-cloud
how to use: 

you need to install two python libraries: cv2 and pillow

python3 -m pip install --upgrade Pillow

python3 -m pip install opencv-python

run the "main.py" script and follow the instructions

_____________________________________________________________________________________________

description and feature:

turns each video frame into a coordinate layer. Z coordinate is a frame layer

in the "pixel_to_coordinates.py" file you can change the format of the output coordinate line

it is recommended to resize images to 150-200 pixels

grayscale pixels below 238 in the decimal code become a dot
