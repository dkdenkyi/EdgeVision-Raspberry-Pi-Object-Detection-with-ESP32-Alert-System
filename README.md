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
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

---

## 🔧 ESP32
- Open esp32/led_control.ino in Arduino IDE
- Install required libraries (WiFi, PubSubClient)

- Update:
    WiFi credentials
    MQTT broker IP
    Topic name

- Upload code to ESP32.


---

## ⚡ Workflow
Camera → Raspberry Pi → Detection → MQTT → ESP32 → LED

---

## 🔮 Future Improvements

This system can be enhanced by fine-tuning the object detection model on a custom dataset to improve accuracy for domain-specific objects and reduce false detections. Performance can also be improved by optimizing inference for Raspberry Pi using lighter architectures or hardware acceleration (e.g., OpenCV optimizations or TensorFlow Lite conversion). 

## 📌 Author
dkdenkyi
