import cv2
import numpy as np


def warp_perspective(img, points_objs: list, rwidth=None, rheight=None):
    x1, y1 = points_objs[0].x, points_objs[0].y
    x2, y2 = points_objs[1].x, points_objs[1].y
    x3, y3 = points_objs[2].x, points_objs[2].y
    x4, y4 = points_objs[3].x, points_objs[3].y
    print((x1, y1), (x2, y2), (x3, y3), (x4, y4))
    unwarp = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], dtype=np.float32)
    warped = np.array([[0, 0], [rwidth, 0], [0, rheight], [rwidth, rheight]], dtype=np.float32)
    tranform_mat = cv2.getPerspectiveTransform(unwarp, warped)
    return cv2.warpPerspective(img, tranform_mat, (rwidth, rheight), flags=cv2.INTER_LINEAR)
