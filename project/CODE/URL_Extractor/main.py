import URL_Detector #Our class used for filtering URL from text array
import ImageOCR #Our class for performing OCR preprocessing steps

Detector = URL_Detector.URL_Detector()
#Pass in our training data so that the detector is trained for finding URLS
Detector.perform_training('URL_files/URLS.txt', 'URL_files/NonURLS.txt')

OCR = ImageOCR.ImageOCR()

#Get a list of words detected by the OCR module for the specified image
txt = OCR.get_word_list(‘../slices/image_1.jpg’, True, True)

#Filter the word list for URL(s)
testURLs = Detector.classify_array(txt)

print('The text from this image is: {}\n'.format(txt))
print('From the list above, detected URL(s) are: {}'.format(testURLs))
