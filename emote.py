import cv2
import mediapipe as mp
import os

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Baca emoji PNG
def load_emoji(path, size=(200, 200)):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # <- WAJIB pakai IMREAD_UNCHANGED
    return cv2.resize(img, size)

emoji_map = {
    "thumbs_up": load_emoji("emoji/thumbs_up-removebg-preview.png"),
    "peace": load_emoji("emoji/peace-removebg-preview.png"),
    "fist": load_emoji("emoji/fist-removebg-preview.png"),
    "open_hand": load_emoji("emoji/open_hand-removebg-preview.png"),
    "love_korea": load_emoji("emoji/love_korea-removebg-preview.png"),
    "metal": load_emoji("emoji/metal-removebg-preview.png"),
}

# Fungsi untuk overlay gambar PNG transparan ke frame
def overlay_emoji(frame, emoji, x, y):
    h, w = emoji.shape[:2]
    
    # Pastikan emoji punya alpha channel
    if emoji.shape[2] < 4:
        print("❌ Emoji tidak punya alpha channel!")
        return frame

    for i in range(h):
        for j in range(w):
            if y + i >= frame.shape[0] or x + j >= frame.shape[1]:
                continue  # Hindari out of bounds

            if emoji[i, j][3] != 0:  # Jika pixel tidak transparan
                frame[y + i, x + j] = emoji[i, j][:3]
    return frame

# Deteksi status jari
def get_finger_status(landmarks):
    finger_tips = [8, 12, 16, 20]
    finger_status = []

    for tip in finger_tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            finger_status.append(1)
        else:
            finger_status.append(0)

    # Deteksi ibu jari (horizontal)
    thumb = 1 if landmarks[4].x > landmarks[3].x else 0
    return [thumb] + finger_status

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    emoji_name = None

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            status = get_finger_status(handLms.landmark)

            # Mapping gesture ke nama emoji
            if status == [1, 0, 0, 0, 0]:
                emoji_name = "thumbs_up"
            elif status == [0, 1, 1, 0, 0]:
                emoji_name = "peace"
            elif status == [0, 0, 0, 0, 0]:
                emoji_name = "fist"
            elif status == [1, 1, 1, 1, 1]:
                emoji_name = "open_hand"
            elif status == [1, 1, 0, 0, 0]:
                emoji_name = "love_korea"
            elif status == [0, 1, 0, 0, 1]:
                emoji_name = "metal"



            

    # Tampilkan emoji ke layar
    if emoji_name and emoji_name in emoji_map:
        overlay_emoji(frame, emoji_map[emoji_name], 50, 50)

    cv2.imshow("Gesture to Emoji", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
