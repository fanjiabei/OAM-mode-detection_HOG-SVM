# -*- coding: utf-8 -*-
#u盘路径图像增强 整合 旋转已无需再手动改动代码
import os
import cv2
import scipy.misc
from PIL import Image
from PIL import ImageEnhance

#######旋转
class BBox(object):

    def __init__(self, bbox):
        self.left = bbox[0]
        self.top = bbox[1]
        self.right = bbox[2]
        self.bottom = bbox[3]
        
def path(mode_num):
    if not os.path.exists("D:/CODE/OAMdataset/paper/image/l7=%d/"%mode_num):
       os.makedirs("D:/CODE/OAMdataset/paper/image/l7=%d/"%mode_num)
    return 0
        # 旋转angle角度，缺失背景白色（255, 255, 255）填充
def rotate_bound_white_bg(image,angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    #    (cX, cY) = (w / 2, h / 2)
    box = [0, 0, w, h]
    bbox = BBox(box)
    center = ((bbox.left + bbox.right) / 2, (bbox.top + bbox.bottom) / 2)
    # -angle位置参数为角度参数负值表示顺时针旋转; 1.0位置参数scale是调整尺寸比例（图像缩放参数），建议0.75
    M = cv2.getRotationMatrix2D(center, -angle, 1)
    # borderValue 缺失背景填充色彩，此处为白色，可自定义
    return cv2.warpAffine(image, M, (image.shape[1], image.shape[0]),borderValue=(255,255,255))
    # borderValue 缺省，默认是黑色（0, 0 , 0）
    # return cv2.warpAffine(image, M, (nW, nH))
######对比度增强 亮度 色度 锐度增强

def contrastEnhancement(root_path,img_name):#对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    contrast = 5.0
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 3.0
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened
def colorEnhancement(root_path,img_name):#色度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_col = ImageEnhance.Color(image)
    color = 1.5
    image_colored = enh_col.enhance(color)
    return image_colored
def sharpnessEnhancement(root_path,img_name):#锐度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharped = enh_sha.enhance(sharpness)
    return image_sharped
####下方旋转和四个角度图像增强可分两部分分别运行，无需手动改代码，唯一需要改的就是路径问题
mode_num =1
for mode_num in range (1,2):
      path(mode_num)
      img = cv2.imread("D:/CODE/OAMdataset/paper/%d/7.png"%(mode_num))
#            img = cv2.imread("F:/OAMimage/UCAgenoam/%d.jpg"%(mode_num))
      #img = cv2.imread("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/source/l_gray=%d.jpg"%(mode_num,mode_num))
      #img = cv2.imdecode(np.fromfile("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=-4/source/l_gray=-4.jpg",dtype=np.uint8),-1)   
      angle=30
      i=1
      count=1
      for i in range(12):
            
           imgRotation = rotate_bound_white_bg(img,angle)
          #scipy.misc.toimage(imgRotation, cmin=0.0, cmax=255).save('outfile2.jpg')
           scipy.misc.imsave(('D:/CODE/OAMdataset/paper/image/l7=%d/'%mode_num)+str(count)+'.jpg', imgRotation)
#           scipy.misc.imsave(('F:/OAMimage/UCAgenoam/l=%d/'%mode_num)+str(count)+'.jpg', imgRotation)
           count=count+1
           angle=30+i*30
           cv2.waitKey(0)
      imageDir=("D:/CODE/OAMdataset/paper/image/l7=%d/"%mode_num) #要改变的图片的路径文件夹
      saveDir=("D:/CODE/OAMdataset/paper/image/l7=%d/"%mode_num)
      num=13
      for name in os.listdir(imageDir):
            saveName1=str(num)+".jpg"
            saveName2=str(num+1)+".jpg"
            saveName3=str(num+2)+".jpg"
            saveName4=str(num+3)+".jpg"
            saveImage1=contrastEnhancement(imageDir,name)###对比度
            saveImage2=brightnessEnhancement(imageDir,name)###亮度
            saveImage3=colorEnhancement(imageDir,name)###色度
            saveImage4=sharpnessEnhancement(imageDir,name)###锐度
            
            saveImage1.save(os.path.join(saveDir,saveName1))
            saveImage2.save(os.path.join(saveDir,saveName2))
            saveImage3.save(os.path.join(saveDir,saveName3))
            saveImage4.save(os.path.join(saveDir,saveName4))
            num=num+4
            cv2.waitKey(0)

