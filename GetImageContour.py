#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image
from PIL import ImageFilter

im = Image.open('birdnest.jpg')
om = im.filter(ImageFilter.CONTOUR)
om.save('birdnestContour.jpg')