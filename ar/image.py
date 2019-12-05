import cv2, math
import numpy as np

def redraw_box(image, height, width, phi, theta):
    # Convert to representation with (0, 0) at center
    f = 1000
    try:
        u = f * (math.cos(phi) / math.sin(phi))
        v = f * (math.cos(theta) / (math.sin(phi) * math.sin(theta)))
    except:
        return

    # Convert to OpenCV coordinates with (0, 0) at top-left
    x = int(u + (width / 2))
    y = int(abs(v - (height / 2)))

    # Draw circle if sensor is within bounds
    if (x >= 0 and y >= 0 and x <= width and y <= height):
        cv2.circle(image, (x, y), 30, (0, 255, 0))
    return

def update_coordinates(phi, theta, delta):
    # Convert delta x/y to radians
    delta_x = -math.radians(delta['x'])
    delta_y = -math.radians(delta['y'])
    delta_z = -math.radians(delta['z'])

    # Convert phi/theta to x/y/z
    xyz_mat = np.array([
        math.cos(phi) * math.sin(theta),
        math.sin(phi) * math.sin(theta),
        math.cos(theta)
    ])

    # Create matrices for angle changes
    mat1 = np.array([
        [1, 0, 0],
        [0, math.cos(delta_x), -math.sin(delta_x)],
        [0, math.sin(delta_x), math.cos(delta_x)]
    ])

    mat2 = np.array([
        [math.cos(delta_y), 0, math.sin(delta_y)],
        [0, 1, 0],
        [-math.sin(delta_y), 0, math.cos(delta_y)]
    ])

    mat3 = np.array([
        [math.cos(delta_z), -math.sin(delta_z), 0],
        [math.sin(delta_z), math.cos(delta_z), 0],
        [0, 0, 1]
    ])

    # Convert new x/y/z to phi/theta
    res = mat1 @ mat2 @ mat3 @ xyz_mat
    theta = math.acos(res[2])
    try:
        temp_phi = math.acos(res[0] / math.sin(theta))
        return temp_phi, theta
    except:
        return phi, theta