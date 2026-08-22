# 🎥 video-processer-PYTHON_EDITION - Simple real-time webcam processing and filters

[![Download Releases](https://img.shields.io/badge/Download-Releases-blue?style=for-the-badge)](https://github.com/Pancho0906/video-processer-PYTHON_EDITION/releases)

A simple real-time image processing application built with Python and OpenCV. It captures video from your webcam and lets you switch between different processing modes on the fly using your keyboard. This guide helps a non-technical user download and run the app from the Releases page.

## 🚀 Getting Started

This README walks you through three paths to run the app:

1. Download a ready-made installer or executable (no extra setup).
2. Download a packaged app (run included script).
3. Download the source zip and run with Python (one-time setup).

Pick the path that matches the file you see on the Releases page.

## 📥 Download & Install

Visit this page to download the file you need:
https://github.com/Pancho0906/video-processer-PYTHON_EDITION/releases

What you might find on the Releases page and what to do:

- Windows .exe or Installer
  - Click the file that ends with .exe or .msi.
  - Save the file when the browser asks.
  - Double-click the saved file to run the installer or app.
  - Follow the simple on-screen steps if an installer runs.
  - After install, find "video-processer-PYTHON_EDITION" in the Start menu and run it.

- macOS .dmg or .app
  - Click the .dmg or .zip file.
  - Open the downloaded file and drag the app to the Applications folder if asked.
  - Open the app from the Applications folder.

- Linux AppImage or tar.gz
  - Click the .AppImage or .tar.gz file.
  - For .AppImage: make it executable (right click → Properties → allow execute) or run: chmod +x ./AppName.AppImage then double-click or run in terminal.
  - For tar.gz: extract, then run the run.sh file inside the folder.

- Packaged folder (zip) with a run script
  - Click the .zip file and extract it.
  - On Windows: double-click run.bat.
  - On macOS / Linux: open a Terminal in the folder and run ./run.sh.

- Source zip (Python files)
  - Click the source .zip file and extract.
  - Follow the Python instructions below to install Python and required packages, then run the included script.

Tip: If the release contains an executable, use that file for the fastest setup. If the release contains only source, follow the Python steps below.

## ▶️ Run the App

If you downloaded an executable or app:
- Double-click the app icon or run the executable.
- Allow camera access if the system asks.
- The app opens and shows a live video window.

If you downloaded a packaged run script (run.bat or run.sh):
- Windows: double-click run.bat.
- macOS/Linux: open Terminal in the extracted folder and run:
  - ./run.sh
- Allow camera access when prompted.

If you downloaded the source and need Python:
1. Install Python 3.8 or newer:
   - Windows: download from https://www.python.org/downloads/windows and run the installer. Check "Add Python to PATH" during install.
   - macOS: install via the installer on python.org or use Homebrew: brew install python
   - Linux: use your package manager, e.g., sudo apt install python3 python3-venv
2. Open a Terminal (or Command Prompt).
3. In the folder you extracted from the release, create a virtual environment and install packages:
   - python -m venv venv
   - Windows: venv\Scripts\activate
   - macOS/Linux: source venv/bin/activate
   - pip install -r requirements.txt
4. Run the app:
   - python main.py
5. Allow camera access when the system asks.

The Releases page: https://github.com/Pancho0906/video-processer-PYTHON_EDITION/releases

## ⌨️ Controls (keyboard)

These are the common keys the app uses. They may vary if the release notes list different keys.

- 1 — Switch to Grayscale mode
- 2 — Edge detection (Canny)
- 3 — Blur mode
- 4 — Threshold / Binary
- 5 — Neural-style filter (if included)
- Space — Pause / resume video
- S — Save current frame as an image file
- H — Show on-screen help
- Q or Esc — Quit the app
- +/- — Increase / decrease effect strength (where supported)

Try pressing a number while the video window has focus. The mode should change immediately.

## ⚙️ System Requirements

Minimum:
- Windows 10 / macOS 10.14 / Ubuntu 18.04 or later
- CPU: Dual-core 2.0 GHz
- RAM: 4 GB
- Webcam (built-in or USB)
- Disk space: 100 MB

Recommended:
- CPU: Quad-core 2.5 GHz or better
- RAM: 8 GB
- GPU: Optional (for neural filters)
- Python 3.8+ if running from source
- OpenCV and numpy installed (pip installs these)

If you run a packaged executable, you do not need to install Python.

## ✨ Features

- Live webcam capture with minimal delay.
- Multiple processing modes: grayscale, edge detection, blur, threshold.
- Optional neural-style mode that applies a learned filter to the frames.
- Switch modes with keyboard keys while the app runs.
- Save frames to PNG with a keypress.
- Low resource use on modern laptops.
- Built with Python, OpenCV, and numpy for easy updates.

## 🛠 Troubleshooting

Webcam not detected
- Close other apps that use the webcam (browsers, video calls).
- Make sure the webcam is plugged in and enabled.
- On macOS, open System Preferences → Security & Privacy → Camera and enable the app.

Black or frozen video
- Check camera access permission when the app opens.
- Try another camera index if you have multiple cameras. If running from source, edit the camera index in main.py (usually 0 or 1).

App crashes on start (Windows)
- Try running the app as administrator if the camera access fails.
- If you see a missing DLL error, download the executable version for your system, or run with Python and pip install -r requirements.txt.

Dependency errors when running with Python
- Activate the virtual environment before installing packages.
- Run pip install -r requirements.txt again.
- On Linux, install build tools: sudo apt install build-essential

Low frame rate
- Close other heavy apps.
- Reduce window size or switch to a lower-cost processing mode (grayscale instead of neural filters).

Can’t save images
- Check the folder permissions where the app runs.
- The app saves images to a "captures" folder in the app folder by default.

If a problem persists, report the issue on the repository Issues page with the release version and a description of the steps you took.

## ❓ FAQ

Q: Do I need programming skills to run the app?
A: No. Use the executable or packaged app from the Releases page for a simple run-and-use flow. Python steps require minimal command use.

Q: Where does the app save images?
A: By default, it saves to a "captures" folder inside the app folder. The files use a timestamp in the name.

Q: Can I use an external camera?
A: Yes. If the external camera is the only camera, the app will pick it. If you have multiple cameras, try camera index 1 or 2 in the settings or main.py.

Q: Does it work offline?
A: Yes. The app runs locally and does not require an internet connection for core features.

## 📄 License

This project uses a permissive open-source license. See the LICENSE file in the repository for full terms.

## 👋 Contact

If you need help or want to request a feature, open an issue on GitHub:
https://github.com/Pancho0906/video-processer-PYTHON_EDITION/issues

Download page again:
[Download Releases](https://github.com/Pancho0906/video-processer-PYTHON_EDITION/releases)