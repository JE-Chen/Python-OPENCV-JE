import cv2

'''
邊緣檢測用
'''

class Edge():

    def __init__(self):
        pass
    '''
    First argument is our input image. 
    Second and third arguments are our minVal and maxVal respectively. 
    Third argument is aperture_size. 
    It is the size of Sobel kernel used for find image gradients. 
    By default it is 3. Last argument is L2gradient which specifies the equation for finding gradient magnitude. 
    If it is True, it uses the equation mentioned above which is more accurate, By default, it is False.
    '''

    #Canny 邊緣檢測
    def Canny_Edge(self,Image,Min=100,Max=200):
        return cv2.Canny(Image,Min,Max)