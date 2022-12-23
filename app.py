from flask import Flask, request, session
from flask_cors import CORS
from flask_oauthlib.client import OAuth
from flask_oauthlib.provider import OAuth2Provider
from oauthlib.oauth2 import TokenEndpoint
from requests_oauthlib import OAuth2Session
from auth import auth_package

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'sdvhkhdfbvxkjdfbkvdfbvkdvf'
oauth = OAuth(app)
token_endpoint = TokenEndpoint(app, grant_types=['password'], default_token_type='bearer')


@app.route('/<username>')
def index(username):
    return session.get(username)

@app.route('/login', methods=['POST'])
def login():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if not auth_package.check_user_credentials(username, password):
            return "Invalid credentials", 401
        else:
            # client = OAuth2Session()
            # token = client.fetch_token("https://localhost:5000", username=username, password=password, client_id=username, client_secret=password)
            # my_oauth_token = token_endpoint.create_token_response('')
            session[username] = (username, '')
            return "", 200

@app.route('/logout/<username>')
def logout(username):
    session.pop(username, None)
    return "", 200

@app.route('/register', methods=['POST'])
def signup():
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        auth_package.create_user(username, password)
        return "", 200
    else:
        return "", 404

@app.route('/change-password/<username>', methods=['POST'])
def change_password(username):
    if 'password' in request.form:
        password = request.form['password']
        auth_package.change_password(username, password)
        logout(username)
        return "", 200
    else:
        return "", 404

@app.route('/check-auth/<username>', methods=['POST'])
def check_auth(username):
    if username in session:
        return "", 200
    else:
        return "", 401


if __name__ == '__main__':
    app.run(debug=True)