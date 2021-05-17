# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageEnhance
import os
import cv2
import numpy as np
imageDir="D:/Subject experiment/Experiment 1_data augmentation/result/l=-4/source/" #要改变的图片的路径文件夹
saveDir="D:/Subject experiment/Experiment 1_data augmentation/result/l=-4/presolve/flip/"   #要保存的图片的路径文件夹

def rotation(root_path, img_name):
  
    img = Image.open(os.path.join(root_path, img_name))
    
    rotation_img = img.rotate(270) #旋转角度
    # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
    return rotation_img

i=0
for name in os.listdir(imageDir):
    i=i+1
    saveName="angle="+str(i)+"度.jpg"
    saveImage=rotation(imageDir,name)
    saveImage.save(os.path.join(saveDir,saveName))
