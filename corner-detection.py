import cv2, random
import numpy as np


img = cv2.imread("./chess.png")
img = cv2.resize(img, (0,0), fx=1.2, fy=1.2)
graysclae_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # the image should be grayscale otherwise it doesnt work

total = 0
corners = cv2.goodFeaturesToTrack(graysclae_img, 100, 0.01, 10)  # (image, number_of_corners, the_quality_of_the_corner, min_distance_from_corners)
corners = np.int64(corners)
for corner in corners:
    x,y = np.ravel(corner)  # [[[1,2,3]]] => [1,2,3] it flatens the array
    cv2.circle(img=img, center=(x,y), color=(0,0,255), radius=3, thickness=-1)
    for cor in corners:
        newx, newy = np.ravel(cor)
        cv2.line(img=img, pt1=(x,y), pt2=(newx, newy), color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)), thickness=1)
        total += 1
print(f"{total} lines")

cv2.imshow("frame", img)
cv2.waitKey(0)
cv2.destroyAllWindows()