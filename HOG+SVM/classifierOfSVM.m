tic;
clear;
dir=('D:\CODE\aboutSVM\classifier_app\Segdataset\train');%D:\CODE\SVM\pictures
testdir=('D:\CODE\aboutSVM\classifier_app\Segdataset\val');%D:\CODE\SVM\testPictures\test
trainingSet = imageSet(dir,'recursive');  %返回1*numdir向量，dir包含至少一个图像的文件夹数 1*9
testSet = imageSet(testdir,'recursive');  %Start recursive image search folder
cellSize=[12 12];
[trainingFeatures,trainingLabels,testFeatures,testLabels]=extractFeature(trainingSet,testSet,cellSize);
data=[trainingFeatures trainingLabels];
% 使用测试图像的特征向量预测样本标签

% model = loadCompactModel('trainedModel.mat');    
[a,b]=trainClassifier(testFeatures);
%% 评估分类器
%使用没有标签的图像数据进行测试，生成一个混淆矩阵表明分类效果
% confMat=confusionmat(testLabels,  predictedLabels)  %通过真实标签和根据svm预测到的标签结果生成混淆矩阵
% accuracy=(confMat(1,1)/sum(confMat(1,:))+confMat(2,2)/sum(confMat(2,:))+...
%     confMat(3,3)/sum(confMat(3,:))+confMat(4,4)/sum(confMat(4,:)))/4
print(b)
toc;
% save workplace
