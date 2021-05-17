clc;
confMat=confusionmat(testLabels,yfit)  %通过真实标签和根据svm预测到的标签结果生成混淆矩阵
accuracy=(confMat(1,1)/sum(confMat(1,:))+confMat(2,2)/sum(confMat(2,:))+...
    confMat(3,3)/sum(confMat(3,:))+confMat(4,4)/sum(confMat(4,:)))/4
