from flask import Flask, request, redirect, render_template, url_for, flash , jsonify
from util7 import register_user, recognize_face
import os 
import mysql.connector as conn

try :
    db = conn.connect(host="localhost",username="root",password="",database="face_reco")
    cursor = db.cursor(dictionary=True)
except ConnectionError as e:
    print("error :",e)
else :
    print("Connection Successfull !")

create_table = '''CREATE TABLE IF NOT EXISTS users (username varchar(100));
'''
cursor.execute(create_table)



fetch_name = '''SELECT username FROM users ;'''
cursor.execute(fetch_name)
users = cursor.fetchall()




app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def login_page():
    return render_template('login.html') 

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template('register.html')


@app.route('/register_action',methods=['GET','POST'])
def register_action():
    if request.method == 'POST':
        uploaded_imgs = request.files.getlist('photos')
        name= request.form['name']
        dob = request.form['dob']
        if uploaded_imgs:
           DIR = "C:/Users/hardi/Downloads/CS(EH)/DSA/register_photos"
           for idx, img in enumerate(uploaded_imgs):
               path = os.path.join(DIR, f"{idx}.png")
               img.save(path)

     #   print(name,uploaded_imgs.type(),dob)
        register_user(name,DIR)
        cursor.execute('INSERT INTO users (username) VALUES(%s)',(name,))
        
        return render_template('index.html')
    return render_template('register.html')
    
        


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print("Working HERE")
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo provided'}), 400
    
    file = request.files['photo']
    if not file :
        print("Photo not captured")
        
    DIR = "C:/Users/hardi/Downloads/CS(EH)/DSA/test photo"
    os.makedirs(DIR, exist_ok=True) 
    path = os.path.join(DIR,'personal_test.png')
    file.save(path)
    person = recognize_face("C:/Users/hardi/Downloads/CS(EH)/DSA/test photo/personal_test.png")
    if person in users:
        return render_template('index.html',name=person)
    # Process the photo (e.g., save temporarily, run face recognition)
    # For now, just return a success message
    else:
      return jsonify({'message': 'Login successful', 'user': 'Example User'})

'''

@app.route('/face_details', methods=['POST'])
def face_details():
    
    return render_template('index.html')




@app.route('/login', methods=['POST'])
def login():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo provided'}), 400
    
    file = request.files['photo']
    # Process the photo (e.g., save temporarily, run face recognition)
    # For now, just return a success message
    return jsonify({'message': 'Login successful', 'user': 'Example User'})
'''
if __name__ == '__main__':
    app.run(debug=True)
