import cv2
import numpy as np
import imutils
import pyautogui as pg  #for operating keys using python

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
     _,frame= cap.read()

     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


     lower_blue=np.array([90,60,0])
     upper_blue=np.array([121,255,255])
     
     
     mask4 = cv2.inRange(hsv,lower_blue,upper_blue)
     
     
     
     cnts4 = cv2.findContours(mask4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts4 = imutils.grab_contours(cnts4)

     for c in cnts4:
         
         area4 = cv2.contourArea(c)
         if area4 > 5000:

             
             cv2.drawContours(frame,[c],-1,(0,255,0), 3)
             pg.press('up')
             
             M = cv2.moments(c)

             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])

             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             cv2.putText(frame,"blue",(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),3)
    
     cv2.imshow("result",frame)

     if cv2.waitKey(1) & 0xFF == ord('q'):       
        break


cap.release()
cv2.destroyAllWindows()
