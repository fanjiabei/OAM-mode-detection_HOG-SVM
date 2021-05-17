function [trainingFeatures,trainingLabels,testFeatures,testLabels]=extractFeature_cellSize(trainingSet,testSet,cellSize)
%%%%%输入为整理过的训练集和测试集，输出为训练集的特征、标签和测试集的特征、标签。
%%%%%这个函数的功能是将HOG特征和提取的GLCM特征合并
%% 确定特征向量尺寸 通过使用训练集中的一张图片得到特征向量尺寸
img = read(trainingSet(1), 1); %1*9 trainingSet(1)代表train文件夹中的第一个文件夹,返回其中第一张图片
%转化为灰度图像
img=rgb2gray(img);
%转化为2值图像
lvl = graythresh(img);
img = imbinarize(img, lvl); 
img=imresize(img,[256 256]);
[hog_feature, ~] = extractHOGFeatures(img,'CellSize',cellSize);%HOG特征
SizeOfFeature = length(hog_feature);%特征总维数142884

%% 构建训练样本特征向量和训练样本标签
trainingFeatures = [];
trainingLabels   = [];
for digit = 1:numel(trainingSet)   %返回train文件夹中文件夹个数 9个/种
    numImages = trainingSet(digit).Count;%每个模式种类文件夹下图片个数，480
    features  = zeros(numImages, SizeOfFeature, 'single');%初始化特征向量
    % 遍历每张图片
    for i = 1:numImages
        img = read(trainingSet(digit), i);% 取出第i张图片
        img=rgb2gray(img);                % 转化为灰度图像
        lvl = graythresh(img);            % 阈值化
        img = imbinarize(img, lvl);            % 转化为2值图像
        img=imresize(img,[256 256]);
        % 提取HOG特征
        [hog_feature, ~] = extractHOGFeatures(img,'CellSize',cellSize);
        % 合并两个特征
        features(i, :) = hog_feature;
    end
    % 使用图像描述作为训练标签 480行第1列放置图像描述（即模式数文件夹名称）
    labels = repmat(str2num(trainingSet(digit).Description), numImages, 1);  
    % 逐个添加每张训练图片的特征和标签
    trainingFeatures = [trainingFeatures; features];
    trainingLabels   = [trainingLabels; labels];       
end


%% 提取测试图片集的特征向量
testFeatures = [];
testLabels   = [];
for digit = 1:numel(testSet)
           
    numImages = testSet(digit).Count;
    %初始化特征向量
    features  = zeros(numImages, SizeOfFeature, 'single');
    
    for i = 1:numImages
        
        img = read(testSet(digit), i);
        %转化为灰度图像
        img=rgb2gray(img);
       
        %转化为2值图像
        lvl = graythresh(img);
        img = imbinarize(img, lvl);
        img=imresize(img,[256 256]);
        [hog, ~] = extractHOGFeatures(img,'CellSize',cellSize);
        features(i, :) = hog;  %%%合并特征
    end
    
    % 使用图像描述作为训练标签
    labels = repmat(str2num(testSet(digit).Description), numImages, 1);
        
    testFeatures = [testFeatures; features];
    testLabels=[testLabels; labels];
        
end
end
