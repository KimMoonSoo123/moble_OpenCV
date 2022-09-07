# 0412.py
import cv2
src = cv2.imread('./data/lena.jpg')

dst = cv2.split(src)
dst = cv2.merge([dst[0], dst[1], dst[2]]) 

print(type(dst))
print(dst.shape)
cv2.imshow('dst',  dst)
cv2.waitKey()    
cv2.destroyAllWindows()
