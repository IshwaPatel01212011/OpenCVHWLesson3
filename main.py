import cv2

pokimon = cv2.imread("Lesson 3/images/pokimon.png")

# Using the cvtColor() function

grey = cv2.cvtColor(pokimon,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey Pokimon",grey)
cv2.waitKey(0)

# Using the HSV function

hsv = cv2.cvtColor(pokimon,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Pokimon",hsv)
cv2.waitKey(0)

# Roating Images
h,w,c = pokimon.shape
Matrix = cv2.getRotationMatrix2D((w/2,h/2),45,1)
rotate = cv2.warpAffine(pokimon,Matrix,(w,h))
cv2.imshow("Roatating Image",rotate)
cv2.waitKey(0)

# Edge Detection
edges = cv2.Canny(pokimon, 500, 1000 )
cv2.imshow("Detecting the Edges of an Image",edges)
cv2.waitKey(0)

# Changing Images Color to Grey Steps

pokimon = cv2.imread("Lesson 3/images/pokimon.png")
h,w,c = pokimon.shape
print(pokimon[156,213])

for i in range (h):
    for j in range (w):
        pokimon[i,j] = sum(pokimon [i,j]) * 0.33

cv2.imshow("Pokimon", pokimon)
cv2.waitKey(0)
