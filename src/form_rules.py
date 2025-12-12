def evaluate_form(keypoints):
    feedback = []

    ls = keypoints["left_shoulder"]
    le = keypoints["left_elbow"]
    lw = keypoints["left_wrist"]
    lh = keypoints["left_hip"]
    rs = keypoints["right_shoulder"]

    # 1) Bicep Curl Elbow Angle
    elbow_angle = calculate_angle(ls, le, lw)
    if elbow_angle < 40:
        feedback.append("Curl too high – reduce contraction.")
    elif elbow_angle > 160:
        feedback.append("Arm too extended – don't lock out elbow.")
    else:
        feedback.append("Elbow angle is correct.")

    # 2) Lateral Raise – wrist aligned with shoulders
    shoulder_line = abs(lw[1] - ls[1])
    if shoulder_line <= 20:
        feedback.append("Good wrist–shoulder alignment.")
    else:
        feedback.append("Incorrect alignment – keep wrist level with shoulders.")

    # 3) Back Posture Symmetry (shoulder–hip vertical line)
    back_angle = abs(ls[0] - lh[0])  # horizontal offset
    if back_angle > 25:
        feedback.append("Leaning detected – keep back straight.")
    else:
        feedback.append("Back posture looks good.")

    return feedback, elbow_angle

