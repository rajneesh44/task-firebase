import pyrebase
from flask import Flask
from flask import render_template, request, redirect, session, flash
# from app import app
import os

app = Flask(__name__)
app.secret_key = 'many random bytes'
config = {
    "apiKey": "AIzaSyAkwb9HdBJ5biBLypINydaOP_SJitLICn4",
    "authDomain": "task-swe.firebaseapp.com",
    "databaseURL": "https://task-swe.firebaseio.com",
    "projectId": "task-swe",
    "storageBucket": "task-swe.appspot.com",
    "messagingSenderId": "458577196822",
    "appId": "1:458577196822:web:ac308d0aeadc1469ea0237",
    "measurementId": "G-057YPEQSX4"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            try:
                auth.sign_in_with_email_and_password(email, password)
                #user_id = auth.get_account_info(user['idToken'])
                #session['usr'] = user_id
                return render_template('home.html')
            except:
                unsuccessful = 'Please check your credentials'
                return render_template('index.html', umessage=unsuccessful)
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if (request.method == 'POST'):
            email = request.form['name']
            password = request.form['password']
            auth.create_user_with_email_and_password(email, password)
            successful = "Account created!"
            return render_template('create_account.html',smessage=successful)
    
    return render_template('create_account.html')

@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if (request.method == 'POST'):
            email = request.form['name']
            auth.send_password_reset_email(email)
            sc = "Password has been sent to your registered email id" 
            return render_template('index.html',smessage=sc)
    
    return render_template('forgot_password.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()
    