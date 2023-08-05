#!/usr/bin/env python
# coding: utf-8

# In[7]:


import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector
import keys_to_gesture as ky
from keys_to_gesture import PressKey, ReleaseKey
from keys_to_gesture import space_pressed
import time


# In[8]:


detector=HandDetector(detectionCon=0.8, maxHands=2)

video=cv2.VideoCapture(0) # id=0 for computer webcam
video.set(3,1080) # id 3-> height, resolution in pixel
video.set(4,1080)

space_key_pressed=space_pressed            
time.sleep(0)
current_key_pressed=set()

while True:
    ret, frame=video.read()
    
    keyPressed=False
    spacePressed=False
    
    key_count=0
    key_pressed=0
    
    hands,img=detector.findHands(frame)
    
    if hands:
        
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)
        
        if fingerUp==[1,1,1,1,1]:
            PressKey(space_key_pressed)
            spacePressed=True
            current_key_pressed.add(space_key_pressed)
            key_pressed=space_key_pressed                        
            keyPressed=True
            key_count=key_count+1
                
        if not keyPressed and len(current_key_pressed)!=0:
            for key in current_key_pressed:
                if key_pressed!=key:
                    ReleaseKey(key)
            current_key_pressed=set()
        elif key_count==1 and len(current_key_pressed)==2:
            for key in current_key_pressed:
                if key_pressed!=key:
                    ReleaseKey(key)
            current_key_pressed=set()
            for key in current_key_pressed:
                ReleaseKey(key)
            current_pressed_key=set()
            
        
    cv2.imshow('cam', frame)
    k=cv2.waitKey(1) 
    if k==ord('x'):
        break

video.release()
cv2.destroyAllWindows()


# 
