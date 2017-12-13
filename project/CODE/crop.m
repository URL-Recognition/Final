% % Authors: Carlos Downie, Rodrigo Estrella, Ryan Yu
% % Project: URL-Recognition
% % Date: 10/12/17
% % Script Description:
% % 
% % This script performs a sliding window approach as a pre-filtering step.
% % It will divide the input image into 10 horizontal slices. These slices will
% % be used as both training and testing data for the script 'barf.m' 
% % 
% % The horizontal slices are divided into two different classes: 'urls' and 'non-urls'
% % The 'urls' is the positive class. This script will store the top 1/10th of
% % the image in the path ~/Desktop/urls/. These are positive because these sections 
% % contain the navigation bar of the web-browser. 

image_path = './pythonSelenium/screenshots/';
url_path = './Images/urls/';
nonurl_path = './Images/non-urls/';
image_filename = 'url_screenshot';
save_filename = 'image_';
image_extension = '.png';
save_extension = '.jpg';

x = 1;
for i=1:100 %adjust sizes to the range of the screenshots taken. 

    full_name = sprintf('%s%s%d%s', image_path,image_filename, i, image_extension);

    im = imread(full_name);
    im = rgb2gray(im);
    [h, w] = size(im);
    bandSize = h/10; 
    
    firstPartition = im(1:bandSize, :, :);
    save_name = sprintf('%s%s%d%s', url_path,save_filename, i, save_extension);
    imwrite(firstPartition, save_name);
    
    
    for j=1:9
      other_save_name = sprintf('%s%s%d%s', nonurl_path,save_filename, x, save_extension);
      slice = im((j * bandSize):((j+1) * bandSize), :, :);
       imwrite(slice, other_save_name);
       x = x + 1;
       % makes sure to collect the same number of urls and non-urls
       if x == 100 
           break
       end
    end
    
   
end


