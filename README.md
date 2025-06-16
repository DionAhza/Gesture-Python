# 🖐️ Hand Gesture to Emoji Recognition using OpenCV & MediaPipe

Proyek ini adalah aplikasi Python yang mendeteksi gesture tangan menggunakan webcam, lalu menampilkan emoji yang sesuai berdasarkan gerakan jari. Dibangun menggunakan `OpenCV`, `MediaPipe`, dan `cv2`.

## ✨ Fitur

- ✅ Deteksi real-time gesture tangan dengan webcam
- ✅ Menampilkan emoji sesuai gesture (misal: 👍 ✌️ ✊ 🤟)
- ✅ Dukungan alpha channel PNG (transparan)
- ✅ Custom emoji bisa ditambahkan dengan mudah

## 🛠️ Teknologi

- Python 3
- OpenCV
- MediaPipe
- (Opsional) TensorFlow / DeepFace (jika digabung dengan deteksi ekspresi wajah)

## 🖼️ Gesture yang Didukung

| Gesture       | Emoji          |
|---------------|----------------|
| Thumbs Up     | 👍              |
| Peace         | ✌️              |
| Fist          | ✊              |
| Open Hand     | 🖐️              |
| Korean Love   | ❤️ (dua jari)  |
| Metal Rock    | 🤘              |

## 📂 Struktur Folder

```
facepy/
├── emoji/
│   ├── thumbs_up.png
│   ├── peace.png
│   ├── fist.png
│   └── ...
├── main.py      # (opsional) deteksi ekspresi wajah
├── emote.py     # gesture ke emoji
├── requirements.txt
└── README.md
```

## 🚀 Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/DionAhza/Gesture-Python.git
cd Gesture-Python
```

### 2. Buat Virtual Environment

```bash
python -m venv facepy_env
.\facepy_env\Scripts\activate  # untuk Windows
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

> Jika belum ada `requirements.txt`, kamu bisa install manual:

```bash
pip install opencv-python mediapipe
```

### 4. Jalankan Program

```bash
python emote.py
```

> Tekan `q` untuk keluar dari aplikasi.

## 🧠 Catatan

- Pastikan gambar emoji PNG memiliki **alpha channel** (transparan), gunakan format `.png`.
- Jika emoji tidak muncul atau muncul tanda tanya:
  - Pastikan file berada di folder `emoji/`
  - Nama file dan ekstensi benar
  - Gunakan `cv2.IMREAD_UNCHANGED` saat memuat PNG

## 🧑‍💻 Kontribusi

Silakan fork dan buat pull request jika ingin:
- Menambahkan gesture baru
- Menambahkan deteksi ekspresi wajah
- Meningkatkan akurasi atau fitur lainnya

## 📄 Lisensi

MIT License © 2025 [Dion Ahza](https://github.com/DionAhza)
