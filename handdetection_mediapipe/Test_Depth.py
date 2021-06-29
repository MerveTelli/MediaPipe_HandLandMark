##################
#Test-Dept
##################

import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math

########################
wCam, hCam = 640, 488
########################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionConf=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition_x(img, draw=False)
    if len(lmList) !=0:
        #print(lmList[4], lmList[8])
        h, w, c = img.shape

        x1, y1, z1 =lmList[0][1],lmList[0][2], lmList[0][3]
        x2,y2, z2 = lmList[20][1],lmList[20][2], lmList[20][3]
        avgZ = abs(round((((z1 + z2) / 2) * 1000)))
        print(avgZ)
        cv2.circle(img, (x1, y1), 10, (51, 102, 0), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (51, 102, 0), cv2.FILLED)






    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime=cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40,50), cv2.FONT_HERSHEY_COMPLEX,1,(102,255,102),3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)