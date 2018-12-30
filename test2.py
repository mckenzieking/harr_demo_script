#!/usr/bin/env python

import numpy as np
import cv2


########## Loads a classifier from a file ########## 
closed_cascadeV3 = cv2.CascadeClassifier('road_closed_v3.xml')
ow_left_cascade = cv2.CascadeClassifier('ow_left_arrow.xml')
ow_right_cascade = cv2.CascadeClassifier('ow_right_arrow.xml')
stop_cascade = cv2.CascadeClassifier('stopsign_classifier.xml')
no_left_cascade = cv2.CascadeClassifier('no_trun_left_symbol_v2.xml')
no_right_cascade = cv2.CascadeClassifier('no_turn_right.xml')


########## Sets up capture from webcam ########## 
cap = cv2.VideoCapture(0)


font = cv2.FONT_HERSHEY_SIMPLEX


while 1:
   

########## Gets frames from camera, sets var gray to a black and white copy of the frame ########## 
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


########## Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles ##########    
    ow_left_signs = ow_left_cascade.detectMultiScale(gray) 
    ow_right_signs= ow_right_cascade.detectMultiScale(gray)
    closed_signsV3 = closed_cascadeV3.detectMultiScale(gray)
    stop_signs = stop_cascade.detectMultiScale(gray)
    no_left_signs = no_left_cascade.detectMultiScale(gray,1.5,2)
    no_right_signs = no_right_cascade.detectMultiScale(gray,1.5,2)  ###play with these params


########## Draws boxes and text ##########
    for (x,y,w,h) in closed_signsV3:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,'Road Closed V3',(x+w,y+h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in ow_right_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,'One Way Right',(x+w,y+h), font, 0.5, (0,255,0), 2, cv2.LINE_AA)
    
    for (x,y,w,h) in ow_left_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,'One Way Left',(x+w,y+h), font, 0.5, (0,255,0), 2, cv2.LINE_AA)

    for (x,y,w,h) in stop_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,'Stop Sign',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    
    for (x,y,w,h) in no_left_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,'No Turn Left',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in no_right_signs:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        cv2.putText(img,'No Turn Right',(x+w,y+h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    

########## Breaks loop if escape key or window close is pressed ########## 
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) < 1:        
        break      


########## Stops showing new frames and closes window ########## 
cap.release()
cv2.destroyAllWindows()
