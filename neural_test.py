from pyray import *
import numpy as np
import random

init_window(1920, 1080, "Pyray Data")
set_target_fps(60)

camera = Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

COLORS = [RED, YELLOW, ORANGE, GREEN, BLUE, PURPLE]

def createBlob(num_points, seed=0,scaling_factor=10):
    np.random.seed(seed)

    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    z = np.random.rand(num_points)

    # Calculate the mean of each axis
    mean_x, mean_y, mean_z = np.mean(x), np.mean(y), np.mean(z)

    # Translate the blob to the origin
    x -= mean_x
    y -= mean_y
    z -= mean_z

    # Scale the coordinates
    x *= scaling_factor
    y *= scaling_factor
    z *= scaling_factor

    # Translate the blob back to its original position
    x += mean_x
    y += mean_y
    z += mean_z

    return x, y, z

num_blobs = 4
color = random.sample(COLORS, num_blobs)

while not window_should_close():
    update_camera(camera, CAMERA_ORBITAL)
    begin_drawing()
    clear_background(RAYWHITE)
    begin_mode_3d(camera)

    for blob_idx in range(num_blobs):
        n_points = 50
        x, y, z = createBlob(n_points, seed=blob_idx)
        x += blob_idx * 2
        y += blob_idx * 2
        z += blob_idx * 2

        for i in range(n_points):
            draw_cube(Vector3(x[i], y[i], z[i]), 0.2, 0.2, 0.2, color[blob_idx])

    draw_grid(20, 1.0)
    end_mode_3d()
    draw_text("Numpy Blob 3D dataset", 190, 200, 30, BLACK)
    end_drawing()
close_window()

