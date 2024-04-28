#Write Python Program for edge detection
import cv2
# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# Apply Gaussian blur to reduce noise
#blur = cv2.GaussianBlur(image, (5,5), 0)
# Apply Canny edge detection
edges = cv2.Canny(image, 50, 150) # You can adjust the thresholds
# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWin