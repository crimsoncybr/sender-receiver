# 📁 Python File Transfer (Socket)

This project demonstrates how to send and receive files over TCP using Python's built-in `socket` module.

## 🚀 How It Works

- **Sender** (`sender.py`) connects to the server and sends:
  - File name
  - File size
  - File content (in chunks)
  - A custom `<END>` marker to signal completion

- **Receiver** (`receiver.py`) listens for a connection, reads the metadata and file content, and saves it to disk with a progress bar.

## 🛠️ Requirements

- Python 3.x
- `tqdm` module (for progress bar)  
  Install it using:
  pip install tqdm

## ▶️ Usage

1. Run `receiver.py` first to start listening.
2. Run `sender.py` and choose a file when prompted.

✅ Works on `localhost` (127.0.0.1).  
🌐 You can update the IP to transfer files across a LAN.

## 📌 Features

- Supports any file type (PDF, images, binary, etc.)
- Shows real-time progress while receiving
- Easy to understand and extend

---

![Screenshot 2025-03-23 223233](https://github.com/user-attachments/assets/c608b011-8d1d-4c52-80bd-17cc22da06ca)
