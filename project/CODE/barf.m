%% 

%% https://www.mathworks.com/help/vision/examples/image-category-classification-using-bag-of-features.html
%%
% matlab function 'bagOfFeatures' trains a bag of words model on the image 
% training set stored in an imageDatastore object. 
imds = imageDatastore(fullfile('./Images'),...
'IncludeSubfolders',true,'FileExtensions','.jpg','LabelSource','foldernames');   

% Divide the images into two different classes acording to the labels 1 and
% 2. In this case, 1 represents a non-url image and 2 represents an image
% with a url. 
[trainingSet, testSet] = splitEachLabel(imds, .5, 'randomize');

%% 
% Train the bag of words model on the training set.  
% Don't train on more than 100 images. 
% We trained the model on 1260 images and the script
% took 3 hours to complete. 
barg = bagOfFeatures(trainingSet);

%%
% Creates a classifier based on the model created in the previous section. 
classifier = trainImageCategoryClassifier(trainingSet, barg);

%%
% Confusion matrix represents how acurate the classifer is, based on the
% input testing set. This calculate the True Positives, True Negatives,
% False Positves and False Negatives
confMat = evaluate(classifier, testSet);
%%

% Perform classification of slices. If an image outputs a Label 2,
% meaning it likely contains a URl, it will be passed on to the next 
% module. 

save_path = './slices';
save_filename = 'image_';
save_extension = '.jpg';
count = 0;
for i=0:162

    full_name = sprintf('%s', testSet.Files{i});

    imtrue = imread(full_name);
    [label, score] = predict(classifier, imtrue);
    
    if label == 2
        %figure, imshow(imtrue);
        imwrite(imtrue, sprintf('%s%s%d%s', save_path, save_filename, i, save_extension)
        count = count +1;
    end
     
end
count;


