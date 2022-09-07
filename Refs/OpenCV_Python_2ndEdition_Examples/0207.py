# 0207.py
import cv2

#cap = cv2.VideoCapture(0)  # 0번 카메라
cap = cv2.VideoCapture('./data/vtest.avi')
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

while True:   
    retval, frame = cap.read()
    if not retval:
        break
    text = 'OpenCV Programming'
    org = (200,100)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,text, org, font, 1, (255,0,0), 2)

    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
