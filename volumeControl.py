import cv2
import mediapipe as mp
import time
from handDetector import HandDetector
import math
import numpy as np
from pycaw.pycaw import AudioUtilities
import time

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
min_volume = volume.GetVolumeRange()[0]
max_volume = volume.GetVolumeRange()[1]

cap = cv2.VideoCapture(0)
pTime = 0
detector = HandDetector()
volume_level=0
volBar = 400
while True:
    success, img = cap.read()
    if not success:
        break

    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime - pTime else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    img = detector.detect_hands(img)       
    lmlist = detector.get_landmark_positions(img)

    if len(lmlist) != 0:
        x1,y1 = lmlist[4][1], lmlist[4][2]  # Thumb tip
        x2,y2 = lmlist[8][1], lmlist[8][2]  # Index finger tip
        cv2.circle(img, (x1, y1), 12, (255, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 12, (255, 255, 0), cv2.FILLED)
        cv2.line(img,(x1, y1), (x2, y2), (255, 255, 0), 2)
        length = math.hypot(x2 - x1, y2 - y1)
        volume_level = np.interp(length, [20, 200], [min_volume, max_volume])
        volBar = np.interp(length, [20, 200], [400, 150])
        volume.SetMasterVolumeLevel(volume_level, None)
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'Vol: {int(np.interp(volBar, [150, 400], [100, 0]))} %', (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Volume Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()