# Exercise Form Evaluation Using Pose Estimation

This project detects human pose using MediaPipe and evaluates exercise form using rule-based geometric logic.

## Features
- Pose keypoint extraction using MediaPipe
- Elbow angle estimation
- Shoulder–wrist alignment checking
- Back posture rule
- Frame-wise feedback overlay
- MLflow-ready structure

## How to Run
1. Install requirements:
   pip install -r requirements.txt

2. Place your input video in `sample_video/input.mp4`

3. Run:
   python src/process_video.py

4. Output will be saved as:
   sample_video/output_with_feedback.mp4

## Repo Structure
(Include the same folder structure shown earlier)
