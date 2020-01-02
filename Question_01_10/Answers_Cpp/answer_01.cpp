/*
 * Question 01 : 通道变换 
 * Created by Harrytsz 2021-1-2
 */
#include <iostream>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  

using namespace cv;

Mat RGB2BGR(Mat img) {
	// get height and width
	int height = img.rows;
	int width = img.cols;

	// prepare output
	Mat out = Mat::zeros(height, width, CV_8UC3);
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			// R -> B
			out.at<Vec3b>(y, x)[0] = img.at<Vec3b>(y, x)[2];
			// G -> G
			out.at<Vec3b>(y, x)[1] = img.at<Vec3b>(y, x)[1];
			// B -> R
			out.at<Vec3b>(y, x)[2] = img.at<Vec3b>(y, x)[0];
		}
	}
	return out;
}


int main()
{
	// 读入一张图片（poyanghu缩小图）    
	Mat img = imread("imori.png");

	// 创建一个名为 "图片"窗口    
	namedWindow("图片");

	// 在窗口中显示图片   
	imshow("Origin", img);
	Mat out = RGB2BGR(img);
	imshow("Output", out);
	
	// Esc 键退出
	waitKey(0);
	destroyAllWindows();
	return 0;
}