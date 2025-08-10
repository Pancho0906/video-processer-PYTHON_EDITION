"""video processing application"""
import numpy as np
import cv2 as cv
import sys

def vid_process():
    #choose option by pressing these keys
    normal = ord('n') #normal feed
    denoise = ord('d')
    blur = ord('b')
    canny_edge = ord('e')
    corner = ord('c')
    clahe = ord('h') #brightness normalization

    corn_params = {"maxCorners" : 500,
                   "qualityLevel" : 0.2,
                   "minDistance" : 15,
                   "blockSize" : 9}
    cam = 1
    if len(sys.argv) > 1:
        cam = int(sys.argv[1])

    source = cv.VideoCapture(cam)
    winname = "moh's image processing app"
    cv.namedWindow(winname,cv.WINDOW_NORMAL)

    width = int(source.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(source.get(cv.CAP_PROP_FRAME_HEIGHT))
    dim = (width,height)
    
    option = normal
    while True:

        hasframe, frame = source.read()
        if not hasframe:
            break


        if option == denoise:
            frame = cv.medianBlur(frame, 3)
                
        elif option == blur:
            frame = cv.blur(frame, (21,21))
                
        elif option == canny_edge:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            gray = cv.Canny(gray, 80, 150)
            frame = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

        elif option == corner:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            corners = cv.goodFeaturesToTrack(gray, **corn_params)
            #draw circles around corners
            for x,y in corners.reshape((-1,2)):
                cv.circle(frame, (int(x),int(y)), 10, (255,0,0))

        elif option == clahe:
            lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
            l,a,b = cv.split(lab)
                
            cl = cv.createCLAHE(clipLimit = 3, tileGridSize = (3,3))
            l = cl.apply(l)

            lab = cv.merge((l,a,b))
            frame = cv.cvtColor(lab,cv.COLOR_LAB2BGR)


        key = cv.waitKey(1)
        if key == denoise:
            option = denoise

        elif key == blur:
            option = blur

        elif key == canny_edge:
            option = canny_edge

        elif key == corner:
            option = edge

        elif key == clahe:
            option = clahe

        elif key == normal:
            option = normal

        elif key == 27:#esc
            break
            
            
        


        cv.putText(frame,
                   "Press: (n)normal, (d)denoise, (b)blur, "
                   +"(e)edge det, (c)corner det, (h)clahe",
                   (10,abs(frame.shape[0]-30)),
                   cv.FONT_HERSHEY_PLAIN,
                   1,
                   (0,255,0),
                   1)
        
        cv.imshow(winname, frame)

    cv.destroyWindow(winname)
    source.release()
                
            

