import cv2

'''
圖片閥值化
'''

class Thresholding():

    def __init__(self):
        pass

    '''
    Here, the matter is straight forward. 
     If pixel value is greater than a threshold value, it is assigned one value (may be white),
      else it is assigned another value (may be black). 
       The function used is cv2.threshold. 
        First argument is the source image, which should be a grayscale image. 
         Second argument is the threshold value which is used to classify the pixel values. 
          Third argument is the maxVal which represents the value to be given 
           if pixel value is more than (sometimes less than) the threshold value. 
            OpenCV provides different styles of thresholding and it is decided by the fourth parameter of the function.
             Different types are:

    cv2.THRESH_BINARY
    cv2.THRESH_BINARY_INV
    cv2.THRESH_TRUNC
    cv2.THRESH_TOZERO
    cv2.THRESH_TOZERO_INV
    '''

    def Basic_Thresholding(self, Image, Mode, Start=127, End=255):
        return cv2.threshold(Image, Start, End, Mode)

    '''
    Adaptive Method - It decides how thresholding value is calculated.

    cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
     cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.

    Block Size - It decides the size of neighbourhood area.
     C - It is just a constant which is subtracted from the mean or weighted mean calculated.
      Below piece of code compares global thresholding and adaptive thresholding for an image with varying illumination:
    '''

    def Adaptive_Thresholding(self, Image, Adaptive_Mode, Mode, Block_Size, C, End=255):
        return cv2.adaptiveThreshold(Image, End, Adaptive_Mode, Mode, Block_Size, C)

    '''
    For this, our cv2.threshold() function is used, but pass an extra flag, cv2.THRESH_OTSU.
     For threshold value, simply pass zero.
      Then the algorithm finds the optimal threshold value and returns you as the second output, retVal.
       If Otsu thresholding is not used, retVal is same as the threshold value you used.
    '''

    # I applied Otsu’s thresholding directly.
    def Otsu_Thresholding(self, Image, Start=0, End=255):
        return cv2.threshold(Image, Start, End, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # I filtered image with a 5x5 gaussian kernel to remove the noise, then applied Otsu thresholding.
    def Otsu_Thresholding_Gaussian(self, Image, Gussian=(5, 5), Start=0, End=255):
        blur = cv2.GaussianBlur(Image, Gussian, 0)
        return cv2.threshold(blur, Start, End, cv2.THRESH_BINARY + cv2.THRESH_OTSU)