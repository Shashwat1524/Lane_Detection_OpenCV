import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(image):
    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    #Gaussian Blur
    #Kernel Convolution
    blur=cv2.GaussianBlur(gray,(5,5),0)
    #Canny function
    canny=cv2.Canny(blur,50,150)
    return canny

def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([
        [(200,height),(1100,height),(550,250)]])
    mask=np.zeros_like(image)
    #creates zeros same dimension as corresponding arrays
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image


image=cv2.imread('test_image.jpg')
# cv2.imshow('Lane Image',image)
lane_image=np.copy(image)
canny=canny(lane_image)
cropped_image=region_of_interest(canny)
cv2.imshow("Result",cropped_image)
cv2.waitKey(10000)

#Edge is detected by rapid change in Brightness
