from itertools import count
from turtle import down
import cv2
import mediapipe as mp
import time
import numpy as np
from Detectors import *


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
poseDict = {}
lastState = 0
lastTime = 0
reps = 0
switch = False
cv2.namedWindow('MediaPipe Pose',0)
# For webcam input:
cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    h,w,c = image.shape
    image.flags.writeable = False
    image = cv2.flip(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            poseDict[id] = (int(lm.x*w),int(lm.y*h))
        lastState,lastTime,reps,switch = headTiltDet(poseDict,lastState,lastTime,reps,switch)
        shoulder,nose,middle,angle = HeadTilePassLineCalculator(poseDict)
        cv2.line(image,shoulder,nose,(255,0,255),1)
        cv2.line(image,shoulder,middle,(255,0,255),1)

    cv2.putText(image,'angle: '+str(angle)+'degree',(200,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)
    cv2.putText(image,'reps:'+str(reps),(500,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)
    cv2.putText(image,'state:'+str(lastState),(500,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)


    if reps%3 == 0 and reps != 0:
        cv2.rectangle(image,(0,0),(175,100),(0,255,0),cv2.FILLED)
    else:
        cv2.rectangle(image,(0,0),(175,100),(0,0,255),cv2.FILLED)
    cv2.imshow('MediaPipe Pose', image)
    key = cv2.waitKey(1)
    if key == 27:
      break
    elif key == 13:
        reps = 0
cap.release()