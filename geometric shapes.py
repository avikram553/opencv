import cv2
img=cv2.imread('board.jpg',1)
img=cv2.line(img,(0,0),(500,144),(255,0,0),6)
img=cv2.arrowedLine(img,(0,0),(50,144),(255,255,255),6)
img=cv2.rectangle(img,(45,45),(300,455),(255,255,255),-1)
img=cv2.circle(img,(300,0),60,(0,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'Hello',(10,500),font,4,(0,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()