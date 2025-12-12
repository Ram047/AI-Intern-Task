def process_video(input_path, output_path="output.mp4"):
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(5)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    pose_detector = PoseEstimator()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        keypoints = pose_detector.get_keypoints(frame)
        if keypoints:
            feedback, angle = evaluate_form(keypoints)

            # Draw angle
            cv2.putText(frame, f"Elbow Angle: {int(angle)} deg", (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw feedback
            y0 = 80
            for msg in feedback:
                cv2.putText(frame, msg, (30, y0),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                y0 += 30

            mp_drawing.draw_landmarks(
                frame, pose_detector.pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).pose_landmarks,
                mp_pose.POSE_CONNECTIONS)

        out.write(frame)

    cap.release()
    out.release()
    print("Processing complete. Output saved as", output_path)
