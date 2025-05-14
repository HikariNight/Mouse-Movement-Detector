# 🖱️ Mouse Movement Detector (MMD)

> A minimalist desktop app that tells you when your mouse is moving... and how *much*.
> Whether you're testing input devices, monitoring idle time, or just curious, MMD has you covered.

---

## 🎯 What is MMD?

**Mouse Movement Detector (MMD)** is a lightweight Python application that monitors and counts your mouse movements in real-time. Using a clean and simple **CustomTkinter GUI**, this app visually indicates whether your cursor is active — down to the millisecond — and how long it's been in motion.

Perfect for:

* Testing custom mice or sensors
* Creating idle-time-based workflows
* Simple desktop experiments
* Debugging ghost mouse issues 👻🖱️

---

## ✨ Features

* 🔍 Real-time mouse movement detection (with millisecond accuracy)
* 🟢🟥 Color-coded status indicator (Green = Has not moved, Red = Has moved)
* ⏱️ Instant display of **Duration of Mouse Movement (DoMM)** in ms
* 🧼 Minimal, modern interface using **CustomTkinter**
* ⚙️ Keyboard shortcut support (F7 to Start, F8 to Stop)
* 📸 Custom window icon for extra style points

---

## 📸 Sneak Peek

![image](https://github.com/user-attachments/assets/a1896927-4690-45b0-974e-d4c235911c78)


---

## 🚀 Getting Started

### 🧠 Keyboard Controls

* **F7** – Start Detection
* **F8** – Stop Detection

---

## 🛠️ Under the Hood

The app works by continuously checking your mouse position and comparing it to the previous location. If the position has changed, it counts that as movement (down to the ms). This loop runs every **1 millisecond**, ensuring high accuracy.

Here’s how the detection logic works:

```python
savedpos = win32api.GetCursorPos()
if savedpos != curpos:
    count += 1
```

When detection stops, the app gives visual feedback:

* **Green** means your mouse stayed still
* **Red** means there was movement

---

## 📁 Assets

* **Icon Image** – Located in `/assets/SEYANAAAAA.JPG`
  Make sure the image is present to avoid errors.

---

## 🎨 GUI Snapshot

* Built using **CustomTkinter** with a "green" theme for a slick, modern look
* Non-resizable window (316x252) keeps things compact and focused

---

## 📌 Note

This app currently supports **Windows only**, due to its use of `win32api` and `keyboard`.

---

## 💬 Final Words

Whether you're experimenting or just curious about your idle time, **MMD** gives you insight into your cursor's every move.

> Because even the smallest twitch matters.
