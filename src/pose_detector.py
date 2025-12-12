mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

class PoseEstimator:
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

        # For smoothing
        self.l_elbow_buffer = []
        self.l_shoulder_buffer = []
        self.l_wrist_buffer = []
        self.l_hip_buffer = []

    def get_keypoints(self, image):
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(img_rgb)

        if not results.pose_landmarks:
            return None

        h, w = image.shape[:2]
        landmarks = results.pose_landmarks.landmark

        keypoints = {
            "left_shoulder": (int(landmarks[11].x * w), int(landmarks[11].y * h)),
            "left_elbow": (int(landmarks[13].x * w), int(landmarks[13].y * h)),
            "left_wrist": (int(landmarks[15].x * w), int(landmarks[15].y * h)),
            "left_hip": (int(landmarks[23].x * w), int(landmarks[23].y * h)),
            "right_shoulder": (int(landmarks[12].x * w), int(landmarks[12].y * h)),
        }

        # Smoothing
        keypoints["left_elbow"] = smooth_keypoints(self.l_elbow_buffer, keypoints["left_elbow"])
        keypoints["left_shoulder"] = smooth_keypoints(self.l_shoulder_buffer, keypoints["left_shoulder"])
        keypoints["left_wrist"] = smooth_keypoints(self.l_wrist_buffer, keypoints["left_wrist"])
        keypoints["left_hip"] = smooth_keypoints(self.l_hip_buffer, keypoints["left_hip"])

        return keypoints
