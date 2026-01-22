from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from ultralytics import YOLO
import os

app = Flask(__name__)
CORS(app)

model = YOLO("yolov8n.pt")

def detect_parking_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)
    return lines

def detect_parking_slots(lines, image):
    slots = []
    if lines is not None:
        vertical_lines = [line for line in lines if abs(line[0][0] - line[0][2]) > abs(line[0][1] - line[0][3])]
        vertical_lines.sort(key=lambda line: line[0][0])
        for i in range(1, len(vertical_lines)):
            left_line = vertical_lines[i - 1][0]
            right_line = vertical_lines[i][0]
            x1 = left_line[0]
            x2 = right_line[0]
            y1 = 0
            y2 = image.shape[0]
            slots.append((x1, y1, x2, y2))
    return slots

def check_slot_availability(slot_area, car_boxes):
    for box in car_boxes:
        box = box.cpu().numpy() if isinstance(box, np.ndarray) else np.array(box)
        x1, y1, x2, y2 = map(int, box[:4])
        if (slot_area[0] < x2 and slot_area[2] > x1) and (slot_area[1] < y2 and slot_area[3] > y1):
            return False
    return True

@app.route('/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    file = request.files['image']
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    results = model(image)[0]
    lines = detect_parking_lines(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 255), 2)
    parking_slots = detect_parking_slots(lines, image)
    available_slots = []
    car_boxes = results.boxes.xyxy
    for i, box in enumerate(results.boxes.xyxy):
        x1, y1, x2, y2 = map(int, box[:4])
        conf = float(results.boxes.conf[i])
        cls = int(results.boxes.cls[i])
        label = f"Slot {i + 1}"
        for j, slot_area in enumerate(parking_slots):
            if check_slot_availability(slot_area, car_boxes):
                available_slots.append(j + 1)
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
            cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            if check_slot_availability(slot_area, car_boxes):
                cv2.rectangle(image, (slot_area[0], slot_area[1]), (slot_area[2], slot_area[3]), (0, 255, 0), 2)
    _, buffer = cv2.imencode('.jpg', image)
    base64_image = base64.b64encode(buffer).decode('utf-8')
    return jsonify({'image': base64_image, 'available_slots': available_slots})

if __name__ == '__main__':
    app.run(debug=True)
# .\venv\Scripts\activate