clear;close all;clc;
%%
%程序实现的功能
%1、把指定路径的数据（已按类别放置在不同的文件夹中），随机的把其中的75%的划分为训练集，25%划分为测试集
%2、训练集按类别放在指定路径的train文件夹中，测试集按类别放在指定路径的val文件夹中
%3、在train和val文件夹的同级文件夹按照caffe需求生成对应的train.txt和val.txt的label
%%
%程序中用到的之前不清楚的函数如下
%1）disp：用来在界面上显示一些必要的信息，方便查看程序进度。disp(' ')可以起到在界面上换行显示的作用
%2）str2double：带起之前一直使用的str2num,matlab的提示是这样函数效率更高。而且这两个函数输出的数据类型都是double类型。
%3）randperm（n）：生成一个1到n直接的随机数列
%4）copyfile（a,b）：把文件a复制到路径b，路径b带有最后的\符号
%
%
%
%%
disp('程序开始执行');
%%%%%%需要更改的参数（即两个路径）%%%%%%%%%%%%%%%%%%%%%%%%%%
 
pathSource='D:\CODE\OAMimage\';%OAM文件夹下有9个文件夹9*600
 
pathDestination='D:\CODE\Segmentation_dataset\Segdataset\';%保存分割后数据集以及train.txt和test.txt
 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%在目标路径创建train、val文件夹
