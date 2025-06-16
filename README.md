# 🖐️ Hand Gesture to Emoji Recognition using OpenCV & MediaPipe

Proyek ini adalah aplikasi Python yang mendeteksi gesture tangan menggunakan webcam, lalu menampilkan emoji yang sesuai berdasarkan gerakan jari. Dibangun menggunakan `OpenCV`, `MediaPipe`, dan `cv2`.


## ✨ Fitur
- Deteksi real-time gesture tangan dengan webcam
- Tampilkan emoji sesuai gesture (misal: 👍 ✌️ ✊ 🤟)
- Dukungan alpha channel PNG (transparan)
- Custom emoji bisa ditambahkan dengan mudah

## 🛠️ Teknologi
- Python 3
- OpenCV
- MediaPipe
- (Optional) TensorFlow / DeepFace (jika kamu gabungkan dengan deteksi wajah)

## 🖼️ Gesture yang Didukung

| Gesture       | Emoji         |
|---------------|---------------|
| Thumbs Up     | 👍             |
| Peace         | ✌️             |
| Fist          | ✊             |
| Open Hand     | 🖐️             |
| Korean Love   | ❤️ (dua jari) |
| Metal Rock    | 🤘             |

## 📂 Struktur Folder

facepy/
├── emoji/
│ ├── thumbs_up.png
│ ├── peace.png
│ ├── fist.png
│ └── ...
├── main.py # (opsional) deteksi ekspresi wajah
├── emote.py # gesture ke emoji
└── README.md

bash
Copy
Edit

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
2. Buat Virtual Environment
bash
Copy
Edit
python -m venv facepy_env
.\facepy_env\Scripts\activate  # Windows
3. Install Dependensi
bash
Copy
Edit
pip install -r requirements.txt
Atau jika belum ada requirements.txt, jalankan:

bash
Copy
Edit
pip install opencv-python mediapipe
4. Jalankan Program
bash
Copy
Edit
python emote.py
Tekan q untuk keluar dari aplikasi.

🧠 Catatan
Pastikan emoji PNG memiliki alpha channel (format transparan).

Jika emoji tidak muncul atau hanya tanda tanya, pastikan gambar bisa dibaca oleh cv2.imread dan berada di path yang benar.

🧑‍💻 Kontribusi
Silakan fork dan PR jika ingin menambahkan gesture baru, fitur lanjutan (seperti ekspresi wajah), atau peningkatan performa.

📄 Lisensi
MIT License © 2025 Dion Ahza
