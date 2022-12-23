from flask import Flask, render_template, request,redirect, url_for, session
from flask_cors import CORS
from flask_oauthlib.client import OAuth


app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'sdvhkhdfbvxkjdfbkvdfbvkdvf'
oauth = OAuth(app)

nerdsSSOProvider = oauth.remote_app(
    'nerdsSSOProvider',
    consumer_key='acsac',
    consumer_secret='thhsfsdafa',
    request_token_params={'scope': 'username'},
    base_url='http://localhost:5000/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='http://localhost:5000/oauth/token',
    authorize_url='http://localhost:5000/oauth/authorize'
)

@nerdsSSOProvider.tokengetter
def get_oauth_token():
    return session.get('my_oauth_token')


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

@app.route('/check-auth')
def check_auth():
    return "Check auth route endpoint"
