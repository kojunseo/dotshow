from sys import stdout
import cv2
from ..matching import __stdshow__

def movshow(path, gray=True, size=7, limit=7):
    vidcap = cv2.VideoCapture(path)
    count = 0
    while(vidcap.isOpened()):
        count += 1
        _, image = vidcap.read()
        if count% 30==0:
            __stdshow__(image,gray,size)
            stdout.write("\r")  

        if count == 30*10*limit:
            break

    vidcap.release()