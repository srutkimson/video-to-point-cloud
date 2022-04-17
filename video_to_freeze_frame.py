import os
import cv2


def create_folder(folder_name):
    folder = folder_name
    os.mkdir(folder)
    print('folder "' + folder + '" has been created')


def video_to_sequence(folder,video_path):
    video_cap = cv2.VideoCapture(video_path)
    count = 1
    while True:
        success, image = video_cap.read()
        if not success:
            break
        cv2.imwrite(folder + os.sep + str(count) + '.png', image)
        count += 1
    print("{} frames extracted to the {}.".format(count, folder))

