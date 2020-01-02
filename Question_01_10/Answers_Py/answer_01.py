"""
    Question 01 : 通道交换
"""
import cv2 as cv

# Target : RGB -> BGR
def RGB2BGR(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    # RGB -> BGR
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b
    return img

# Read Image
img = cv.imread("./imori.jpg")
# Show & Save origin image
cv.imshow("Origin", img)
cv.imwrite("Origin.jpg", img)
# RGB -> BGR
img = RGB2BGR(img)
# Save result
cv.imwrite("Out.jpg", img)
cv.imshow("Result", img)
cv.waitKey(0)
cv.destroyAllWindows()