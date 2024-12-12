# ---------------------------------------------------- #
# Assignment 1 - SECV3213 FIP - Section 1 - Group 3    #
# 1. Bilkis Musa A20EC0233                             #
# 2. Fatin Aimi Ayuni Binti Affindy A20EC0190          #
# -----------------------------------------------------#

import cv2 as cv
import numpy as np
from tkinter import *

# this function will minus the values of the image to darken the image
def  minusTrunc(img,num):
    img1=img
    (x,y) = img1.shape 
    for i in range(0,x):
           for j in range(0,y):
               if (img[i,j]< num):
                img1[i,j]=0; 
               else: 
                 img1[i,j] = img[i,j]-int(num);                 
    return img1

# this function will display a text box to give instruction to the user on how to
# navigate the interface
top = Tk()  
top.title('Instruction')
top.geometry('600x170')
text = Text(top, height=200, width=300)
text.insert(INSERT, '! ! ! PLEASE READ BEFORE START ! ! !\n\n')
text.insert(INSERT, '1. Select a ROI and then press SPACE or ENTER button!\n\n')
text.insert(INSERT, '2. Repeat step 1 to select multiple region\n\n')
text.insert(INSERT, '3. Finish the selection of region(s) by pressing ECS button!\n\n')
text.insert(INSERT, '4. Please close this window to begin cropping image\n\n')
text.pack()
top.mainloop()

# this line will create a blank window named 'Image'
cv.namedWindow('Image')

# this line will read the image cat.jpg from the same folder and convert it to grayscale
image = cv.imread('cat.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# this line will take the dimension of the image
size = image.shape
x = size[0]
y = size[1]

# this line will enable the user to select multiple part of image to be manipulated
# depending on the choice chosen by the user
selected = cv.selectROIs('Image', image, showCrosshair=False)

# these are to initialize the values
cropnum = 0
cropim = image.copy()

# this function will darken the regions chosen by the user
def darken():
    
    global cropnum
    for rect in selected:
        
        x1=rect[0]
        y1=rect[1]
        x2=rect[2]
        y2=rect[3]

        cropim = image[y1:y1+y2, x1:x1+x2]

        x = np.uint8(90)
        gray = cv.cvtColor(cropim, cv.COLOR_BGR2GRAY)
        img_dark = minusTrunc(gray,x)

        cv.imshow("Darken"+str(cropnum+1), img_dark)
        cv.imwrite("Darken"+str(cropnum+1)+" .jpg", img_dark)

        cropnum += 1

    cv.waitKey(0)

# this function will give blur to the regions chosen by the user with the kernel size of 10
def blur(): 
    
    global cropnum
    for rect in selected:
        
        x1=rect[0]
        y1=rect[1]
        x2=rect[2]
        y2=rect[3]

        cropim = image[y1:y1+y2, x1:x1+x2]
        
        img_blur = cv.blur(cropim, (10,10))

        cv.imshow("Blur"+str(cropnum+1), img_blur)
        cv.imwrite("Blur"+str(cropnum+1)+" .jpg", img_blur)

        cropnum += 1

    cv.waitKey(0)


# this function will display a window with text and button to help navigate the user
top = Tk()  
top.title('Action')
top.geometry('670x230')
text = Text(top, height=200, width=300)
text.insert(INSERT, '1. Click the button to view the cropped image in chosen condition(darken/blur)\n\n')
text.insert(INSERT, '2. Press SPACE to reset the button\n\n')
text.insert(INSERT, '3. Repeat step 1 and 2 if you want to view the cropped image in both condition\n\n')
text.insert(INSERT, '4. Cropped image with changed condition will be saved automatically\n\n')

# this line will display a clickable button
darken = Button(top, text = "Darken",activeforeground = "black",activebackground = '#ed92b6', pady=10, padx=10,command = darken)  
blur = Button(top, text = "Blur",activeforeground = "black",activebackground = '#a4d3eb', pady=10, padx=15, command = blur)

darken.pack(side = BOTTOM)    
blur.pack(side = BOTTOM)

text.pack()
top.mainloop()  

cv.waitKey(0)