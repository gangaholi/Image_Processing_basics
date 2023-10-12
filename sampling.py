import cv2
 
# Load the image

img = cv2.imread('messi5.jpg')
 
# Show the image
 
cv2.imshow('Original color',img)
print("Size of Original image: ", img.shape)

image = cv2.pyrUp(img)
print("Size of image after pyrUp: ", image.shape)
cv2.imshow('UpSample', image)

image = cv2.pyrDown(img)
print("Size of image after pyrDown: ", image.shape)
cv2.imshow('DownSample', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