pathCreDirTrain=[pathDestination,'\','train','\'];
mkdir(pathCreDirTrain);
pathCreDirVal=[pathDestination,'\','val','\'];
mkdir(pathCreDirVal);
 
 
%读取文件夹列表，这种方式读取会保留原文件.(在结构体中第一个)和上一层目录..(在结构体第二个)
dirSourceList=dir(pathSource);   %modenum_-4,...,modenum_0,...,modenum_4
countSourceList=length(dirSourceList);%文件夹个数
%拷贝数据到目标路径
for numDirList=3:countSourceList  %实际文件夹个数为9（11-2）
    %if(length(dirSourceList(numDirList).name)>=2)%根据这个过滤掉在此文件夹可能的train.txt、val.txt、count.txt文件
        %continue;
    %end    
    fileName=dir([pathSource,'\',dirSourceList(numDirList).name]);%读取子文件夹中的图片
    
    %统计子文件夹中的文件个数
    fileSum=length(fileName);
    fileNum=fileSum-2;%为了生成对应于读取的从3开始的文件，只能先减去2，然后生成随机数后加上2
    disp(' ');%加入一个空格，作为在界面显示中一个类似于换行的工具
    %在程序中增加一些输出信息，方便查看数据内容
    disp(['原始数据子文件夹',num2str(dirSourceList(numDirList).name),'中有图片：',num2str(fileNum)]);
    
    %由于matlab读取文件的规则，在文件列表中肯定最前面会有.和..这两个文件
    %所以想到先生成fileSum-2范围内的随机数，然后再各项加2，就为真正要找的随机数
    numFileList=randperm(fileNum);
    numFileList=numFileList+2;
    partitionPosition=round(fileNum/5);%这是通过四舍五入确定的分割位置。这是划分数据的比例，2是按一半划分，如果是4的话，'先拷贝val（前25%）后拷贝train（后75%）'
    
    %在程序中增加一些输出信息，方便查看数据内容
%     disp(['先拷贝val（前25%）后拷贝train（后75%）']);
    
   %%
    %拷贝测试集数据val
    %在程序中增加一些输出信息，方便查看程序执行进度
    disp(['在val文件夹下创建子文件夹',num2str(dirSourceList(numDirList).name)]);
    disp(['拷贝',num2str(partitionPosition),'张图片到val文件夹下子文件夹',num2str(dirSourceList(numDirList).name),'中']);
     
    %不知道这种拷贝东西到别的地方，是先拷贝数据量比较多的部分，还是数据量比较少的部分，这有什么讲究。
    %在目标val文件夹中，创建对应的子文件夹
    pathCreValDir=[pathCreDirVal,dirSourceList(numDirList).name,'\'];
    mkdir(pathCreValDir);
    
    %在程序中增加一些输出信息，方便查看程序执行进度
    disp(['复制测试数据到val子文件夹',num2str(dirSourceList(numDirList).name),'中']);
    
    %复制图片到指定路径
    for picNum=1:partitionPosition%由于是要读取numFileList中生成的随机数据，所以从1开始
        copyfile([pathSource,'\',dirSourceList(numDirList).name,'\',fileName(numFileList(picNum)).name], ...
            pathCreValDir);
    end
   %%
    %拷贝训练集数据train
    %在程序中增加一些输出信息，方便查看程序执行进度
    disp(['在train文件夹下创建子文件夹',num2str(dirSourceList(numDirList).name)]);
    disp(['拷贝',num2str(fileNum-partitionPosition),'张图片到train文件夹下子文件夹',num2str(dirSourceList(numDirList).name),'中']);  
    
    %在目标train文件夹中，创建对应的子文件夹
    pathCreTrainDir=[pathCreDirTrain,dirSourceList(numDirList).name,'\'];
    mkdir(pathCreTrainDir);  
    
    %在程序中增加一些输出信息，方便查看程序执行进度
    disp(['复制训练数据到Train子文件夹',num2str(dirSourceList(numDirList).name),'中']);
    
    %复制图片到指定路径
    for picNum=partitionPosition+1:fileNum%由于是要读取numFileList中生成的随机数据，所以从1开始
        copyfile([pathSource,'\',dirSourceList(numDirList).name,'\',fileName(numFileList(picNum)).name], ...
            pathCreTrainDir);
    end    
end
disp('数据拷贝完毕');
 
 
%%
%生成label
disp('开始生成label');
%考虑到最好写个程序，能够一步完整所有操作。所以在这程序下面加上生成label的功能
%在上面的程序中，已经有变量pathCreDirTrain（目标Train的路径）、pathCreDirVal（目标Val的路径）
%先生成train文件夹中的label
disp('开始生成trainlabel');
dirTrainList=dir(pathCreDirTrain);%读取文件夹列表，这种方式读取会保留原文件.(在结构体中第一个)和上一层目录..(在结构体第二个)
countTrainList=length(dirTrainList);%文件夹个数
fid = fopen([pathDestination,'\','train.txt'], 'w');%打开train文件夹时，对应的文本文件
for numList=3:countTrainList%文件夹从3开始
    %if(length(dirTrainList(numList).name)>=2)%根据这个过滤掉在此文件夹可能的train.txt文件
        %continue;
    %end
    fileName=dir([pathCreDirTrain,'\',dirTrainList(numList).name]);%读取子文件夹
    fileSum=length(fileName);%统计子文件夹中的文件个数
    for fileNum=3:fileSum%文件从3开始
        fprintf(fid,'%s', [fileName(fileNum).name]);%输入：子文件/图片名称
        fprintf(fid,'%s', ' ');%空格间隔符    
        fprintf(fid,'%s', dirTrainList(numList).name);%加入label,即文件夹名称
        fprintf(fid,'\n');%换行
    end
end
fclose(fid);%关闭文本文件 fprintf(fid,'%s', dirTrainList(numList).name);%加入label,即文件夹名称
fclose('all');%关闭所有连接，防止没关掉的情况
disp('trainlabel生成完毕');
 
%在上面的程序中，已经有变量pathCreDirTrain（目标Train的路径）、pathCreDirVal（目标Val的路径）
%先生成train文件夹中的label
disp('开始生成vallabel');
dirValList=dir(pathCreDirVal);%读取文件夹列表，这种方式读取会保留原文件.(在结构体中第一个)和上一层目录..(在结构体第二个)
countValList=length(dirValList);%文件夹个数
fid = fopen([pathDestination,'\','val.txt'], 'w');%打开train文件夹时，对应的文本文件
for numList=3:countValList%文件夹从3开始
    %if(length(dirValList(numList).name)>=2)%根据这个过滤掉在此文件夹可能的train.txt文件
     %   continue;
    %end
    fileName=dir([pathCreDirVal,'\',dirValList(numList).name]);%读取子文件夹
    fileSum=length(fileName);%统计子文件夹中的文件个数
    for fileNum=3:fileSum%文件从3开始
        fprintf(fid,'%s', [fileName(fileNum).name]);%输入：子文件/图片名称
        fprintf(fid,'%s', ' ');%空格间隔符    
        fprintf(fid,'%s', dirValList(numList).name);%加入label,即文件夹名称
        fprintf(fid,'\n');%换行
    end
end
fclose(fid);%关闭文本文件
fclose('all');%关闭所有连接，防止没关掉的情况
disp('vallabel生成完毕');
