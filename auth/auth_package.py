import sqlite3

connectionToDB = sqlite3.connect('./databases/users.db', check_same_thread=False)
cursor = connectionToDB.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        UNIQUE(username))'''

cursor.execute(create_table_query)
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
    print("user is in")
    