##########################################
#    Question 02 : Grayscale(灰度化)
##########################################
import cv2 as cv
import numpy as np

# Target : gray scale
def BGR2GRAY(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    # Gray scale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)
    return out

# Read Image
img = cv.imread("./imori.jpg")
# Show & Save origin image
cv.imshow("Origin", img)
cv.imwrite("Origin_02.jpg", img)
# Gray scale
img = BGR2GRAY(img)
# Save result
cv.imwrite("Output_02.jpg", img)
cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()