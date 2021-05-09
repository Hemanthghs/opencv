import cv2

cap=cv2.VideoCapture("../images/vid1.asf")

while True:
    success,img=cap.read()
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
    