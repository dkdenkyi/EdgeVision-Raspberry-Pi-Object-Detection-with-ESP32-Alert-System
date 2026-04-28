
import cv2
import numpy as np
import time
import paho.mqtt.client as mqtt

# ---------------- MQTT SETUP ----------------
client = mqtt.Client()
client.connect("localhost", 1883, 60)

# prevent spamming messages continuously
last_sent_time = 0
COOLDOWN = 2  # seconds

def trigger_mqtt():
    client.publish("camera/events", "tvmonitor detected")


# ---------------- LOAD MODEL ----------------
net = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt",
    "mobilenet_iter_73000.caffemodel"
)

# ---------------- CLASS LABELS ----------------
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

print("Starting detection... Press ESC to exit.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w = frame.shape[:2]

        blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        tvmonitor_detected = False

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > 0.5:
                idx = int(detections[0, 0, i, 1])
                label = CLASSES[idx]

                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x1, y1, x2, y2) = box.astype("int")

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label}: {confidence:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)

                # ---------------- TARGET OBJECT ----------------
                if label == "tvmonitor":
                    tvmonitor_detected = True

        # ---------------- MQTT TRIGGER ----------------
        current_time = time.time()

        if tvmonitor_detected and (current_time - last_sent_time > COOLDOWN):
            trigger_mqtt()
            last_sent_time = current_time
            print("MQTT: tvmonitor detected → message sent")

        # Show frame
        cv2.imshow("Object Detection", frame)

        # Exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    client.disconnect()
