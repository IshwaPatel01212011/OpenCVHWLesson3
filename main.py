import cv2

dog = cv2.imread("Lesson 3/images/dog.png")

# Using the cvtColor() function

grey = cv2.cvtColor(dog,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Dog",grey)
cv2.waitKey(0)

# Using the HSV function

hsv = cv2.cvtColor(dog,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV dog",hsv)
cv2.waitKey(0)

# Roating Images
h,w,c = dog.shape
Matrix = cv2.getRotationMatrix2D((w/2,h/2),45,1)
rotate = cv2.warpAffine(dog,Matrix,(w,h))
cv2.imshow("Roatating Image",rotate)
cv2.waitKey(0)

# Edge Detection
edges = cv2.Canny(dog, 250, 500 )
cv2.imshow("Detecting the Edges of an Image",edges)
cv2.waitKey(0)

# Changing Images Color to Grey Steps

dog = cv2.imread("Lesson 3/images/dog.png")
h,w,c = dog.shape
print(dog[156,213])

for i in range (h):
    for j in range (w):
        dog[i,j] = sum(dog [i,j]) * 0.33

cv2.imshow("Dog", dog)
cv2.waitKey(0)

