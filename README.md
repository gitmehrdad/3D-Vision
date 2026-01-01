# 3D Vision
A repository for studying 3D vision techniques — covering theory, algorithms, and hands-on implementations of key methods.

## Camera Calibration
Camera calibration is the process of finding the intrinsic properties of a camera that affect how it forms an image. 
The main goals are to:
 1. Correct for Lens Distortion: In a perfect camera, straight lines in the real world would appear as straight lines in the image. However, lenses introduce distortions. The most common are:
	 - Barrel Distortion: Straight lines bend outwards, like on a barrel. Common in wide-angle lenses.
	 - Pincushion Distortion: Straight lines bend inwards. Common in telephoto lenses.
 2. Find the Intrinsic Matrix: This matrix contains the camera's internal parameters:
	 - Focal Length (fx, fy): How strongly the camera converges light.
	 - Optical Center (cx, cy): The point where the "principal ray" hits the image sensor. It's often close to, but not exactly, the center of the image.

We want to calibrate two cameras that are streaming over RTSP.
