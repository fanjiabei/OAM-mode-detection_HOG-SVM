# -*- coding: utf-8 -*-
#step3step4的改进，尝试消除尺度问题，添加循环,需手动改的地方有两处：mode_num赋值以及 scipy.misc.imsave路径中
import os
import cv2
from math import *
import numpy as np
import scipy.misc

class BBox(object):

    def __init__(self, bbox):
        self.left = bbox[0]
        self.top = bbox[1]
        self.right = bbox[2]
        self.bottom = bbox[3]
        # 旋转angle角度，缺失背景白色（255, 255, 255）填充
def rotate_bound_white_bg(image,angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    #    (cX, cY) = (w / 2, h / 2)
    box = [0, 0, w, h]
    bbox = BBox(box)
    center = ((bbox.left + bbox.right) / 2, (bbox.top + bbox.bottom) / 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    # -angle位置参数为角度参数负值表示顺时针旋转; 1.0位置参数scale是调整尺寸比例（图像缩放参数），建议0.75
    M = cv2.getRotationMatrix2D(center, -angle, 1)

    # perform the actual rotation and return the image
    # borderValue 缺失背景填充色彩，此处为白色，可自定义
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]),borderValue=(255,255,255))
    # borderValue 缺省，默认是黑色（0, 0 , 0）
    # return cv2.warpAffine(image, M, (nW, nH))

mode_num=4

img = cv2.imread("D:/CODE/Segmentation_dataset/ucagenoam/-1.jpg")
#(D:/Subject experiment/test/data/source/l=%d.jpg"%(mode_num))
#img = cv2.imread("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/source/l_gray=%d.jpg"%(mode_num,mode_num))
#img = cv2.imdecode(np.fromfile("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=-4/source/l_gray=-4.jpg",dtype=np.uint8),-1)   
angle=30
i=1
for i in range(12):
 imgRotation = rotate_bound_white_bg(img,angle)
#scipy.misc.toimage(imgRotation, cmin=0.0, cmax=255).save('outfile2.jpg')
# scipy.misc.imsave('D:/Subject experiment/test/data/l=4/'+'rgbmodenum_'+str(mode_num)+'_rotate'+str(angle)+'°.jpg', imgRotation)
# scipy.misc.imsave('D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=4/presolve/rotation/'+'modenum_'+str(mode_num)+'_rotate'+str(angle)+'°.jpg', imgRotation)
 angle=30+i*30
#  cv2.imshow("img",img) 
 cv2.imshow("imgRotation",imgRotation)
 cv2.waitKey(0)
