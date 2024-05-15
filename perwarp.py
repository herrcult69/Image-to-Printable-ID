import cv2
import numpy as np

image = cv2.imread("unwarp.jpg")
# ul82-133; bl228-681; br1005-501; ur863-0

points_1 = np.array([[82, 133], [863,0],
                     [228, 681], [1005, 501]])
for point in points_1:
    cv2.circle(image, (point[0], point[1]), 5, (0,0,0), cv2.FILLED)

print((points_1[0][0], points_1[0][1]))
print(points_1)
cv2.imshow("image", image)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()