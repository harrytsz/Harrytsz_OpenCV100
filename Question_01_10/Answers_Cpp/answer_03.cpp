/*
 * Question 03 : Thresholding(二值化) 
 * Created by Harrytsz 2021-1-2
 */
#include <iostream>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  

using namespace cv;

Mat BGR2GRAY(Mat img) {
	// get height and width
	int height = img.rows;
	int width = img.cols;
	// prepare output
	Mat out = Mat::zeros(height, width, CV_8UC1);
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			// BGR -> GRAY
			out.at<uchar>(y, x) = 0.2126 * (float)img.at<Vec3b>(y, x)[2] \
				+ 0.7152 * (float)img.at<Vec3b>(y, x)[1] \
				+ 0.0722 * (float)img.at<Vec3b>(y, x)[0];
		}
	}
	return out;
}

//  Binaryzation
Mat Binaryzation(Mat grayImg, int thresholding=128) {
	// get height and width
	int height = grayImg.rows;
	int width = grayImg.cols;

	// Prepare output
	Mat out = Mat::zeros(height, width, CV_8UC1);

	// Thresholding
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			// compare with thresholding
			if (grayImg.at<uchar>(y, x) < thresholding) out.at<uchar>(y, x) = 0;
			else out.at<uchar>(y, x) = 255;
		}
	}
	return out;
}


int main()
{
	// Read image    
	Mat img = imread("imori.png");    
	namedWindow("Images");

	// Show Origin image
	imshow("Origin", img);
	imwrite("Origin_03_cpp.jpg", img);

	// Run operation
	Mat grayImg = BGR2GRAY(img);

	// Binaryzation
	Mat out = Binaryzation(grayImg);

	// Show output image
	imshow("Output", out);
	imwrite("Output_03_cpp.jpg", out);

	// Esc exit
	waitKey(0);
	destroyAllWindows();
	return 0;
}