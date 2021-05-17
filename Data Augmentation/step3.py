# -*- coding: utf-8 -*-
#用于实现图片的任意角度旋转并且实现白色填充,但尺度变化问题未解决

import cv2
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
img = cv2.imread("D:/Subject experiment/Experiment 1_data augmentation/result/l=-4/source/l_gray=-4.jpg")
#当文件名含中文时会对cv2读取数据造成影响，解决方式如下：
#img = cv2.imdecode(np.fromfile("D:/Subject experiment/Experiment 1_data augmentation/result/l=-4/source/l_gray=-4.jpg",dtype=np.uint8),-1)   
angle=330
imgRotation = rotate_bound_white_bg(img,angle)
#scipy.misc.toimage(imgRotation, cmin=0.0, cmax=255).save('outfile2.jpg')
scipy.misc.imsave('D:/Subject experiment/Experiment 1_data augmentation/result/l=-4/presolve/rotation/'+'modenum_4旋转'+str(angle)+'度.jpg', imgRotation)
#  cv2.imshow("img",img) 
#  cv2.imshow("imgRotation",imgRotation)
cv2.waitKey(0)
