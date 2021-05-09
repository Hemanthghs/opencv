import cv2

cap=cv2.VideoCapture(0)

cap.set(3,100)
cap.set(4,50)
cap.set(10,100)


while True:
    success,img=cap.read()
    
    cv2.imshow("Webcam",img)
    
    cv2.imshow("Webcam1",img/10)
    cv2.imshow("Webcam2",img/100)
    cv2.imshow("Webcam3",img/255)
    cv2.imshow("Webcam4",img/30)
    cv2.imshow("Webcam5",img/50)
    cv2.imshow("Webcam6",img*10)
    cv2.imshow("Webcam7",img*60)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break