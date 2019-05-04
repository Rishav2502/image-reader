import cv2

img = cv2.imread('rj.jpg',1)
print(img.shape)
resiged = cv2.resize(img,(800,600))
cv2.imshow("quotes", resiged)
cv2.waitKey(0)
cv2.destryAllWindows()