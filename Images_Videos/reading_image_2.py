import cv2

img=cv2.imread("../images/dog.209.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(21,21),0)#(21,21) [Note:kernel size must be in odd numbers] is the kernel size and 0 is sigma x value
imgCanny=cv2.Canny(img,150,200)


cv2.imshow("image",img)
cv2.imshow("imageGray",imgGray)
cv2.imshow("imageBlur",imgBlur)
cv2.imshow("imageCanny",imgCanny)

cv2.waitKey(0)