import cv2
import numpy as np

image = cv2.imread("unwarp.jpg")
# ul82-133; bl228-681; br1005-501; ur863-0
# 204 x 323
height = 204
width = 323
points_1 = np.float32([[82, 133], [863,0],
                     [228, 681], [1005, 501]])
points_2 = np.float32([[0, 0], [width, 0],
                     [0, height], [width, height]])
for point in points_1:
    center = (int(point[0]), int(point[1]))  # Convert to integers
    cv2.circle(image, center, 5, (0, 0, 0), cv2.FILLED)

tranform_mat = cv2.getPerspectiveTransform(points_1, points_2)
new_image = cv2.warpPerspective(image, tranform_mat, (width, height))

cv2.imshow("image", image)
cv2.imshow("new_image", new_image)
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()