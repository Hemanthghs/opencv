import cv2

cap=cv2.VideoCapture(0)

cap.set(3,640) #here 3 is the id number for setting the width and 640 is the width of the video window

cap.set(4,480) #here 4 is the id number for setting the height of the video window and 480 is the height

cap.set(10,100) #10 is the id doe setting the brightness



while True:
    success,img=cap.read()
    
    cv2.imshow("Webcam",img)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break