import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, MaxHands= 2, detectionConf=0.5, trackConf=0.5):
        self.mode = mode
        self.MaxHands = MaxHands
        self.detectionConf = detectionConf
        self.trackConf = trackConf

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.MaxHands, self.detectionConf, self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB = cv2.flip(imgRGB, 1)
        self.result = self.hands.process(imgRGB)
        #print(result.multi_hand_landmarks)

        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS )
        return img

    def findPosition(self, img, handNo=0, handIndex=0, draw = True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            if self.result.multi_handedness[0].classification[0].index == 0:


                for id, lm in enumerate(myHand.landmark):
                    # print(id,lm)
                    h, w, c= img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    #print(id, cx,cy)
                    #lmList.append([id,cx,cy])
                    lmList.append([id,lm.z])
                    #if id == 0:
                    if draw:
                        if id == 5:


                                cv2.circle(img, (cx,cy), 15 , (255,0,0), cv2.FILLED)

        return lmList

    def findPosition(self, img, handNo=0, handIndex=0, draw=True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            if self.result.multi_handedness[0].classification[0].index == 0:

                for id, lm in enumerate(myHand.landmark):
                    # print(id,lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id, cx,cy)
                    # lmList.append([id,cx,cy])
                    lmList.append([id, lm.z])
                    # if id == 0:
                    if draw:
                        if id == 5:
                            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

        return lmList
                #for id , lm in enumerate(handLms.landmark()):
                    #print(id,lm)
                    #h, w, c= img.shape
                    #cx, cy = int(lm.x*w), int(lm.y*h)
                    #print(id, cx,cy)
                    #if id == 0:
                        #cv2.circle(img, (cx,cy), 25 , (255,0,255), cv2.FILLED)









