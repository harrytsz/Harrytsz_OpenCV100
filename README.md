# Harrytsz_OpenCV100
OpenCV 100 questions answer

(画像処理100本ノック)[https://github.com/yoyoyo-yo/Gasyori100knock]

## [Tutorial](Tutorial)

|      |      内容      |         Python          |                   C++                   | JavaScript |
| :--: | :------------: | :---------------------: | :-------------------------------------: | ---------- |
|  1   |      安装      |      [✓](Tutorial)      | [✓](Tutoria/README_opencv_c_install.md) |            |
|  2   | 读取、显示图像 | [✓](Tutorial/README.md) | [✓](Tutoria/README_opencv_c_install.md) |            |
|  3   |    操作像素    | [✓](Tutorial/README.md) | [✓](Tutoria/README_opencv_c_install.md) |            |
|  4   |    拷贝图像    | [✓](Tutorial/README.md) | [✓](Tutoria/README_opencv_c_install.md) |            |
|  5   |    保存图像    | [✓](Tutorial/README.md) | [✓](Tutoria/README_opencv_c_install.md) |            |
|  6   |    练习问题    | [✓](Tutorial/README.md) | [✓](Tutoria/README_opencv_c_install.md) |            |

[Matplotlib和OpenCV的Tips](Image_processing_tips.ipynb)

## 问题

详细的问题请参见各页面下的`README`文件（各个页面下滑就可以看见）。
- 为了简化答案，所以没有编写`main()`函数。
- 虽然我们的答案以`numpy`为基础，但是还请你自己查找`numpy`的基本使用方法。

### [问题1 - 10](Question_01_10/README.md)

| 序号 |                            问题                             |                  Python                  |                      C++                      | 翻译一校 |
| :--: | :---------------------------------------------------------: | :--------------------------------------: | :-------------------------------------------: | :------: |
|  1   |            [通道替换](Question_01_10/README.md)             | [✓](Question_01_10/answers/answer_1.py)  | [✓](Question_01_10/answers_cpp/answer_1.cpp)  |    ✓     |
|  2   |       [灰度化（Grayscale）](Question_01_10/README.md)       | [✓](Question_01_10/answers/answer_2.py)  | [✓](Question_01_10/answers_cpp/answer_2.cpp)  |    ✓     |
|  3   |     [二值化（Thresholding）](Question_01_10/README.md)      | [✓](Question_01_10/answers/answer_3.py)  | [✓](Question_01_10/answers_cpp/answer_3.cpp)  |    ✓     |
|  4   | [大津二值化算法（Otsu's Method）](Question_01_10/README.md) | [✓](Question_01_10/answers/answer_4.py)  | [✓](Question_01_10/answers_cpp/answer_4.cpp)  |    ✓     |
|  5   |        [$\text{HSV}$变换](Question_01_10/README.md)         | [✓](Question_01_10/answers/answer_5.py)  | [✓](Question_01_10/answers_cpp/answer_5.cpp)  |    ✓     |
|  6   |            [减色处理](Question_01_10/README.md)             | [✓](Question_01_10/answers/answer_6.py)  | [✓](Question_01_10/answers_cpp/answer_6.cpp)  |    ✓     |
|  7   |   [平均池化（Average Pooling）](Question_01_10/README.md)   | [✓](Question_01_10/answers/answer_7.py)  | [✓](Question_01_10/answers_cpp/answer_7.cpp)  |    ✓     |
|  8   |     [最大池化（Max Pooling）](Question_01_10/README.md)     | [✓](Question_01_10/answers/answer_8.py)  | [✓](Question_01_10/answers_cpp/answer_8.cpp)  |    ✓     |
|  9   |   [高斯滤波（Gaussian Filter）](Question_01_10/README.md)   | [✓](Question_01_10/answers/answer_9.py)  | [✓](Question_01_10/answers_cpp/answer_9.cpp)  |    ✓     |
|  10  |    [中值滤波（Median Filter）](Question_01_10/README.md)    | [✓](Question_01_10/answers/answer_10.py) | [✓](Question_01_10/answers_cpp/answer_10.cpp) |    ✓     |

### [问题11 - 20](Question_11_20/README.md)

| 序号 |                             内容                             | Python                                   | C++                                          | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | -------------------------------------------- | :------: |
|  11  |            [均值滤波器](Question_11_20/README.md)            | [✓](Question_11_20/answers/answer_1.py)  | [✓](Question_11_20/answers_cpp/answer_1.cpp) |    ✓     |
|  12  |          [Motion Filter](Question_11_20/README.md)           | [✓](Question_11_20/answers/answer_2.py)  | [✓](Question_11_20/answers_cpp/answer_2.cpp) |    ✓     |
|  13  |          [MAX-MIN滤波器](Question_11_20/README.md)           | [✓](Question_11_20/answers/answer_3.py)  | [✓](Question_11_20/answers_cpp/answer_3.cpp) |    ✓     |
|  14  | [差分滤波器（Differential Filter）](Question_11_20/README.md) | [✓](Question_11_20/answers/answer_4.py)  | [✓](Question_11_20/answers_cpp/answer_4.cpp) |    ✓     |
|  15  |           [Sobel滤波器](Question_11_20/README.md)            | [✓](Question_11_20/answers/answer_5.py)  | [✓](Question_11_20/answers_cpp/answer_5.cpp) |    ✓     |
|  16  |          [Prewitt滤波器](Question_11_20/README.md)           | [✓](Question_11_20/answers/answer_6.py)  | [✓](Question_11_20/answers_cpp/answer_6.cpp) |    ✓     |
|  17  |         [Laplacian滤波器](Question_11_20/README.md)          | [✓](Question_11_20/answers/answer_7.py)  | [✓](Question_11_20/answers_cpp/answer_7.cpp) |    ✓     |
|  18  |           [Emboss滤波器](Question_11_20/README.md)           | [✓](Question_11_20/answers/answer_8.py)  | [✓](Question_11_20/answers_cpp/answer_8.cpp) |    ✓     |
|  19  |            [LoG滤波器](Question_11_20/README.md)             | [✓](Question_11_20/answers/answer_9.py)  | [✓](Question_11_20/answers_cpp/answer_9.cpp) |    ✓     |
|  20  |        [直方图](Question_01_10/answers/answer_10.py)         | [✓](Question_11_20/answers/answer_10.py) |                                              |    ✓     |

### [问题21-30](Question_21_30/README.md)

| 序号 |                             内容                             | Python                                   | C++                                           | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | --------------------------------------------- | :------: |
|  21  | [直方图归一化（Histogram Normalization）](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_1.py)  | [✓](Question_21_30/answers_cpp/answer_1.cpp)  |          |
|  22  |            [直方图操作](Question_21_30/README.md)            | [✓](Question_21_30/answers/answer_2.py)  | [✓](Question_21_30/answers_cpp/answer_2.cpp)  |          |
|  23  | [直方图均衡化（Histogram Equalization）](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_3.py)  | [✓](Question_21_30/answers_cpp/answer_3.cpp)  |          |
|  24  |   [伽玛校正（Gamma Correction）](Question_21_30/README.md)   | [✓](Question_21_30/answers/answer_4.py)  | [✓](Question_21_30/answers_cpp/answer_4.cpp)  |          |
|  25  | [最邻近插值（Nearest-neighbor Interpolation）](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_5.py)  | [✓](Question_21_30/answers_cpp/answer_5.cpp)  |          |
|  26  | [双线性插值（Bilinear Interpolation）](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_6.py)  | [✓](Question_21_30/answers_cpp/answer_6.cpp)  |          |
|  27  | [双三次插值（Bicubic Interpolation）](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_7.py)  | [✓](Question_21_30/answers_cpp/answer_7.cpp)  |          |
|  28  | [仿射变换（Afine Transformations）——平行移动](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_8.py)  | [✓](Question_21_30/answers_cpp/answer_8.cpp)  |          |
|  29  | [仿射变换（Afine Transformations）——放大缩小](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_9.py)  | [✓](Question_21_30/answers_cpp/answer_9.cpp)  |          |
|  30  | [仿射变换（ Afine Transformations ）——旋转](Question_21_30/README.md) | [✓](Question_21_30/answers/answer_10.py) | [✓](Question_21_30/answers_cpp/answer_10.cpp) |          |

### [问题31-40](Question_31_40/README.md)
| 序号 |                             内容                             | Python                                   | C++                                           | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | --------------------------------------------- | :------: |
|  31  | [仿射变换（Afine Transformations）——倾斜](Question_31_40/README.md) | [✓](Question_31-40/answers/answer_1.py)  | [✓](Question_31-40/answers_cpp/answer_1.cpp)  |          |
|  32  | [傅立叶变换（Fourier Transform）](Question_31_40/README.md)  | [✓](Question_31-40/answers/answer_2.py)  | [✓](Question_31-40/answers_cpp/answer_2.cpp)  |          |
|  33  |       [傅立叶变换——低通滤波](Question_31_40/README.md)       | [✓](Question_31-40/answers/answer_3.py)  | [✓](Question_31-40/answers_cpp/answer_3.cpp)  |          |
|  34  |       [傅立叶变换——高通滤波](Question_31_40/README.md)       | [✓](Question_31-40/answers/answer_4.py)  | [✓](Question_31-40/answers_cpp/answer_4.cpp)  |          |
|  35  |       [傅立叶变换——带通滤波](Question_31_40/README.md)       | [✓](Question_31-40/answers/answer_5.py)  | [✓](Question_31-40/answers_cpp/answer_5.cpp)  |          |
|  36  | [JPEG 压缩——第一步：离散余弦变换（Discrete Cosine Transformation）](Question_31_40/README.md) | [✓](Question_31-40/answers/answer_6.py)  | [✓](Question_31-40/answers_cpp/answer_6.cpp)  |          |
|  37  | [峰值信噪比（Peak Signal to Noise Ratio）](Question_31_40/README.md) | [✓](Question_31-40/answers/answer_7.py)  | [✓](Question_31-40/answers_cpp/answer_7.cpp)  |          |
|  38  | [JPEG 压缩——第二步：离散余弦变换+量化](Question_31_40/README.md) | [✓](Question_31-40/answers/answer_8.py)  | [✓](Question_31-40/answers_cpp/answer_8.cpp)  |          |
|  39  | [JPEG 压缩——第三步：YCbCr 色彩空间](Question_31_40/README.md) | [✓](Question_31-40/answers/answer_9.py)  | [✓](Question_31-40/answers_cpp/answer_9.cpp)  |          |
|  40  | [JPEG 压缩——第四步：YCbCr+DCT+量化](Question_31_40/README.md) | [✓](Question_31-40/answers/answer_10.py) | [✓](Question_31-40/answers_cpp/answer_10.cpp) |          |

### [问题41-50](Question_41_50/README.md)

| 序号 |                             内容                             | Python                                   | C++                                           | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | --------------------------------------------- | :------: |
|  41  | [`Canny`边缘检测：第一步——边缘强度](Question_41_50/README.md) | [✓](Question_41-50/answers/answer_1.py)  | [✓](Question_41-50/answers_cpp/answer_1.cpp)  |          |
|  42  | [`Canny`边缘检测：第二步——边缘细化](Question_41_50/README.md) | [✓](Question_41-50/answers/answer_2.py)  | [✓](Question_41-50/answers_cpp/answer_2.cpp)  |          |
|  43  | [`Canny`边缘检测：第三步——滞后阈值](Question_41_50/README.md) | [✓](Question_41-50/answers/answer_3.py)  | [✓](Question_41-50/answers_cpp/answer_3.cpp)  |          |
|  44  | [霍夫变换（Hough Transform）／直线检测——第一步：霍夫变换](Question_41_50/README.md) | [✓](Question_41-50/answers/answer_4.py)  | [✓](Question_41-50/answers_cpp/answer_4.cpp)  |          |
|  45  | [霍夫变换（Hough Transform）／直线检测——第二步：NMS](Question_41_50/README.md) | [✓](Question_41-50/answers/answer_5.py)  | [✓](Question_41-50/answers_cpp/answer_5.cpp)  |          |
|  46  | [霍夫变换（Hough Transform）／直线检测——第三步：霍夫逆变换](Question_41_50/README.md) | [✓](Question_41-50/answers/answer_6.py)  | [✓](Question_41-50/answers_cpp/answer_6.cpp)  |          |
|  47  |    [形态学处理：膨胀（Dilate）](Question_41_50/README.md)    | [✓](Question_41-50/answers/answer_7.py)  | [✓](Question_41-50/answers_cpp/answer_7.cpp)  |          |
|  48  |    [形态学处理：腐蚀（Erode）](Question_41_50/README.md)     | [✓](Question_41-50/answers/answer_8.py)  | [✓](Question_41-50/answers_cpp/answer_8.cpp)  |          |
|  49  |   [开运算（Opening Operation）](Question_41_50/README.md)    | [✓](Question_41-50/answers/answer_9.py)  | [✓](Question_41-50/answers_cpp/answer_9.cpp)  |          |
|  50  |   [闭运算（Closing Operation）](Question_41_50/README.md)    | [✓](Question_41-50/answers/answer_10.py) | [✓](Question_41-50/answers_cpp/answer_10.cpp) |          |

### [问题51-60](Question_51_60/README.md)

| 序号 |                             内容                             | Python                                   | C++  | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | ---- | :------: |
|  51  | [形态学梯度（Morphology Gradient）](Question_51_60/README.md) | [✓](Question_51-60/answers/answer_1.py)  |      |          |
|  52  |         [顶帽（Top Hat）](Question_51_60/README.md)          | [✓](Question_51-60/answers/answer_2.py)  |      |          |
|  53  |        [黑帽（Black Hat）](Question_51_60/README.md)         | [✓](Question_51-60/answers/answer_3.py)  |      |          |
|  54  | [使用误差平方和算法（Sum of Squared Difference）进行模式匹配（Template Matching）](Question_51_60/README.md) | [✓](Question_51-60/answers/answer_4.py)  |      |          |
|  55  | [使用绝对值差和（Sum of Absolute Differences）进行模式匹配](Question_51_60/README.md) | [✓](Question_51-60/answers/answer_5.py)  |      |          |
|  56  | [使用归一化交叉相关（Normalization Cross Correlation）进行模式匹配](Question_51_60/README.md) | [✓](Question_51-60/answers/answer_6.py)  |      |          |
|  57  | [使用零均值归一化交叉相关（Zero-mean Normalization Cross Correlation）进行模式匹配](Question_51_60/README.md) | [✓](Question_51-60/answers/answer_7.py)  |      |          |
|  58  |        [$4-$邻域连通域标记](Question_51_60/README.md)        | [✓](Question_51-60/answers/answer_8.py)  |      |          |
|  59  |        [$8-$邻域连通域标记](Question_51_60/README.md)        | [✓](Question_51-60/answers/answer_9.py)  |      |          |
|  60  |    [透明混合（Alpha Blending）](Question_51_60/README.md)    | [✓](Question_51-60/answers/answer_10.py) |      |          |

### [问题61-70](Question_61_70/README.md)

| 序号 |                             内容                             | Python                                   | C++  | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | ---- | :------: |
|  61  |            [$4-$连接数](Question_61_70/README.md)            | [✓](Question_61-70/answers/answer_1.py)  |      |          |
|  62  |            [$8-$连接数](Question_61_70/README.md)            | [✓](Question_61-70/answers/answer_2.py)  |      |          |
|  63  |             [细化处理](Question_61_70/README.md)             | [✓](Question_61-70/answers/answer_3.py)  |      |          |
|  64  |        [Hilditch 细化算法](Question_61_70/README.md)         |                                          |      |          |
|  65  |       [Zhang-Suen 细化算法](Question_61_70/README.md)        | [✓](Question_61-70/answers/answer_5.py)  |      |          |
|  66  | [方向梯度直方图（HOG）第一步：梯度幅值・梯度方向](Question_61_70/README.md) | [✓](Question_61-70/answers/answer_6.py)  |      |          |
|  67  | [方向梯度直方图（HOG）第二步：梯度直方图](Question_61_70/README.md) | [✓](Question_61-70/answers/answer_7.py)  |      |          |
|  68  | [方向梯度直方图（HOG）第三步：直方图归一化](Question_61_70/README.md) | [✓](Question_61-70/answers/answer_8.py)  |      |          |
|  69  | [方向梯度直方图（HOG）第四步：可视化特征量](Question_61_70/README.md) | [✓](Question_61-70/answers/answer_9.py)  |      |          |
|  70  |    [色彩追踪（Color Tracking）](Question_61_70/README.md)    | [✓](Question_61-70/answers/answer_10.py) |      |          |
### [问题71-80](Question_71_80/README.md)

| 序号 |                             内容                             | Python                                   | C++  | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | ---- | :------: |
|  71  |         [掩膜（Masking）](Question_71_80/README.md)          | [✓](Question_71-80/answers/answer_1.py)  |      |          |
|  72  | [掩膜（色彩追踪（Color Tracking）+形态学处理）](Question_71_80/README.md) | [✓](Question_71-80/answers/answer_2.py)  |      |          |
|  73  |            [缩小和放大](Question_71_80/README.md)            | [✓](Question_71-80/answers/answer_3.py)  |      |          |
|  74  |    [使用差分金字塔提取高频成分](Question_71_80/README.md)    | [✓](Question_71-80/answers/answer_4.py)  |      |          |
|  75  |  [高斯金字塔（Gaussian Pyramid）](Question_71_80/README.md)  | [✓](Question_71-80/answers/answer_5.py)  |      |          |
|  76  |      [显著图（Saliency Map）](Question_71_80/README.md)      | [✓](Question_71-80/answers/answer_6.py)  |      |          |
|  77  |   [Gabor 滤波器（Gabor Filter）](Question_71_80/README.md)   | [✓](Question_71-80/answers/answer_7.py)  |      |          |
|  78  |        [旋转 Gabor 滤波器](Question_71_80/README.md)         | [✓](Question_71-80/answers/answer_8.py)  |      |          |
|  79  |  [使用 Gabor 滤波器进行边缘检测](Question_71_80/README.md)   | [✓](Question_71-80/answers/answer_9.py)  |      |          |
|  80  |  [使用 Gabor 滤波器进行特征提取](Question_71_80/README.md)   | [✓](Question_71-80/answers/answer_10.py) |      |          |

### [问题81-90](Question_81_90/README.md)

| 序号 |                             内容                             | Python                                   | C++  | 翻译一校 |
| :--: | :----------------------------------------------------------: | ---------------------------------------- | ---- | :------: |
|  81  |         [Hessian 角点检测](Question_81_90/README.md)         | [✓](Question_81-90/answers/answer_1.py)  |      |          |
|  82  | [Harris 角点检测第一步：Sobel + Gausian](Question_81_90/README.md) | [✓](Question_81-90/answers/answer_2.py)  |      |          |
|  83  | [Harris 角点检测第二步：角点检测](Question_81_90/README.md)  | [✓](Question_81-90/answers/answer_3.py)  |      |          |
|  84  | [简单图像识别第一步：减色化+直方图](Question_81_90/README.md) | [✓](Question_81-90/answers/answer_4.py)  |      |          |
|  85  |   [简单图像识别第二步：判别类别](Question_81_90/README.md)   | [✓](Question_81-90/answers/answer_5.py)  |      |          |
|  86  |     [简单图像识别第三步：评估](Question_81_90/README.md)     | [✓](Question_81-90/answers/answer_6.py)  |      |          |
|  87  |     [简单图像识别第四步：k-NN](Question_81_90/README.md)     | [✓](Question_81-90/answers/answer_7.py)  |      |          |
|  88  | [k-平均聚类算法（k -means Clustering）第一步：生成质心](Question_81_90/README.md) | [✓](Question_81-90/answers/answer_8.py)  |      |          |
|  89  | [k-平均聚类算法（k -means Clustering）第二步：聚类](Question_81_90/README.md) | [✓](Question_81-90/answers/answer_9.py)  |      |          |
|  90  | [k-平均聚类算法（k -means Clustering）第三步：调整初期类别](Question_81_90/README.md) | [✓](Question_81-90/answers/answer_10.py) |      |          |

### [问题91-100](Question_91_100/README.md)

| 序号 |                             内容                             |                  Python                   | C++  | 翻译一校 |
| :--: | :----------------------------------------------------------: | :---------------------------------------: | ---- | :------: |
|  91  | [利用 k-平均聚类算法进行减色处理第一步：按颜色距离分类](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_1.py)  |      |          |
|  92  | [利用 k-平均聚类算法进行减色处理第二步：减色处理](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_2.py)  |      |          |
|  93  | [准备机器学习的训练数据第一步：计算 IoU](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_3.py)  |      |          |
|  94  | [准备机器学习的训练数据第一步：随机裁剪（Random Cropping）](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_4.py)  |      |          |
|  95  | [神经网络（Neural Network）第一步：深度学习（Deep Learning）](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_5.py)  |      |          |
|  96  | [神经网络（Neural Network）第二步：训练](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_6.py)  |      |          |
|  97  | [简单物体检测第一步----滑动窗口（Sliding Window）+HOG](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_7.py)  |      |          |
|  98  | [简单物体检测第二步----滑动窗口（Sliding Window）+ NN](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_8.py)  |      |          |
|  99  | [简单物体检测第三步----非极大值抑制（Non-Maximum Suppression）](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_9.py)  |      |          |
| 100  | [简单物体检测第三步----评估 Precision, Recall, F-score, mAP](Question_91_100/README.md) | [✓](Question_91-100/answers/answer_10.py) |      |          |
## TODO

adaptivebinalizatino, poison image blending
## Citation

```bash
@article{Harrytsz_OpenCV100,
    Author = {Harrytsz},
    Title = {OpenCV100},
    Journal = {https://github.com/harrytsz/Harrytsz_OpenCV100},
    Year = {2020}
}
```

## License

&copy; Harrytsz All Rights Reserved.

This is under MIT License.

