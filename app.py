from flask import Flask, render_template, request
import sqlite3 as sql
from passlib.hash import sha256_crypt


app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        result = valid_login(request.form['UserName'], request.form['Password'])
        if result:
            return render_template('home.html', error=error, result=result)
        else:
            error = 'Invalid login credentials. Please try again.'
    return render_template('login.html', error=error)


def valid_login(user_name, password_in):
    connection = sql.connect('database.db')
    #cursor = connection.execute('SELECT * FROM users WHERE username=? AND hashedpass=?;',(user_name, sha256_crypt.hash(password_in)))
    cursor = connection.execute('SELECT * FROM users WHERE username=?;', (user_name,))
    connection.commit()
    try:
        hashedPassword = cursor.fetchone()[1]
        isMatch = sha256_crypt.verify(password_in, hashedPassword)
    except:
        isMatch = None
    return isMatch

def hash_passwords():
    connection = sql.connect('database.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    # Fetch all passwords
    passwords = cursor.execute('SELECT * FROM users;').fetchall()
    for passw in passwords:
        rowPassword = passw[1]
        hashedPassword = sha256_crypt.hash(rowPassword)
        cursor2.execute('UPDATE users SET hashedpass=? WHERE password=?;', (hashedPassword, rowPassword))
    connection.commit()
    connection.close()





if __name__ == "__main__":
    app.run()


