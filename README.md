```markdown
# Keylogger

A simple Python-based keylogger that records keyboard inputs and saves them to a log file for monitoring purposes.

---

## Features
- Logs all keyboard inputs, including alphanumeric keys and special keys.
- Saves keystrokes to a `log.txt` file.
- Appends a space for every spacebar press for better readability.
- Lightweight and easy to use.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `pynput` library (`pip install pynput`)

---

## How It Works
1. Captures all keystrokes using the `pynput` library.
2. Saves the captured inputs to a text file (`log.txt`).
3. Ignores special keys except the spacebar.

---

## Installation
1. Clone the repository or download the script.
2. Install the required library:
   ```bash
   pip install pynput
   ```

---

## Usage
1. Run the script:
   ```bash
   python keylogger.py
   ```
2. Press keys on your keyboard. The inputs will be logged to `log.txt` in the same directory.

3. To stop the keylogger, press the **Esc** key.

---

## Disclaimer
This keylogger is intended for educational and ethical purposes only. Unauthorized use to monitor others without their consent is illegal and unethical. Use responsibly!

---
