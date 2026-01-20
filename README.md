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
![Login Page](login.png)

### 🔹 Register Page
![Register Page](register.png)

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

## 📂 Project Structure



Face-Recognition-Login-Register-System/
│
├── app.py
├── embeddings.pkl
├── models/
│   └── facenet_keras.h5
├── templates/
│   ├── login.html
│   └── register.html
├── static/
│   └── styles.css
├── requirements.txt
└── README.md
📥 Model Setup (IMPORTANT)
This project uses FaceNet model, which is not included due to large file size.
🔗 Download FaceNet Model
Download facenet_keras.h5 from the link below:
👉 https://github.com/nyoki-mtl/keras-facenet/blob/master/model/facenet_keras.h5
📌 Steps:
Create a folder named models
Paste facenet_keras.h5 inside the models folder
Copy code

models/
└── facenet_keras.h5
🗄️ Database Setup
Create a MySQL database and table to store registered usernames.
🧩 Table Name
Copy code

face_reco
📄 SQL Query
Copy code
Sql
CREATE TABLE face_reco (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE
);
You can use:
XAMPP
WAMP
Any MySQL Server
▶️ How to Run the Project
1️⃣ Install Dependencies
Copy code
Bash
pip install -r requirements.txt
2️⃣ Configure Database
Update MySQL credentials in app.py:
Copy code
Python
host="localhost"
user="root"
password=""
database="your_database_name"
3️⃣ Run the Application
Copy code
Bash
python app.py
4️⃣ Open in Browser
Copy code

http://127.0.0.1:5000
📌 Important Files Explained
🔹 embeddings.pkl
Stores facial embeddings of all registered users
Used during login to recognize users by face
Automatically updated when a new user registers
🔹 face_reco Table
Stores registered usernames
Used to map embeddings to users
🔐 Security Notes
No passwords are stored
Authentication is based purely on face embeddings
Embeddings are stored locally for faster matching
📈 Future Improvements
Encrypt embeddings
Liveness detection
Multi-face handling
Cloud-based embedding storage
Role-based access
🤝 Contribution
Contributions are welcome!
Feel free to open issues or submit pull requests.
👨‍💻 Author
Hardik Gohel
Computer Engineering Student
Python | Flask | Machine Learning | Face Recognition
🔗 GitHub: https://github.com/Gohel-Hardik-M 


**Login Page**
<img width="1906" height="1047" alt="Screenshot 2026-01-20 111036" src="https://github.com/user-attachments/assets/190296d9-5438-4051-b5e9-3311e4b9d444" />



**Register Page**
<img width="1910" height="972" alt="Screenshot 2026-01-20 111111" src="https://github.com/user-attachments/assets/58f14819-7caf-4aec-89a3-aa726e24f083" />



