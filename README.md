# 🚗 Parking Space Detection System

A web-based Parking Space Detection System that detects parking slots and identifies whether they are **occupied or available** using **computer vision and deep learning**.

The system consists of a **Flask backend** integrated with a **YOLOv8 model** and a **frontend dashboard** built using HTML, CSS, and JavaScript.

---

## 📌 Features

- 🔍 Detects parking spaces from images
- 🚘 Identifies whether a parking slot is **occupied or empty**
- 🟥 Marks occupied slots in **red**
- 🟩 Marks available slots in **green**
- 🖥️ Web-based dashboard to upload images and view results
- 📊 Displays number of free parking slots
- ⚡ Fast and efficient detection using YOLOv8

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- OpenCV
- YOLOv8 (Ultralytics)
- NumPy

### Frontend
- HTML
- CSS
- JavaScript

---
## 📁 Project Structure
app/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── processed/
│
├── frontend/
│ ├── index.html
│ ├── dashboard.html
│ ├── script.js
│ └── style.css
│
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Aaish48/Parking-project-backend.git
cd Parking-project-backend
2️⃣ Create and activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r backend/requirements.txt

4️⃣ Run the Flask server
cd backend
python app.py


Server will start at:

http://127.0.0.1:5000

5️⃣ Open the Frontend

Open frontend/index.html in your browser.

🧪 How It Works

User uploads a parking image from the dashboard

Image is sent to the Flask backend

YOLOv8 model detects cars and parking slots

Backend processes and marks slots as occupied or free

Output image and statistics are displayed on the dashboard

🚫 Ignored Files

The following files are ignored using .gitignore:

venv/

YOLO model files (*.pt)

Processed images

.env file

🚀 Future Enhancements

Real-time parking detection using live video feed

Mobile-friendly UI

Database integration for parking history

Map-based parking visualization

Slot number labeling with availability list

👨‍💻 Author

Aaish

GitHub: https://github.com/Aaish48

📜 License

This project is for educational purposes.


---

## ✅ How to add it to GitHub

```powershell
git add README.md
git commit -m "Add README file"
git push

## 📁 Project Structure

