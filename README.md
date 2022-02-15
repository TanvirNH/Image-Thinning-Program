# Image Thinning Program

## Author
- Tanvir N Hasan

## Environment
- OS: macOS Monterey
- Python: 3.9.7
- NumPy: 1.21.1
- Matplotlib: 3.4.2
- OpenCV: 4.5.5

## Introduction
- What is thinning?

Thinning is a morphological operation that is used to remove selected foreground pixels from binary images, somewhat like erosion or opening. It can be used for several applications, but is particularly useful for skeletonization. In this mode it is commonly used to tidy up the output of edge detectors by reducing all lines to single pixel thickness. Thinning is normally only applied to binary images, and produces another binary image as output (Morphology - Thinning, 2004).

More information about image thinning can be found in this URL: https://homepages.inf.ed.ac.uk/rbf/HIPR2/thin.htm


- What does this program do?

This Python program consists of thinning an image and then displaying the input and output images. 

## Implementation of the Program
We will go through the helper functions used throughout the program before discussing the implementation of the main thinning algorithm. In order to promote code reusability and readability, each of these was placed inside a function.

The function 'def is_or_not_blk_pixel(arr, a, b)’ will be our starting point.

This function's main goal is to detect if a pixel represented by the arrays 'a' and 'b' is a black pixel
or not.

![Screen Shot 2022-02-14 at 9 44 45 PM](https://user-images.githubusercontent.com/68251349/153982718-bd1f179e-e50a-4c82-a2b1-cd04f131d91c.png)

Second, we'll look at the 'def blk_neighboring_pixels(arr, a, b)' function. This function's primary goal is to determine the number of black pixels that surround the middle pixel. The function accomplishes this by inspecting each and every pixel in the neighborhood. After calculating the sum, it returns TRUE if the result falls within [2,6]; else, it returns FALSE.

![Screen Shot 2022-02-14 at 9 45 44 PM](https://user-images.githubusercontent.com/68251349/153982804-94e761e8-ddff-4f76-ad4e-7f8029c12ae3.png)

Now we will look at the function 'def wt_blk_transitions(arr, a, b)'. The main purpose of this function is to count the amount of white to black transitions in the neighborhood. The function accomplishes this by first populating an array called 'nbr' with the surrounding values in such an order that while examining for adjacency in nbr, it also examines for transitions in the matrix.

![Screen Shot 2022-02-14 at 9 46 20 PM](https://user-images.githubusercontent.com/68251349/153982855-2eea50b5-c4fc-4ada-a911-5109f5c2bcc9.png)

Now, we will look at the functions, 'def first_step_c(arr, a, b)', 'def first_step_d(arr, a, b)', 'def second_step_c(arr, a, b)' and 'def second_step_d(arr, a, b)'. These functions are used to check for the thinning algorithm's conditions c, d, c', and d', respectively. The functions can do this by inspecting the values in the array, for example, 2,4,5 for condition c, and determining whether they are zero.

![Screen Shot 2022-02-14 at 9 46 56 PM](https://user-images.githubusercontent.com/68251349/153982934-542bbad4-8b98-48f0-85bf-673ad3584e27.png)

Finally, we will discuss the implementation of the main thinning algorithm 'def image_thinning()'. This main function utilizes all of the previously mentioned helper functions. First, the function declares two arrays, 'first_step' and 'second_step.' The algorithm is then put into action by first running all of the helper functions to determine whether the middle pixel is a suitable candidate for removal. This procedure is performed once with the conditions a, b, c, and d. All the pixels which are candidates for removal are stored in the array ‘first_step’. The pixels are then deleted from the image when sub-iteration 1 has been performed. The pixels are then deleted in sub-iteration 2 using a similar procedure. This two-step procedure is repeated until either 'first_step,' or the 'second_step' is empty, indicating that there are no more pixels left to delete. It is also worth noting here that 'first_step' and 'second_step' are emptied before the iterations take place so that if there are no pixels to be removed, then the loop ultimately ends.

![Screen Shot 2022-02-14 at 9 49 17 PM](https://user-images.githubusercontent.com/68251349/153983201-173b42e0-798c-47a6-b2ce-b1c71b827514.png)


## Final Result

Executing the program:

![Screen Shot 2022-02-14 at 10 05 41 PM](https://user-images.githubusercontent.com/68251349/153984982-83a32484-e8b1-4a01-9445-6007195aed44.png)

The following are the input and output results for ‘input_image1.jpg':

![Screen Shot 2022-02-14 at 9 50 24 PM](https://user-images.githubusercontent.com/68251349/153983321-78371d8e-3858-410f-b635-970b2590f43f.png)

The following are the input and output results for ‘input_image2.jpg’:

![Screen Shot 2022-02-14 at 9 50 54 PM](https://user-images.githubusercontent.com/68251349/153983358-bbebce5d-9ed9-4438-be03-292a530e47a6.png)


## References

- Morphology - Thinning. (2004, March 1). Image Processing Learning Resources. Retrieved February 14, 2022, from https://homepages.inf.ed.ac.uk/rbf/HIPR2/thin.htm


