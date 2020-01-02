##########################################
#    Question 03 : Thresholding(二值化)
##########################################
import cv2 as cv
import numpy as np

# Target : Gray scale
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)
    return out

# Binaryzation
def binaryzation(grayImage, thresholding=128):
    grayImage[grayImage < thresholding] = 0
    grayImage[grayImage >= thresholding] = 255
    return grayImage

# Read Image
img = cv.imread("./imori.jpg")

# Show & Save origin image
cv.imshow("Origin", img)
cv.imwrite("Origin_03.jpg", img)

# Gray scale
grayImg = BGR2GRAY(img)

# Binaryzation
out = binaryzation(grayImg)

# Save result
cv.imwrite("Output_03.jpg", out)
cv.imshow("Result", out)

# Esc exit
cv.waitKey(0)
cv.destroyAllWindows()