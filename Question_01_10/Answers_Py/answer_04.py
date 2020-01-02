##########################################
#    Question 04 : Otsu Binaryzation Method(大津二值化算法)
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
def Binaryzation(grayImage, thresholding=128):
    grayImage[grayImage < thresholding] = 0
    grayImage[grayImage >= thresholding] = 255
    return grayImage

# Otsu Binaryzation
def OtsuBinaryzation(img, th=128):
    max_sigma = 0
    max_t = 0

    # Detemine threshold
    for _t in range(1, 255):
        v0 = img[np.where(img < _t)]
        m0 = np.mean(v0) if len(v0) > 0 else 0
        w0 = len(v0) / (H * W)
        v1 = img[np.where(img >= _t)]
        m1 = np.mean(v1) if len(v1) > 0 else 0
        w1 = len(v1) / (H * W)
        sigma = w0 * w1 * ((m0 - m1)**2)
        if sigma > max_sigma:
            max_sigma = sigma
            max_t = _t
    return max_t # 输出最优二值化阈值


# Read Image
img = cv.imread("./imori.jpg")
H, W, C = img.shape

# Show & Save origin image
cv.imshow("Origin", img)
cv.imwrite("Origin_04.jpg", img)

# Gray scale
grayImg = BGR2GRAY(img)

# Otsu Binaryzation
max_t = OtsuBinaryzation(grayImg)
print(max_t) # max_t = 127
# Binaryzation
out = Binaryzation(grayImg, max_t)

# Save result
cv.imwrite("Output_04.jpg", out)
cv.imshow("Result", out)

# Esc exit
cv.waitKey(0)
cv.destroyAllWindows()