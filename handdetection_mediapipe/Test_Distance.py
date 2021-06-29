##################
# Test-Distance
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
    lmList = detector.findPosition2(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[0][1], lmList[0][2]
        x2, y2 = lmList[20][1], lmList[20][2]
        avgX = (x1 + x2) / 2
        print(avgX)

        cv2.circle(img, (x1, y1), 10, (51, 102, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (51, 102, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (102, 255, 102), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
