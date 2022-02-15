
"""
Copyright 2022 Tanvir N Hasan

Licensed under the GNU General Public License, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# Required library imports
import math
import numpy as np
import matplotlib.pyplot as plt
import cv2

# This function determines if the middle pixel in the array indicated by the variables 'a' and 'b' is a black pixel or not
def is_or_not_blk_pixel(arr, a, b): 
    if arr[a][b] == 1:
        return True
    return False

# This function checks for condition one, calculating the amount of black pixels around the middle pixel and determining if the neighboring pixels have two to six black pixels
def blk_neighboring_pixels(arr, a, b):
    if (2 <= arr[a, b-1] + arr[a+1, b-1] + arr[a+1, b] + arr[a+1, b+1] + arr[a, b+1] + arr[a-1, b+1] + arr[a-1, b] + arr[a-1, b-1] <= 6):
        return True
    return False

# This function checks for condition two, calculating the number of white to black transitions in the areaneighborhood and determining if there is approximately one (0-1) pair
def wt_blk_transitions(arr, a, b):
    nbr = [arr[a, b-1], arr[a+1, b-1], arr[a+1, b], arr[a+1, b+1], arr[a, b+1], arr[a, b+1], arr[a-1, b], arr[a-1, b-1], arr[a, b-1]]
    trns = 0
    for i in range(len(nbr) - 1):
        if nbr[i] == 0 and nbr[i+1] == 1:
            trns += 1
    if trns == 1:
        return True
    return False

def first_step_c(arr, a, b): # This function verifies that the first step's condition three is met 
    if (arr[a, b-1] and arr[a+1, b] and arr[a, b+1]) == False:
        return True
    return False

def first_step_d(arr, a, b): # This function verifies that the first step's condition four is met 
    if (arr[a+1, b] and arr[a, b+1] and arr[a-1, b]) == False:
        return True
    return False

def second_step_c(arr, a, b): # This function verifies that the second step's condition three is met 
    if (arr[a, b-1] and arr[a+1, b] and arr[a-1, b]) == False:
        return True
    return False

def second_step_d(arr, a, b): # This function verifies that the second step's condition four is met 
    if (arr[a, b-1] and arr[a, b+1] and arr[a-1, b]) == False:
        return True
    return False
 
# The main thinning method is demonstrated in this function.
def image_thinning():
    first_step = [(-1, -1)]
    second_step = [(-1, -1)]

    while first_step or second_step:
        first_step = []
        for a in range(1, len(Bin_Threshold) - 1):
            for b in range(1, len(Bin_Threshold[a]) - 1):
                if (is_or_not_blk_pixel(Bin_Threshold, a, b) and 
                blk_neighboring_pixels(Bin_Threshold, a, b) and
                wt_blk_transitions(Bin_Threshold, a, b) and
                first_step_c(Bin_Threshold, a, b) and
                first_step_d(Bin_Threshold, a, b) ):
                    first_step.append((a, b))

        for pxl in first_step:
            Bin_Threshold[pxl] = 0

        second_step = []
        for a in range(1, len(Bin_Threshold) - 1):
            for b in range(1, len(Bin_Threshold[a]) - 1):
                if (is_or_not_blk_pixel(Bin_Threshold, a, b) and 
                blk_neighboring_pixels(Bin_Threshold, a, b) and
                wt_blk_transitions(Bin_Threshold, a, b) and
                second_step_c(Bin_Threshold, a, b) and
                second_step_d(Bin_Threshold, a, b) ):
                    second_step.append((a, b))
        for pxl in second_step:
            Bin_Threshold[pxl] = 0
    return Bin_Threshold

# This is where we insert the image, with the grayscale set to zero.
input_img = cv2.imread('input_image1.jpg', 0)  # Input either 'input_image1.jpg' or 'input_image2.jpg'
_, Original_Threshold = cv2.threshold(input_img, 0, 255, cv2.THRESH_BINARY)
Bin_Threshold = (Original_Threshold == 0).astype(int)
cv2.imshow('Image', Original_Threshold)
img = image_thinning()
thinned_output_img = (img == 0).astype(np.uint8)
thinned_output_img *= 255
cv2.imshow('Original Input Image', input_img)
cv2.imshow('Thinned Output Image', thinned_output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(Bin_Threshold)