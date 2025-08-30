import cv2
import numpy as np
import time

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
time.sleep(3)

for i in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)


cv2.namedWindow("HSV Adjustments")
cv2.createTrackbar("LS", "HSV Adjustments", 120, 255, nothing) 
cv2.createTrackbar("LV", "HSV Adjustments", 70, 255, nothing)  
cv2.createTrackbar("US", "HSV Adjustments", 255, 255, nothing)  
cv2.createTrackbar("UV", "HSV Adjustments", 255, 255, nothing)

print("✅ Ready! Adjust sliders to match RED cloth.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ls = cv2.getTrackbarPos("LS", "HSV Adjustments")
    lv = cv2.getTrackbarPos("LV", "HSV Adjustments")
    us = cv2.getTrackbarPos("US", "HSV Adjustments")
    uv = cv2.getTrackbarPos("UV", "HSV Adjustments")

    lower_red1 = np.array([0, ls, lv])
    upper_red1 = np.array([10, us, uv])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, ls, lv])
    upper_red2 = np.array([179, us, uv])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 | mask2

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=3)
    mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations=2)
    mask = cv2.GaussianBlur(mask, (7,7), 0)

    mask_inv = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)  
    res2 = cv2.bitwise_and(background, background, mask=mask) 
    final = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak - Red", final)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
