import cv2
cap = cv2.VideoCapture('videoplayback.mp4');
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.mp4',fourcc,20,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
        out.write(frame)
        cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()