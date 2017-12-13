import cv2
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

class ImageOCR:

    #CHARACTER_WHITELIST = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:/?#[]@!$&'()*+,;=`._ -psm 6"

    #Takes in a grayscale image slice and pre_processes it for the OCR
    def pre_process(self,image_file,save = False):
        """
        :param image_file: The image file name to preprocess
        :param save: Set to true if you want preprocessed image to be saved (Optional)
        """

        # read in image
        image = cv2.imread(image_file, cv2.CV_8UC1)
        # resize image to be of 2x original size
        x, y = image.shape[:2]
        rsize = cv2.resize(image, (y*2, 2*x))
        # apply adaptive threshold and conversion to binary image, this works best with blur
        prep2 = cv2.adaptiveThreshold(rsize, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
        # apply median blur to clean pepper noise
        prep2 = cv2.medianBlur(prep2, 3)

        #If save option, save preprocessed image
        if(save):
            #create image name
            ind = image_file.rfind('.')#Get index of last period
            save_name = image_file[:ind] + '_processed' + image_file[ind:]
            # save image to new name
            cv2.imwrite(save_name, prep2)
            return [prep2, save_name]

        return prep2

    def do_OCR(self,image_file,preprocess = True,save = False):

        #Perform preprocessing operation
        if(preprocess):
            if save:
                image = self.pre_process(image_file, save)[0]
            else:
                image = self.pre_process(image_file, save)
        else:
            image = cv2.imread(image_file)

        return pytesseract.image_to_string(Image.fromarray(image))

    def get_word_list(self,image_file,preprocess=True,save=False):
        txt = self.do_OCR(image_file, preprocess, save)
        return txt.split()

# #The rest of the code here should occur after preprocessing
#
#
# def cleanstring(s):
#     dict = [('|', 'l'), ('—', '-')]
#     for i in dict:
#         if i[0] in s:
#             s = s.replace(i[0], i[1])
#     return s
#
# #replace '|' and '—' with 'l' and '-'
# text = cleanstring(text)
#
# #print entirety of read
# print(text)


