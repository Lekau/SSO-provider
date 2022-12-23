from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Default route endpoint"

@app.route('/login')
def login():
    return "Login route endpoint"

@app.route('/logout')
def logout():
    return "Logout route endpoint"

@app.route('/register')
def signup():
    return "Register route endpoint"

@app.route('/change-password')
def change_password():
    return "Change password route endpoint"

@app.route('/check-session')
def check_auth():
    return "Check session route endpoint"
