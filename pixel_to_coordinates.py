from PIL import Image


def pixel_to_coord(img, txt_file_name, z):
    img = Image.open(img)
    file = open(txt_file_name + '.txt', "a")
    width, height = img.size
    for x in range(width):
        for y in range(height):
            if img.getpixel((x, y)) < 238:
                file.write(str(x) + ', ' + str(y) + ', ' + str(z) + '\n')   # Here you can change the format
                                                                            # of the output coordinate line