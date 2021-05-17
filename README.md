# OAM-mode-detection_HOG-SVM
OAM-mode-detection
In the case of OAM transceiver alignment, HOG + SVM is used for mode detection. The functions are as follows:

Python language:

1. Judge whether the folder exists, if not, create a new one, read and save JPG files in batch.

2. Data enhancement (rotation, contrast, brightness, chroma, sharpness), just modify the file path, solve the problem of background missing caused by rotation, select white fill. python

MATLAB：

1. Batch reading of images enhanced by Python data;

2. Set different cellsizes to extract hog features;

3. SVM realizes modal detection and classification.

result:

Recognition accuracy is 100%
