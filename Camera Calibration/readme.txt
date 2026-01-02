
Here is the Procedure
Step 1: Find a checkerboard pattern online and print it on a flat board. We used a pattern with 7x5 squares.
Step 2: measure the length of one square in millimeters. Update line 73 and line 74 of the code in Calibrate.py based on your measurements.
Step 3: Update line 122 and line 123 of the code in Capture.py with the rtsp links to your camera. 
Step 4: Run Capture.py. A window will pop up showing your live camera feed. Press the c key to capture and save a frame. When you are done, Press the q key to quit the capture phase. The code creates a directory calibration_images and save images to it. 

During capturing, move the checkerboard pattern in front of the camera following these instruction:

Vary the Angle: Tilt the board forward, backward, left, and right.
Vary the Distance: Capture images with the board close to the camera and far away.
Cover the Edges: Make sure to capture images where the board is in the corners and along the edges of the video frame. This is where lens distortion is greatest.
Keep it Sharp: Ensure the checkerboard is in focus and not blurry from motion.


Step 5: Run Calibrate.py. The script will automatically find the images in the calibration_images folder. It will process them, find the corners, and calculate the camera matrix and distortion coefficients. The results will be printed to your terminal and saved in a file.

After running the script, you will have two important outputs:

camera_calibration_data.npz: This file contains the results. You can load it in other Python scripts to correct your live video in real-time.
camera_matrix: The intrinsic matrix of the camera (K).
dist_coeffs: The distortion parameters.
undistorted_example.jpg: An image file showing one of your captured frames before and after distortion correction, proving that the calibration worked.










Press q to quit and begin calibration.
The script will process the images and save the results to main_cam_calibration_data.npz.
Calibrate Camera 2 (e.g., "side_cam"):
Update the CAMERA_CONFIG dictionary with the details for your second camera.
Run the script again, but this time specifying the second camera's name:
Bash

Copy
python advanced_calibrate.py --camera_name side_cam
The process is identical, but this time it will use a calibration_images_side_cam/ folder and save the results to side_cam_calibration_data.npz.
You now have two separate, clearly named files containing the unique calibration data for each camera.