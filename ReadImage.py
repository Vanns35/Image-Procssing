import cv2
#ReadImage
image = cv2.imread("testing.jpg");
#DisplayImage
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyWindows()
