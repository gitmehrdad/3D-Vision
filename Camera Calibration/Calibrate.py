# ********************* Camera Calibration Version 1.0 ********************* #
# ************************ Author: Mehrdad Morsali ************************* #
# ************************ mehrdadmorsali@gmail.com ************************ #
# ************************************************************************** #

import numpy as np
import cv2
import os
import glob
import time

def calibrate_camera(checkerboard_dims, square_width, square_height, camera_name):
    """Performs calibration using captured images and non-square checkerboard logic."""
    print(f"--- Starting {camera_name} Calibration ---")

    images = glob.glob(os.path.join('calibration_images', f'{camera_name}*.jpg'))
    if not images:
        print(f"No images found for {camera_name} calibration. Exiting.")
        return
        
    print(f"Found {len(images)} images to process...")
    
    # Create the idealized 3D object points
    objp = np.zeros((checkerboard_dims[0] * checkerboard_dims[1], 3), np.float32)
    # Generate a grid of indices (0,0), (1,0), ... (0,1), (1,1), ...
    grid_indices = np.mgrid[0:checkerboard_dims[0], 0:checkerboard_dims[1]].T.reshape(-1, 2)
    # Multiply by the physical size of the squares
    objp[:, :2] = grid_indices * np.array([square_width, square_height])

    objpoints = []  # 3D points
    imgpoints = []  # 2D points

    gray_shape = None
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_shape = gray.shape[::-1]

        ret, corners = cv2.findChessboardCorners(gray, checkerboard_dims, None)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
        else:
            print(f"Corners NOT found in: {os.path.basename(fname)}")

    if not objpoints:
        print(f"{camera_name} Calibration failed: No corners were detected in any image.")
        return

    print("Running calibration algorithm...")
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_shape, None, None)

    if ret:
        output_file = f'{camera_name}_calibration_data.npz'
        print("--- Calibration Successful! ---")
        print(f"Camera Matrix for '{camera_name}':")
        print(mtx)
        print(f"Distortion Coefficients for '{camera_name}':")
        print(dist)
        
        np.savez(output_file, camera_matrix=mtx, dist_coeffs=dist, cam_name=camera_name)
        print(f"\nCalibration data saved to '{output_file}'")
    else:
        print("\n--- Calibration Failed. ---")


if __name__ == '__main__':
    # Number of inner corners of the checkerboard (width, height)
    checkerboard_dims = (4, 6)
    # Manually measured dimension of rectangles (millimeters)
    square_width = 53.0           
    square_height = 53.0          
    
    calibrate_camera(checkerboard_dims, square_width, square_height, "camera1")
    calibrate_camera(checkerboard_dims, square_width, square_height, "camera2")

