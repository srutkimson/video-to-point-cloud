from PIL import Image, ImageFilter
import PIL.ImageOps


def greyscaling(img):
    x = Image.open(img)
    x = x.convert('L')
    x.save(img)


def contouring(img):
    x = Image.open(img)
    x = x.filter(ImageFilter.CONTOUR)
    x.save(img)


def cropping(img):
    q = Image.open(img)
    x, y = q.size
    q = q.crop((1, 1, x - 1, y -1))
    q.save(img)


def inverting(img):
    q = Image.open(img)
    x = PIL.ImageOps.invert(q)
    x.save(img)
