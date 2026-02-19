import cv2
import mediapipe as mp
import numpy as np
import joblib

# -------------------------------
# Load your trained model & label encoder
# -------------------------------
model = joblib.load("./xgb_hand_gesture_model.pkl")
le = joblib.load("./label_encoder.pkl")

# -------------------------------
# Initialize MediaPipe Hands
# -------------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# -------------------------------
# Start webcam capture
# -------------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert to RGB for MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Extract landmarks
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            landmarks = np.array(landmarks)

            # -------------------------------
            # Preprocessing: translation + scale
            # -------------------------------
            landmarks = landmarks.reshape(21,3)
            wrist = landmarks[0]
            landmarks = landmarks - wrist
            middle_tip = landmarks[12]
            ref_length = np.linalg.norm(middle_tip)
            if ref_length == 0:
                ref_length = 1e-6
            landmarks = (landmarks / ref_length).flatten().reshape(1,-1)

            # -------------------------------
            # Predict gesture
            # -------------------------------
            pred_number = model.predict(landmarks)[0]
            pred_label = le.inverse_transform([pred_number])[0]

            # -------------------------------
            # Draw prediction on frame
            # -------------------------------
            cv2.putText(frame, pred_label, (50,50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0,255,0), 2)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show video
    cv2.imshow("Hand Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
