import cv2
 
# Load the image


img = cv2.imread('Images/opencv_logo1.jpg')
 
# Show the image
 
cv2.imshow('Original color',img)


b,g,r=cv2.split(img)
print(b)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
"""

image = cv2.pyrUp(img)
print("Size of image after pyrUp: ", image.shape)
cv2.imshow('UpSample', image)

img_neg = cv2.bitwise_not(img)
 
# Show the image

cv2.imshow('color negative',img_neg)

img = cv2.imread('messi5.jpg',0)
 
cv2.imshow('Original gray scale',img)

# Invert the image using cv2.bitwise_not

img_neg = cv2.bitwise_not(img)
 
# Show the image
cv2.imshow('negative',img_neg)
"""
cv2.waitKey(0)




