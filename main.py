from PIL import Image
import video_to_freeze_frame, img_process, pixel_to_coordinates
import os
import shutil

folder_name = input('Enter the path to the file: ')
video_to_freeze_frame.create_folder(folder_name)

video_path = input('Enter the full path of the video file: ')
video_to_freeze_frame.video_to_sequence(folder_name, video_path)

file_counter = 1
img_path = folder_name + os.sep + str(file_counter) + '.png'

if input('Do you need to resize images? (yes/no)   ') == 'yes':
    width = input('Enter the width in pixels: ')
    height = input('Enter the length in pixels: ')
    while True:
        try:
            img_path = folder_name + os.sep + str(file_counter) + '.png'
            x = Image.open(img_path)
            x.thumbnail((int(width), int(height)))
            x.save(img_path)
            file_counter += 1
        except:
            break

if input('Need to highlight the outline of images? (yes/no)   ') == 'yes':
    while True:
        try:
            img_path = folder_name + os.sep + str(file_counter) + '.png'
            img_process.contouring(img_path)
            file_counter += 1
        except:
            break

file_counter = 1

while True:
    try:
        img_path = folder_name + os.sep + str(file_counter) + '.png'
        img_process.greyscaling(img_path)
        file_counter += 1
    except:
        break

file_counter = 1

if input('Need to invert the color of images? (if you highlighted the outline, the background is already white) (yes/no)   ') == 'yes':
    while True:
        try:
            img_path = folder_name + os.sep + str(file_counter) + '.png'
            img_process.inverting(img_path)
            file_counter += 1
        except:
            break

file_counter = 1

if input('Need to crop the edge of an image? (yes/no)   ') == 'yes':
    while True:
        try:
            img_path = folder_name + os.sep + str(file_counter) + '.png'
            img_process.cropping(img_path)
            file_counter += 1
        except:
            break

file_counter = 1

txt_name = input('Enter the name of the txt file (without ".txt"): ')
open(txt_name + '.txt', 'w')
while True:
    try:
        img_path = folder_name + os.sep + str(file_counter) + '.png'
        pixel_to_coordinates.pixel_to_coord(img_path, txt_name, file_counter)
        file_counter += 1
    except:
        break

if input('Need to delete the folder with screenshots? (yes/no)   ') == "yes":
    try:
        shutil.rmtree(folder_name)
    except:
        print('Something went wrong when deleting the folder')
    else:
        print('Folder successfully deleted')
pluralize = ' layer' if file_counter <= 1 else ' layers'
print('The program created a txt file with ' + str((int(file_counter) - 1)) + pluralize)
