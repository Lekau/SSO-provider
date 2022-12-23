from flask import Flask, request, session
from flask_cors import CORS
from flask_oauthlib.client import OAuth
from auth import auth_package

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
    return session.get('my_oauth_token')

@app.route('/login', methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if not auth_package.check_user_credentials(username, password):
            return "Invalid credentials", 401
        else:
            my_oauth_token = nerdsSSOProvider.get_access_token(username, password)
            session[username] = (my_oauth_token.token, '')
            return "", 200

@app.route('/logout')
def logout():
    session.pop('my_oauth_token', None)
    return "", 200

@app.route('/register', methods=['POST'])
def signup():
    return "Register route endpoint"

@app.route('/change-password')
def change_password():
    return "Change password route endpoint"

@app.route('/check-auth/<username>', methods=['POST'])
def check_auth(username):
    if username in session:
        return "", 200
    else:
        return "", 401
