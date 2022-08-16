"""Get bounding box of cropped image from original image."""

import sys
import os
import cv2 as cv
import numpy as np
import pyautogui as pg

from matplotlib import pyplot as plt



IMAGES_DIR = 'E:/ml_test/osrs_auto/images'

def make_img_path(img_name):
    return '/'.join([IMAGES_DIR, img_name])

print('Trying to test image recognition...')
#
if os.path.exists(r'E:\ml_test\osrs_auto\images\shot1.jpg'):
    print('Reading img')
    # img_rgb = cv.imread(r'E:\ml_test\osrs_auto\images\shot1.jpg')
    # img_rgb = cv.imread(make_img_path('shot1.jpg'))
    img_rgb = cv.imread(make_img_path('shot3.jpg'))
    # print(img_rgb)
    print('Image read')
else:
    print('Cannot find the image')
    exit(1)
# # the cropped image, expected to be smaller
if os.path.exists(r'E:\ml_test\osrs_auto\images\target1.jpg'):
    print('Reading img')
    # target_img = cv.imread(r'E:\ml_test\osrs_auto\images\target1.jpg')
    target_img = cv.imread(make_img_path('target1.jpg'))
    # print(target_img)
    print('Image read')
else:
    print('Cannot find the image')
    exit(1)


_, w, h = target_img.shape[::-1]
res = cv.matchTemplate(img_rgb, target_img, cv.TM_CCOEFF_NORMED)

print('Showing the res probably confidence levels...')
# print(res)

# with the method used, the date in res are top left pixel coords
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc

print(f'The max and min values are {max_val} and {min_val} respectively')

# To check if target exists, use a threshold on max_val
if max_val < 0.7:
    print('The target image is not present in the background image!')
else:
    print('Target image found!')

    # if we add to it the width and height of the target, then we get the bbox.
    bottom_right = (top_left[0] + w, top_left[1] + h)

    pg.moveTo(top_left)

    # cv.rectangle(img_rgb, top_left, bottom_right, 255, 2)
    # cv.imshow('', img_rgb)
    #
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    # cv.waitKey(1)




#
print('Reaches end')
