# Face Recognition Login & Registration System 🔐👤

A Python-based face recognition authentication system that allows users to **register and log in using facial recognition** instead of traditional passwords.  
The system generates and stores **face embeddings** during registration and later uses them to authenticate users during login.

---

## 🚀 Features

- Face-based **User Registration**
- Face-based **User Login**
- Secure facial embedding generation using **FaceNet**
- Stores user embeddings locally for fast recognition
- Stores registered usernames in **MySQL database**
- Simple and clean UI for login & registration

---

## 🛠️ Tech Stack

- **Python**
- **Flask**
- **OpenCV**
- **FaceNet (Keras)**
- **MySQL**
- **NumPy, Pickle**
- **HTML, CSS**

---

## 📸 Screenshots

### 🔹 Login Page
<img width="1906" height="1047" alt="Screenshot 2026-01-20 111036" src="https://github.com/user-attachments/assets/190296d9-5438-4051-b5e9-3311e4b9d444" />






### 🔹 Register Page
<img width="1910" height="972" alt="Screenshot 2026-01-20 111111" src="https://github.com/user-attachments/assets/58f14819-7caf-4aec-89a3-aa726e24f083" />

*(Images added in the repository)*

---

## ⚙️ Project Workflow

1. User uploads multiple face images during **registration**
2. System:
   - Detects face
   - Generates facial embeddings using FaceNet
   - Stores embeddings in `embeddings.pkl`
   - Saves username in MySQL database
3. During **login**:
   - Face is captured/uploaded
   - Embedding is generated
   - Compared with stored embeddings
   - User is authenticated if a match is found

---

---

## 📥 Model Setup (IMPORTANT)

This project uses **FaceNet model**, which is **not included** due to large file size.

### 🔗 Download FaceNet Model

Download `facenet_keras.h5` from the link below:

👉 https://www.kaggle.com/datasets/rmamun/kerasfaceneth5

### 📌 Steps

1. Download `facenet_keras.h5`
2. Paste `facenet_keras.h5` inside the `models` folder

---

## 🗄️ Database Setup

Create a MySQL database and table to store registered usernames.

### 🧩 Database Name
face_reco


# You can use:
- XAMPP
- WAMP
- Any MySQL Server

### How to run project :

- Clone the repository
- install requirements.txt `(pip install requirements.txt)`
- setup the `facenet_keras.h5` model (Read Above to know how to do it)
- Create `face_reco` named database in XAMPP or WAMP or any MYSQL server
- run   `app.py`


## How it Works
- During registration, users upload their face images.
- The system generates embeddings and stores them in embeddings.pkl.
- During login, the system compares the live face with stored embeddings to authenticate the user.

## 💡 Notes
- Keep embeddings.pkl in the project root. It stores all registered users’ face embeddings.
- Make sure MySQL service is running before starting the Flask app.
- The face_reco table stores all registered usernames.
- Users need to upload multiple images during registration for better recognition.


--

## 💡 Want to Contribute?
Contributions are welcome! 🎉 If you’d like to improve this project, please fork the repo and submit a pull request. You can also open issues for bugs, suggestions, or new features. Steps to contribute:
- 1. Fork the repository
- 2. Create a new branch 
- 3. Make your changes
- 4. Commit and push (`git commit -m "Add feature xyz"`)
- 5. Open a Pull Request



