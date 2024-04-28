import cv2
import matplotlib.pyplot as plt
# Read the image
img = cv2.imread('image.jpg')
# Check if the image has been successfully loaded
if img is None:
    print("Error: Unable to load image.")
else:
# Display the color image
    cv2.imshow('Color Image', img)
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image', image)
# Calculate the histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
# Plotting the histogram
plt.plot(histogram, color='gray')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Image Histogram')
plt.show()