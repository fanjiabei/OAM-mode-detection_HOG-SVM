# -*- coding: utf-8 -*-

import os
 
def IsSubString(SubStrList,Str):
    flag=True
    for substr in SubStrList:
        if not(substr in Str):
            flag=False
    
    return flag
 
#扫面文件
def GetFileList(FindPath,FlagStr=[]):
    FileList=[]
    FileNames=os.listdir(FindPath)
    if len(FileNames)>0:
        for fn in FileNames:
            if len(FlagStr)>0:
                if IsSubString(FlagStr,fn):
                    fullfilename=os.path.join(FindPath,fn)
                    FileList.append(fullfilename)
            else:
                fullfilename=os.path.join(FindPath,fn)
                FileList.append(fullfilename)
    
    if len(FileList)>0:
        FileList.sort()
        
    return FileList
 
 
 
train_txt=open('train.txt','w')
#制作标签数据，多标签数据，编号从0开始
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/cabbage')#.py文件目录下
for img in imgfile:
    str1=img+' '+'0'+'\n'        #用空格代替转义字符 \t 
    train_txt.writelines(str1)
    
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/carrot')
for img in imgfile:
    str2=img+' '+'1'+'\n'
    train_txt.writelines(str2)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/cauliflower')
for img in imgfile:
    str3=img+' '+'2'+'\n'
    train_txt.writelines(str3)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/cucumber')
for img in imgfile:
    str4=img+' '+'3'+'\n'
    train_txt.writelines(str4)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/eggplant')
for img in imgfile:
    str5=img+' '+'4'+'\n'
    train_txt.writelines(str5)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/green_pepper')
for img in imgfile:
    str6=img+' '+'5'+'\n'
    train_txt.writelines(str6)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/potato')
for img in imgfile:
    str7=img+' '+'6'+'\n'
    train_txt.writelines(str7)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/pumpkin')
for img in imgfile:
    str8=img+' '+'7'+'\n'
    train_txt.writelines(str8)
 
 
imgfile=GetFileList('/home/aa/qxq/project/fruits/ncnn-master/data/train/tomato')
for img in imgfile:
    str9=img+' '+'8'+'\n'
    train_txt.writelines(str9)
 
#转换完成后，将.txt文档关闭
train_txt.close()
 
#测试集文件列表
#test_txt=open('val.txt','w')
#制作标签数据，如果是男的，标签设置为0，如果是女的标签为1
#imgfile=GetFileList('val/test_cat')#将数据集放在与.py文件相同目录下
#for img in imgfile:
#    str3=img+' '+'1'+'\n'
#    test_txt.writelines(str3)
    
 
#imgfile=GetFileList('val/test_dog')
#for img in imgfile:
#    str4=img+' '+'0'+'\n'
#    test_txt.writelines(str4)
#test_txt.close()
 
print("成功生成文件列表")
 
 
 

