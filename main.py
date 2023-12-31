import cv2
source = "Love LOGO.png"
destination = "newImage.png"
scale_percent = 50 #Percent by which image is resized

image = cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("Love_Stories",image)
# cv2.waitKey(0)



# Calcutale the 50 percent of original Dimensions 
new_width = int(image.shape[1]*scale_percent/100)
new_height = int(image.shape[0]*scale_percent/100)

# Resize Image 
output = cv2.resize(image , (new_width , new_height))

cv2.imwrite(destination,output)
cv2.waitKey(0)
