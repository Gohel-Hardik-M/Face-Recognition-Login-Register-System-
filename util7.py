import os
import numpy as np
from mtcnn.mtcnn import MTCNN
from keras.models import load_model
from PIL import Image
import cv2
import pickle
from numpy import asarray
from numpy import expand_dims
from numpy import linalg as LA

# ---------------------------
# Load FaceNet model
# ---------------------------
model = load_model('model/facenet_keras.h5')
detector = MTCNN()



import cv2
import numpy as np

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
import cv2
import numpy as np

def extract_face(filename, required_size=(160, 160)):
    # Load the image
    img = cv2.imread(filename)
    if img is None:
        print("Error: Image not found or cannot be opened.")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier('model/haar_face.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    if len(faces) == 0:
        print("No face detected in", filename)
        return None

    # Take the first detected face (you can improve this by selecting the largest one)
    x, y, w, h = faces[0]

    # Crop the face region
    face = img[y:y+h, x:x+w]

    # Resize to required size
    face = cv2.resize(face, required_size)

    # Convert to float and normalize (as Facenet expects)
    face = face.astype('float32') / 255.0

    return face
# ---------------------------
# Function to extract face from image
# ---------------------------

# ---------------------------
# Get embedding using FaceNet
# ---------------------------

def preprocess_face(face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    return face_pixels

def get_embedding(model, face_pixels):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    samples = expand_dims(face_pixels, axis=0)
    yhat = model.predict(samples)
    return yhat[0]

# ---------------------------
# Register user (multiple images)
# ---------------------------
def register_user(user_name, image_folder):
    embeddings = []
    for filename in os.listdir(image_folder):
        path = os.path.join(image_folder, filename)
        face = extract_face(path)
        if face is not None:
            face_2 = preprocess_face(face)
            emb = get_embedding(model, face_2)
            embeddings.append(emb)
    if len(embeddings) == 0:
        print("No faces detected for", user_name)
        return
    embeddings = np.array(embeddings)
    mean_emb = np.mean(embeddings, axis=0)
    save_user_embedding(user_name, mean_emb)
    print(f"[✔] User {user_name} registered successfully!")

# ---------------------------
# Save embeddings
# ---------------------------
def save_user_embedding(user_name, embedding):
    if os.path.exists("embeddings.pkl"):
        with open("embeddings.pkl", "rb") as f:
            database = pickle.load(f)
    else:
        database = {}
    database[user_name] = embedding
    with open("embeddings.pkl", "wb") as f:
        pickle.dump(database, f)

# ---------------------------
# Recognize face from image
# ---------------------------import numpy as np
from numpy import linalg as LA
import pickle

def normalize(embedding):
    """Normalize embedding vector for stable distance comparison."""
    return embedding / LA.norm(embedding)

def recognize_face(image_path, threshold=1.1):
    # Step 1: Extract face from the image
    face = extract_face(image_path)
    if face is None:
        print("No face detected.")
        return

    # Step 2: Preprocess face and get embedding
    face_2 = preprocess_face(face)
    emb = get_embedding(model, face_2)
    emb = normalize(emb)  # 🔥 Normalize for stable comparison

    # Step 3: Load stored embeddings
    with open("embeddings.pkl", "rb") as f:
        database = pickle.load(f)

    # Step 4: Compare embeddings
    min_dist = float('inf')
    identity = "Unknown"

    for name, db_emb in database.items():
        db_emb = normalize(db_emb)  # 🔥 Ensure stored embedding is normalized too
        dist = LA.norm(db_emb - emb)
        if dist < min_dist:
            min_dist = dist
            identity = name

    # Step 5: Show results
    print(f"Closest distance = {min_dist:.4f}")
    if min_dist > threshold:
        identity = "Unknown"

    print("Recognized as:", identity)
    return identity

recognize_face("ws.jpg")
#DIR = "C:/Users/hardi/Downloads/CS(EH)/DSA/Celebrity Faces Dataset"
#people = []
#for person in os.listdir(DIR):
#    path_ = os.path.join(DIR,person)
#    register_user(person,path_)
    
