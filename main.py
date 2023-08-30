import cv2 as cv

# Load the image
img = cv.imread('a.jpg')  # Make sure to provide the correct image file extension

# Convert the image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Apply a fixed threshold
_, result = cv.threshold(img_gray, 25, 255, cv.THRESH_BINARY)

# Apply adaptive thresholding
adaptive = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 4)

# Display the images
cv.imshow('Original Image', img)
cv.imshow('Thresholded Image', result)
cv.imshow('Adaptive Thresholded Image', adaptive)

cv.waitKey(0)
cv.destroyAllWindows()
