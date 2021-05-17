# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:28:15 2019

@author: lenovo
"""

# -*- coding: utf-8 -*-
#对比度、亮度增强,需手动该改1处


from PIL import Image
from PIL import ImageEnhance
import os
import shutil   #批量文件复制

mode_num=4


#目录自己改一下即可
path = ("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/rotation/"%mode_num)   #there are many directories
if not os.path.exists("D:/Subject experiment/total_data_improve/l=%d/"%mode_num):
       os.makedirs("D:/Subject experiment/total_data_improve/l=%d/"%mode_num)
       
new_path =("D:/Subject experiment/total_data_improve/l=%d/"%mode_num)

#mode_num=4
#img = cv2.imread("D:/Subject experiment/Experiment 1_data augmentation/result/l=%d/source/l_gray=%d.jpg"%(mode_num,mode_num))
#
#hist=cv2.calcHist([img],[0],None,[256],[0,256])

if not os.path.exists("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/contrastEnhancement/"%mode_num):
       os.makedirs("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/contrastEnhancement/"%mode_num)
       
if not os.path.exists("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/brightnessEnhancement/"%mode_num):
       os.makedirs("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/brightnessEnhancement/"%mode_num)

if not os.path.exists("D:/Subject experiment/total_data_improve/l=%d/"%mode_num):
       os.makedirs("D:/Subject experiment/total_data_improve/l=%d/"%mode_num)
       
imageDir=("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/rotation/"%mode_num) #要改变的图片的路径文件夹
saveDir=("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/contrastEnhancement/"%mode_num)   #要保存的图片的路径文件夹
saveDir1=("D:/Subject experiment/Experiment 1_data augmentation/result_improve/l=%d/presolve/brightnessEnhancement/"%mode_num)   #要保存的图片的路径文件夹
saveDir2=("D:/Subject experiment/total_data_improve/l=%d/"%mode_num)

def contrastEnhancement(root_path,img_name):#对比度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_con = ImageEnhance.Contrast(image)
    contrast = 5
    image_contrasted = enh_con.enhance(contrast)
    return image_contrasted

def brightnessEnhancement(root_path,img_name):#亮度增强
    image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    brightness = 3
    image_brightened = enh_bri.enhance(brightness)
    return image_brightened

i=0
for name in os.listdir(imageDir):
    i=i+1
    saveName="mode_num_"+str(mode_num)+"_"+str(i)+"contrast.jpg"
    saveName1="mode_num_"+str(mode_num)+"_"+str(i)+"brightness.jpg"
    
    saveImage=contrastEnhancement(imageDir,name)
    saveImage.save(os.path.join(saveDir,saveName))
    
    saveImage.save(os.path.join(saveDir2,saveName))
    
    saveImage1=brightnessEnhancement(imageDir,name)
    saveImage1.save(os.path.join(saveDir1,saveName1))
    
    saveImage1.save(os.path.join(saveDir2,saveName1))
    
count = 0
for file in os.listdir(path):
    full_file = os.path.join(path, file)
    new_full_file = os.path.join(new_path, file)
    shutil.copy(full_file, new_full_file)
#    
#    if count == 100:
#        print("done!")
#        break
    count += 1

#print("complete!")
