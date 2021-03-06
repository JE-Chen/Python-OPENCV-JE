import cv2
import numpy as np

'''
物件追蹤
'''

class Object_Tracking():

    def __init__(self):
        pass

    def MeanShift(self,Video,Right=100,Height=400,C=200,Width=125):
        cap = cv2.VideoCapture(Video)

        # take first frame of the video
        ret, frame = cap.read()

        # setup initial location of window
        r, h, c, w = Right, Height, C, Width  # simply hardcoded the values
        track_window = (c, r, w, h)

        # set up the ROI for tracking
        roi = frame[r:r + h, c:c + w]
        hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
        roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

        # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

        while (1):
            ret, frame = cap.read()

            if ret == True:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

                # apply meanshift to get the new location
                ret, track_window = cv2.meanShift(dst, track_window, term_crit)

                # Draw it on image
                x, y, w, h = track_window
                img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
                cv2.imshow('img2', img2)

                k = cv2.waitKey(60) & 0xff
                if k == 27:
                    break
                else:
                    pass

            else:
                break

        cv2.destroyAllWindows()
        cap.release()

    def CamShift(self,Video,Right=100,Height=200,C=200,Width=125):
        cap = cv2.VideoCapture(Video)

        # take first frame of the video
        ret, frame = cap.read()

        # setup initial location of window
        r, h, c, w = Right, Height, C, Width  # simply hardcoded the values
        track_window = (c, r, w, h)

        # set up the ROI for tracking
        roi = frame[r:r + h, c:c + w]
        hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
        roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
        cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

        # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
        term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

        while (1):
            ret, frame = cap.read()

            if ret == True:
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

                # apply meanshift to get the new location
                ret, track_window = cv2.CamShift(dst, track_window, term_crit)

                # Draw it on image
                pts = cv2.boxPoints(ret)
                pts = np.int0(pts)
                img2 = cv2.polylines(frame, [pts], True, 255, 2)
                cv2.imshow('img2', img2)

                k = cv2.waitKey(60) & 0xff
                if k == 27:
                    break
                else:
                    pass

            else:
                break

        cv2.destroyAllWindows()
        cap.release()


    '''
    How to find HSV values to track?
    >>> green = np.uint8([[[0,255,0 ]]])
    >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    >>> print (hsv_green)
    [[[ 60 255 255]]]
    '''
    def Tracking_Color(self,Video,Track_Range_Lower=[110, 50, 50],Track_Range_Upper=[130, 255, 255]):
        cap = cv2.VideoCapture(Video)

        while (1):

            # Take each frame
            _, frame = cap.read()

            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower_blue = np.array(Track_Range_Lower)
            upper_blue = np.array(Track_Range_Upper)

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame, frame, mask=mask)

            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            elif k == ord('q'):
                break

        cv2.destroyAllWindows()