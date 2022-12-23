import sqlite3

connectionToDB = sqlite3.connect('database/users.db')
cursor = connectionToDB.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
    );
''')
connectionToDB.commit()

def create_user(username, password):
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password))
    connectionToDB.commit()

def check_user_credentials(username, password):
    """Returns True if the user exists and the password is correct"""
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    return user is not None

def change_password(username, password):
    cursor.execute('''
        UPDATE users SET password = ? WHERE username = ?
    ''', (password, username))
    connectionToDB.commit()
    