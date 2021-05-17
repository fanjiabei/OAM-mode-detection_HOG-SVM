function [] = Predict(imageurl)

load D:\CODE\aboutSVM\try\only_HOG\classifier2.mat;
figure;
img = imread(imageurl);
imshow(img);

%提取图像的特征向量
%转化为灰度图像
img=rgb2gray(img);
glcm_feature = getGLCMFeatures(img);
%转化为2值图像
lvl = graythresh(img);
img = im2bw(img, lvl);

% imshow(img);
% figure
img=imresize(img,[256 256]);
[hog_4x4, ~] = extractHOGFeatures(img,'CellSize',[4 4]);
testFeature = [hog_4x4 glcm_feature];  %%%%合并特征


% 使用测试图像的特征向量预测样本标签
predictedLabel = predict(classifier2, testFeature);%%%预测标签

str = ['分类结果：' predictedLabel];
dim = [0.25 0.0004 0.2 0.2];
annotation('textbox', dim, 'string', str, 'fontsize', 20, 'color', 'g','edgecolor', 'none');
