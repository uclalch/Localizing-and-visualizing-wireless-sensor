import cv2, math, time
from server_data import Sensors
from image import *

# Initialize camera
cap = cv2.VideoCapture(1)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Initialize video capture (if enabled)
video = False
pause = 0.05
if video:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 1/pause, (width, height))

# Initialize sensor readings
pause = 0.05
sensors = Sensors()
sensors.update()
time.sleep(pause)
sensors.update()

# Get initial location
phi = math.pi / 2
theta = math.pi / 2

while (1):
    # Update sensors
    sensors.update()
    change = sensors.gyr_change()
    phi, theta = update_coordinates(phi, theta, change)

    # Update video
    ret, frame = cap.read()
    redraw_box(frame, height, width, phi, theta)
    cv2.imshow('frame', frame)
    if video:
        out.write(frame)
    if (cv2.waitKey(1) == ord('q')):
        break

    time.sleep(pause)

# Release camera resources
cap.release()
if video:
    out.release()
cv2.destroyAllWindows()