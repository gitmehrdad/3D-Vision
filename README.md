# 3D Vision

A repository for studying **3D vision techniques**, covering **theory**, **algorithms**, and **hands-on implementations** of key methods.

---

## Camera Calibration

Camera calibration is the process of estimating the **intrinsic parameters** of a camera that determine how 3D points in the real world are projected onto a 2D image.

### Objectives

1. **Correct Lens Distortion**

   In an ideal camera, straight lines in the real world appear straight in the image. In practice, lenses introduce distortion, most commonly:

   - **Barrel Distortion**  
     Straight lines bend outward (typical for wide-angle lenses).

   - **Pincushion Distortion**  
     Straight lines bend inward (typical for telephoto lenses).

2. **Estimate the Intrinsic Camera Matrix**

   The intrinsic matrix \( K \) contains the internal camera parameters:

   - **Focal Length (`fx`, `fy`)**  
     Controls how strongly the camera focuses light.

   - **Optical Center (`cx`, `cy`)**  
     The point where the principal ray intersects the image sensor.  
     This is usually close to, but not exactly at, the image center.

---

## RTSP Camera Calibration Procedure

We calibrate **two cameras streaming over RTSP** using a checkerboard pattern.

### Step 1: Prepare the Checkerboard

- Download a checkerboard pattern and print it on a **flat, rigid surface**.
- We used a **7 × 5** inner-corner checkerboard.

### Step 2: Measure Square Size

- Measure the side length of **one square** in **millimeters**.
- Update the following lines in `Calibrate.py`:
  - **Line 73**
  - **Line 74**

### Step 3: Configure RTSP Streams

- Update the RTSP URLs in `Capture.py`:
  - **Line 122**
  - **Line 123**

### Step 4: Capture Calibration Images

Run:

```bash
python Capture.py
