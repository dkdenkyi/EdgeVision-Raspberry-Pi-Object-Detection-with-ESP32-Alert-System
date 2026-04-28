# 📡 EdgeVision: Raspberry Pi Object Detection with ESP32 Alert System

Real-time object detection system running on Raspberry Pi that triggers hardware alerts on an ESP32 via MQTT when a specific object is detected.

---

## 🚀 Overview
This project demonstrates an edge AI + IoT pipeline where a Raspberry Pi performs real-time object detection using a USB camera. When a predefined object is detected, a message is sent via MQTT to an ESP32 which triggers an LED alert.

---

## 🧠 Key Features
- Real-time object detection
- MQTT-based communication
- ESP32 hardware alert (LED)
- Edge AI processing (no cloud required)

---

## 🏗️ Architecture

![Architecture](docs/architecture.png)

---

## ⚙️ Setup
```bash
## Download Model

cd models

wget https://github.com/chuanqi305/MobileNet-SSD/raw/master/MobileNetSSD_deploy.caffemodel
wget https://github.com/chuanqi305/MobileNet-SSD/raw/master/MobileNetSSD_deploy.prototxt

pip install -r requirements.txt
python src/detector.py
```

---

## 🔌 MQTT Setup
```bash
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
```

---

## 🔧 ESP32
Upload `esp32/led_control.ino` and configure WiFi + MQTT.

---

## ⚡ Workflow
Camera → Raspberry Pi → Detection → MQTT → ESP32 → LED

---

## 📌 Author
dkdenkyi
