import time
import math
def squatDet(landmarksDictionary,previousState,previousTime,count,flag):
    if landmarksDictionary != {}:
        knee_y = landmarksDictionary[25][1]
        hip_y = landmarksDictionary[23][1]
        ankle_y = landmarksDictionary[27][1]
        if (knee_y - (ankle_y - knee_y)*0.5) < hip_y : # hip lower than or having equal height with knee
            if previousState == 1 and time.time()-previousTime >= 0.5 and flag == False:
                count +=1
                flag = True
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == False:
                previousState = 1
                previousTime = time.time()
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        elif (knee_y - (ankle_y - knee_y)*0.5) > hip_y:# hip higher than knee
            if previousState == 1 and flag == True:
                flag = False
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 1 and flag == False:
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == True:
                flag = False
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        else:
            return previousState,previousTime,count,flag

def latArmDet(landmarksDictionary,previousState,previousTime,count,flag):
    if landmarksDictionary != {}:
        eye_y = landmarksDictionary[5][1]
        L_elbow_y = landmarksDictionary[14][1]
        R_elbow_y = landmarksDictionary[13][1]
        if L_elbow_y < eye_y and R_elbow_y < eye_y: # elbow higher than  eye
            if previousState == 1 and time.time()-previousTime >= 0.5 and flag == False:
                count +=1
                flag = True
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == False:
                previousState = 1
                previousTime = time.time()
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        elif  L_elbow_y > eye_y or R_elbow_y > eye_y:# elbow lower than  eye
            if previousState == 1 and flag == True:
                flag = False
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 1 and flag == False:
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == True:
                flag = False
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        else:
            return previousState,previousTime,count,flag


def frontArmDet(landmarksDictionary,previousState,previousTime,count,flag):
    if landmarksDictionary != {}:
        L_shoulder_x = landmarksDictionary[11][0]
        R_shoulder_x = landmarksDictionary[12][0]
        L_elbow_y = landmarksDictionary[14][1]
        R_elbow_y = landmarksDictionary[13][1]
        L_wrist_x = landmarksDictionary[15][0]
        R_wrist_x = landmarksDictionary[16][0]
        L_mouth_y = landmarksDictionary[9][1]
        R_mouth_y = landmarksDictionary[10][1]
        mouth_middle = (L_mouth_y+R_mouth_y)/2
        if L_elbow_y < mouth_middle and R_elbow_y < mouth_middle and L_wrist_x < L_shoulder_x and R_wrist_x > R_shoulder_x: # elbow higher than  shoulder
            if previousState == 1 and time.time()-previousTime >= 0.5 and flag == False:
                count +=1
                flag = True
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == False:
                previousState = 1
                previousTime = time.time()
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        elif  L_elbow_y > mouth_middle or R_elbow_y > mouth_middle or L_wrist_x > L_shoulder_x or R_wrist_x < R_shoulder_x:# elbow lower than  shoulder
            if previousState == 1 and flag == True:
                flag = False
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 1 and flag == False:
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == True:
                flag = False
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        else:
            return previousState,previousTime,count,flag




def headTiltDet(landmarksDictionary,previousState,previousTime,count,flag):
    if landmarksDictionary != {}:
        L_shoulder_x = landmarksDictionary[11][0]
        L_shoulder_y = landmarksDictionary[11][1]
        R_shoulder_x = landmarksDictionary[12][0]
        R_shoulder_y = landmarksDictionary[12][1]
        nose_x = landmarksDictionary[0][0]
        nose_y = landmarksDictionary[0][1]
        shoulder_middle_x = (L_shoulder_x+R_shoulder_x)/2
        shoulder_middle_y = (L_shoulder_y+R_shoulder_y)/2
        middle_line_x = shoulder_middle_x
        middle_line_y = nose_y
        head_tilt_angle = angleCalculator(shoulder_middle_x,shoulder_middle_y,nose_x,nose_y,middle_line_x,middle_line_y)
        # return int(head_tilt_angle)

        if head_tilt_angle>20: # elbow higher than  shoulder
            if previousState == 1 and time.time()-previousTime >= 0.5 and flag == False:
                count +=1
                flag = True
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == False:
                previousState = 1
                previousTime = time.time()
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        elif  head_tilt_angle<20:# elbow lower than  shoulder
            if previousState == 1 and flag == True:
                flag = False
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 1 and flag == False:
                previousState = 0
                return previousState,previousTime,count,flag
            elif previousState == 0 and flag == True:
                flag = False
                return previousState,previousTime,count,flag
            else:
                return previousState,previousTime,count,flag
        else:
            return previousState,previousTime,count,flag



def SquatPassLineCalculator(landmarksDictionary):
    if landmarksDictionary != {}:
        knee_y = landmarksDictionary[25][1]
        hip_y = landmarksDictionary[23][1]
        ankle_y = landmarksDictionary[27][1]
        L_knee_y = landmarksDictionary[26][1]
        L_hip_y = landmarksDictionary[24][1]
        L_ankle_y = landmarksDictionary[28][1]
        passPoint = int(knee_y - (ankle_y - knee_y)*0.5)
        L_passPoint = int(knee_y - (ankle_y - knee_y)*0.5)
        return L_passPoint,passPoint
    else:
        return None


def FrontArmRaisePassLineCalculator(landmarksDictionary):
    if landmarksDictionary != {}:
        L_shoulder_x = landmarksDictionary[12][0]
        R_shoulder_x = landmarksDictionary[11][0]
        L_mouth_y = landmarksDictionary[9][1]
        R_mouth_y = landmarksDictionary[10][1]
        mouth_middle = int((L_mouth_y+R_mouth_y)/2)
        R_passPoint = int(R_shoulder_x)
        L_passPoint = int(L_shoulder_x)
        return L_passPoint,R_passPoint,mouth_middle
    else:
        return None


def HeadTilePassLineCalculator(landmarksDictionary):
    if landmarksDictionary != {}:
        L_shoulder_x = landmarksDictionary[11][0]
        L_shoulder_y = landmarksDictionary[11][1]
        R_shoulder_x = landmarksDictionary[12][0]
        R_shoulder_y = landmarksDictionary[12][1]
        nose_x = landmarksDictionary[0][0]
        nose_y = landmarksDictionary[0][1]
        shoulder_middle_x = (L_shoulder_x+R_shoulder_x)/2
        shoulder_middle_y = (L_shoulder_y+R_shoulder_y)/2
        middle_line_x = shoulder_middle_x
        middle_line_y = nose_y
        head_tilt_angle = angleCalculator(shoulder_middle_x,shoulder_middle_y,nose_x,nose_y,middle_line_x,middle_line_y)
        return (int(shoulder_middle_x),int(shoulder_middle_y)),(int(nose_x),int(nose_y)),(int(middle_line_x),int(middle_line_y)),int(head_tilt_angle)
    else:
        return None


def angleCalculator(mx,my,bx,by,cx,cy):
    mb = (bx-mx,by-my)
    mc = (cx-mx,cy-my)
    mbAbs = ((mx-bx)**2+(my-by)**2)**0.5
    mcAbs = ((mx-cx)**2+(my-cy)**2)**0.5 
    angle = math.degrees(math.acos((mb[0]*mc[0]+mb[1]*mc[1])/(mbAbs*mcAbs)))
    return angle
