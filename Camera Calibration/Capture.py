# ********************* Camera Calibration Version 1.0 ********************* #
# ************************ Author: Mehrdad Morsali ************************* #
# ************************ mehrdadmorsali@gmail.com ************************ #
# ************************************************************************** #

import cv2
import os
import threading
import numpy as np

class CameraStream:
    """A class to handle reading from an RTSP stream in a separate thread."""
    def __init__(self, src=0):
        # Initialize the video capture object
        self.cap = cv2.VideoCapture(src, cv2.CAP_FFMPEG)
        self.ret = False
        self.frame = None
        self.read_thread = None  
        self.stopped = False

        if not self.cap.isOpened():
            print(f"Error: Could not open video stream")
            return

        # Reduce internal buffer size to 1 for low latency
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        # Read the first frame
        self.ret, self.frame = self.cap.read()

        # Only create thread if cap is valid
        self.read_thread = threading.Thread(target=self.update, args=())
        self.read_thread.daemon = True

    def start(self):
        """Starts the background thread."""
        if self.read_thread is not None:
            self.stopped = False
            self.read_thread.start()
        else:
            print("Cannot start stream: VideoCapture failed to open.")

    def update(self):
        """The main loop of the thread that continuously reads frames."""
        while not self.stopped:
            self.ret, self.frame = self.cap.read()
            if not self.ret:
                print("Warning: Frame read failed. Stopping stream.")
                self.stop()
                break

    def read(self):
        """Returns the most recent frame read by the background thread."""
        return self.ret, self.frame

    def stop(self):
        """Signals the thread to stop and cleans up resources."""
        self.stopped = True
        if self.read_thread is not None and self.read_thread.is_alive():
            self.read_thread.join(timeout=1.0)  # Slightly longer timeout
        if hasattr(self, 'cap') and self.cap.isOpened():
            self.cap.release()
        
def capture_images(output_dir, rtsp_url_1, rtsp_url_2):
    stream_1 = CameraStream(rtsp_url_1)
    stream_2 = CameraStream(rtsp_url_2)
    
    if stream_1.cap is None or not stream_1.cap.isOpened():
        print("Failed to initialize camera stream 1. Exiting.")
        return
        
    if stream_2.cap is None or not stream_2.cap.isOpened():
        print("Failed to initialize camera stream 2. Exiting.")
        return    
        

    stream_1.start()
    stream_2.start()
    
    print("--- Starting Image Capture ---")
    print("Press 'c' to capture image.")
    print("Press 'q' to quit.")
    
    img_count = 0
    while True:
        ret_1, frame_1 = stream_1.read()
        ret_2, frame_2 = stream_2.read()
        
        if not ret_1:
            print("Error: Can't receive frame from camera 1")
            break
        
        if not ret_2:
            print("Error: Can't receive frame from camera 2")
            break
         
        # Combine the frames horizontally
        frame = np.hstack((frame_1, frame_2))
         
        cv2.imshow('GitMehrdad 3D Vision - Capture Images', frame)
              
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            filename_1 = os.path.join(output_dir, f'camera1_{img_count}.jpg')
            filename_2 = os.path.join(output_dir, f'camera2_{img_count}.jpg')
            cv2.imwrite(filename_1, frame_1)
            cv2.imwrite(filename_2, frame_2)
            
            img_count += 1
            print(f"Captured image number {img_count}")
            
    stream_1.stop()
    stream_2.stop()
    
    cv2.destroyAllWindows()
    print(f"Finished capturing {img_count} images.")

if __name__ == '__main__':    
    # Camera Configuration
    rtsp_url_1 = 'link to camera 1'
    rtsp_url_2 = 'link to camera 2'   
    output_dir = 'calibration_images'
    os.makedirs(output_dir, exist_ok=True)
    
    # Capture Camera frames
    capture_images(output_dir, rtsp_url_1, rtsp_url_2)
    
