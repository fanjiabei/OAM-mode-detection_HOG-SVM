# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:08:04 2019

@author: lenovo
"""
######实现指定文件夹批量处理图片（重命名）并copy到指定文件夹中，需修改模式数文件夹名称
import os
import shutil


#for num in range(100,1001,100):
#    path = ("D:/Subject experiment/OAMimage/dis%d/l=4/"%(num))#
#    new_path = ("D:/CODE/OAMimage/modenum_4/")#
#    count = os.listdir(path)
#    plus=int(((num-100)/100)*60)
#    for j in range(1,len(count)+1):#for j in range(1,len(count)+1):
#    #    for root, dirs, files in os.walk(path):
#    #        if len(dirs) == 0:
#    #            for i in range(len(files)):
#    #                print("i=",i)
#    #                if files[i].find('label.jpg')!=-1:
##                        shutil.copy(os.path.join(path+str(j)+'.jpg'), os.path.join(new_path+str(j+plus)+'.jpg'))
##                         print(j+plus)

#for num in range(100,1001,100):
path = ("D:/CODE/OAMdataset/paper/image/l7=-1/")#D:/Subject experiment/OAMimage/dis%d/l=4
new_path = ("D:/CODE/OAMdataset/OAMimage_original/-1/")#D:/CODE/OAMimage/modenum_4/
count = os.listdir(path)
plus=1080
for j in range(1,len(count)+1):#for j in range(1,len(count)+1):
#    for root, dirs, files in os.walk(path):
#        if len(dirs) == 0:
#            for i in range(len(files)):
#                print("i=",i)
#                if files[i].find('label.jpg')!=-1:
#                        shutil.copy(os.path.join(path+str(j)+'.jpg'), os.path.join(new_path+str(j+plus)+'.jpg'))
                    shutil.copy(os.path.join(path+str(j)+'.jpg'), os.path.join(new_path+str(j+plus)+'.jpg'))
#                        