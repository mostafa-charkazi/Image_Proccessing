import cv2
import numpy as np

def line_detection(image_path, THRESHOLD_VALUE=125, ROI_START=0.55, MIN_CONTOUR_AREA=500):
    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (320, 240))
    frame = cv2.rotate(frame, cv2.ROTATE_180)
    height, width, _ = frame.shape

    # 1. grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3. threshold (خط مشکی)
    _, binary = cv2.threshold(
        blur, THRESHOLD_VALUE, 255, cv2.THRESH_BINARY_INV
    )

    # 4. ROI (فقط پایین تصویر)
    roi_y_start = int(height * ROI_START)
    roi = binary[roi_y_start:height, 0:width]

    # 5. پیدا کردن کانتورها
    contours, _ = cv2.findContours(
        roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    cx = None
    error = None

    if contours:
        # بزرگ‌ترین کانتور (خط)
        c = max(contours, key=cv2.contourArea)

        if cv2.contourArea(c) > MIN_CONTOUR_AREA:
            M = cv2.moments(c)

            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # مرکز تصویر
                frame_center = width // 2
                error = cx - frame_center

                # رسم مرکز خط
                cv2.circle(
                    frame,
                    (cx, roi_y_start + cy),
                    6,
                    (0, 0, 255),
                    -1
                )

                # رسم کانتور
                cv2.drawContours(
                    frame,
                    [c + np.array([0, roi_y_start])],
                    -1,
                    (0, 255, 0),
                    2
                )

    # رسم خط مرکز تصویر
    cv2.line(
        frame,
        (width // 2, 0),
        (width // 2, height),
        (255, 0, 0),
        2
    )

    return error

url = 'images/2.png'
error = line_detection(url)
print(f"Error: {error}")